'''
DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


n是要抽取的行数。（例如n=20000时，抽取其中的2W行）

frac是抽取的比列。
（有一些时候，我们并对具体抽取的行数不关系，我们想抽取其中的百分比，这个时候就可以选择使用frac，例如frac=0.8，就是抽取其中80%）

replace抽样后的数据是否代替原DataFrame()

weights这个是每个样本的权重，具体可以看官方文档说明。

random_state这个在之前的文章已经介绍过了。

axis是选择抽取数据的行还是列。axis=0的时是抽取行，axis=1时是抽取列（也就是说axis=1时，在列中随机抽取n列，在axis=0时，在行中随机抽取n行）
'''


import pandas as pd

data =pd.read_excel("G:/work/日报/短信/181026/181026短信导出_字段.xlsx")
print(data.shape)

df1 = data.sample(n=20)
print(df1.shape)

out =  "E:\\backup\\基本语法\\pandas\\"
df1.to_excel(out+"sample.xlsx",index=False)