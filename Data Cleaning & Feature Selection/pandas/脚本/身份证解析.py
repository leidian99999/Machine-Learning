import pandas as pd
import numpy as np
import datetime
import time

df = pd.read_excel(r"G:\work\日报\短信反馈\每日激活量\11.1-11.25激活量.xlsx",usecols=[28,34,40,65])
biaoka = pd.read_excel("G:/work/日报/功能列表/产品标卡.xlsx")

df= df[df["入网身份证号"].notnull()]

# 号码所属地分列
split = pd.DataFrame((x.split('/') for x in df['号码归属地']),index=df.index,columns=["所属省","所属地区"])
df = pd.merge(df,split,left_index=True,right_index=True)

df["销售品编号"] = df["销售品编号"].map(lambda x:str(x))
biaoka["销售品编号"] = biaoka["销售品编号"].map(lambda x:str(x))
df = pd.merge(df,biaoka,how="left",on="销售品编号")

df["生日"] = df["入网身份证号"].str[6:14]
df["生日"] = pd.to_datetime(df["生日"])
now_year = datetime.datetime.today().year
df["年龄"] = now_year - df["生日"].dt.year

df["sex"] = df["入网身份证号"].str[-2]
df = df[df['入网身份证号'].str.contains("入网身份证号") == False]
df["sex"] = df["sex"].astype("int")

sex = []
num = df["sex"]
for x in num:
    if x % 2 == 0:
        sex.append("女")
    else:
        sex.append("男")

df["性别"] = sex

df.to_excel(r"G:\work\日报\短信反馈\11.1-11.25激活明细.xlsx",index=False)

'''日期计算'''


#计算激活时效
df_out['订单生成日期'] = pd.to_datetime(df_out['订单生成日期'])
df_out['交易完成日期'] = pd.to_datetime(df_out['交易完成日期'])
df_out["激活时效"] = (df_out['交易完成日期'] - df_out['订单生成日期']).dt.days


'''
分组
'''
# 区分沉默用户
bins =[0,10,100] 
df_new['silence'] = pd.cut(df_new['激活时效'],bins,labels=["非沉默用户","沉默用户"])

# 区分年龄段
df_new['birthday'] = df_new['入网身份证号'].str[6:14]
df_new['birthday'] = pd.to_datetime(df_new["birthday"])
now_year =datetime.datetime.today().year #当前的年份
df_new['age']=now_year-df_new["birthday"].dt.year
bins2 = [0,18,25,35,45,55,200]
df_new['age_group'] = pd.cut(df_new['age'],bins2,labels=["18岁及以下","19-25岁",'26-35岁','36-45岁','46-55岁','56岁及以上'])


'''透视表'''
# 分卡品
category = pd.pivot_table(df_new,index=[u'分类',u'silence'],values=['激活时效'],
                          aggfunc=[np.mean,len],fill_value = 0,
                          margins = True,margins_name = '合计')

# 分省
province = pd.pivot_table(df_new,index=[u'所属省',u'silence'],values=['激活时效'],
                          aggfunc=[np.mean,len],fill_value = 0,
                          margins = True,margins_name = '合计')
# 分年龄段 
ages = pd.pivot_table(df_new,index=[u'age_group',u'silence'],values=['激活时效'],
                      aggfunc=[np.mean,len],fill_value = 0,
                      margins = True,margins_name = '合计')