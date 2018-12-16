import pandas as pd

df = raed_excel()

# 按指定列属性筛选行
df["运营商"] = df["运营商"].fillna('miss')
df_ben = df[df['运营商'].str.contains('中国电信')]
df_yi  = df[~df['运营商'].str.contains('中国电信')]





# 多列多条件筛选
df['是否线下转线上'] = df['是否线下转线上'].fillna("空")
df['是否线下模式'] = df['是否线下模式'].fillna("空")
# df['是否线下转线上'] = df['是否线下转线上'].map(lambda x:str(x))
# df['是否线下模式'] = df['是否线下模式'].map(lambda x:str(x))
ex_list = ['空','是否线下转线上']
# ex_list = ["空"]
# set = "是"
df1=df[(df['是否线下模式']=="是")&(df['是否线下转线上'].isin(ex_list))]
df = df.drop(df1.index)
print("去掉线下后：" + str(df.shape))

# 多重筛选函数并输出
def getTmall(data):
    PV = data['浏览量'].sum()
    print("总PV：{}".format(PV))
    UV = data['访客数'].sum()
    print("总UV：{}".format(UV))
    data = data[data['支付商品件数'] != 0]


    data_chongzhi = data[data['商品标题'].str.contains('充值')]
    data_huafei = data_chongzhi[data_chongzhi['商品标题'].str.contains('话费')]
    print(data_huafei.shape)#对

    index = ~data[u'商品标题'].isin(data_huafei[u'商品标题'])
    data = data[index]
    print(data.shape)
    data = data[~data['商品标题'].str.contains('测试')]
    print(data.shape)


    payBuyerNum = np.sum(data['支付买家数'])
    print("PC端—非充值类买入人数：{}".format(payBuyerNum))
    payProNum = np.sum(data['支付商品件数'])
    print("PC端—非充值类支付件数：{}".format(payProNum))
    data_luoji = data[data['商品标题'].str.contains('#')]

    index2 = ~data[u'商品标题'].isin(data_luoji[u'商品标题'])
    data  = data[index2]
    data_haoka = data[data['商品标题'].str.contains('号卡')]
    index3 = ~data[u'商品标题'].isin(data_haoka[u'商品标题'])
    data_liuliangbao = data[index3]
    return data_haoka,data_huafei,data_liuliangbao,data_luoji

HK,HF,LLB,LJ = getTmall(dataA)


data1.to_excel(writer,'总表',index=False)
HF.to_excel(writer, sheet_name='话费',index=False)
LLB.to_excel(writer, sheet_name='流量包',index=False)
HK.to_excel(writer, sheet_name='号卡',index=False)
LJ.to_excel(writer, sheet_name='裸机',index=False)
writer.save()