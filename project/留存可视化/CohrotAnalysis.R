library('xlsx')
library('ggplot2')
library('dplyr')
library('magrittr')
library('tidyr')
library('reshape2')

#step1、设置工作路径并导入数据
setwd('D:/backup/')
df <- read.xlsx('D:/backup/projects/留存可视化/relay-foods.xlsx',sheetName = 'Purchase Data - Full Study')



#step2、清洗数据
#存留分析使用到的字段只有用户购买日期、用户ID等信息，
#分析月度存留，需要将日期规范化成年月形式，
#同时按照客户id分组，计算出用户首次购买的日期

#创建购买月份字段
df$OrderPeriod = format(df$OrderDate,'%Y-%m')   #购买日期

#创建用户首次购买字段
CohortGroup = df %>% group_by(UserId) %>% 
  summarize( CohortGroup = min(OrderDate)) 

#计算用户首购日期
CohortGroup$CohortGroup <-  CohortGroup$CohortGroup %>% 
  format('%Y-%m') 

df <- df %>% left_join(CohortGroup,by = 'UserId')  
#将首购日期与原始订单表合并对齐

#分组（按照首购日期、购买日期）计算总用户数、总订单数、总支付金额（用户ID要去重）
chorts <- df %>% group_by(CohortGroup,OrderPeriod) %>% 
  summarize(
    UserId  = n_distinct(UserId),
    OrderId = n_distinct(OrderId),
    TotalCharges = sum(TotalCharges)
  ) %>% rename(TotalUsers= UserId , TotalOrders = OrderId)

#按照用户首购日期分组并根据各个首购日期内的购买日期顺序添加顺序标签
chorts <- chorts %>% 
  arrange(CohortGroup,OrderPeriod) %>% 
  group_by(CohortGroup) %>% 
  mutate( CohortPeriod =row_number())


#step3、计算当月购买用户数
cohort_group_size <- chorts %>% 
  filter(CohortPeriod == 1) %>% 
  select(CohortGroup,OrderPeriod,TotalUsers)

user_retention <- chorts %>% 
  select(CohortGroup,CohortPeriod,TotalUsers) %>% 
  spread(CohortGroup,TotalUsers) 
#长表转换为宽表

#将具体用户数换算为占基准月份比率
user_retention[,-1] <- user_retention[,-1] %>% 
  t() %>% 
  `/`(cohort_group_size$TotalUsers) %>%
  t() %>%
  as.data.frame()

#宽表转为长表
user_retention1 <- user_retention %>% select(1:5) %>% 
  melt( 
    id.vars = 'CohortPeriod', 
    variable.name = 'CohortGroup', 
    value.name = 'TotalUsers'
  )

#step4、留存曲线
ggplot(user_retention1,aes(CohortPeriod,TotalUsers)) +
  geom_line(aes(group = CohortGroup,colour = CohortGroup)) +
  scale_x_continuous(breaks = 1:15) +
  scale_colour_brewer(type = 'div')

#展示了2009-01~2009~04四个月份的用户留存趋势！

user_retentionT <- t(user_retention) %>% .[2:nrow(.),]  %>% as.data.frame
user_retentionT$CohortPeriod <- row.names(user_retentionT)
row.names(user_retentionT) <- NULL
user_retentionT <- user_retentionT[,c(16,1:15)]

user_retentionT1 <- user_retentionT %>% 
  melt( 
    id.vars = 'CohortPeriod', 
    variable.name = 'CohortGroup', 
    value.name = 'TotalUsers'
  )

#step5、存留分析热力图
library("Cairo")
library("showtext")

font_add("myfont","msyh.ttc")
CairoPNG("C:/Users/RAINDU/Desktop/emoji1.png",1000,750)
showtext_begin()
ggplot(user_retentionT1 ,aes(CohortGroup,CohortPeriod,fill=TotalUsers))+
  geom_tile(colour='white') +
  geom_text(aes(label = ifelse(TotalUsers != 0,paste0(round(100*TotalUsers,2),'%'),'')),colour = 'blue') +
  scale_fill_gradient2(limits=c(0,.55),low="#00887D", mid ='yellow', high="orange",midpoint = median(user_retentionT1$TotalUsers, na.rm =TRUE),na.value = "grey90") +
  scale_y_discrete(limits = rev(unique(user_retentionT1$CohortPeriod))) +
  scale_x_discrete(position = "top")+
  labs(title="XXX产品Chort留存分析",subtitle="XXX产品在2019年1月至2010年三月中间的留存率趋势")+
  theme(
    text = element_text(family = 'myfont',size = 15),
    rect = element_blank()
  )
showtext_end()
dev.off()