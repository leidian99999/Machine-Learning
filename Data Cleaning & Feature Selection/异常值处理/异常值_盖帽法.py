import pandas as pd
def cap(x,quantile = [0.01,0.99]):
    '''
    x:pd.Series 列，连续变量
    quantile:指定盖帽法的上下分位数范围
    '''
    # 生成分位数
    Q01,Q99 = x.quantile(quantile).value.tolist()
    # 替换异常值为指定的分位数
    if Q01 > x.min():
        x = x.copy()
        x.loc[x<Q01] = Q01
    if Q99 < x.max():
        x = x.copy()
        x.loc[x>Q99] = Q99
        return(x)

# 验证效果
sample = pd.DataFrame({"normal" : np.random.randn(1000)})
sample.hist(bins=50)

new =sample.apply(cap,quantile=[0.01,0.99])
new.hist(bins=50)