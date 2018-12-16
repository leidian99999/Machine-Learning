import pandas as pd
import numpy as np

#读取文件
data = pd.read_excel("D:/work/dong/test/9.13数据9.14取.xlsx")

# print(data.head(3))

# df1 = pd.read_excel("D:/work/dong/test/test1.xlsx")
# df2 = pd.read_excel("D:/work/dong/test/test2.xlsx")

# print("df1")
# print(df1.shape)
# print("*"*100)

# print("df2")
# print(df2.shape)

# 使用shape获取数据维度(行列)
#print(data.shape)

# 使用info查看数据表信息
# print(data.info)
#
# 使用dtypes函数查看数据类型
#print(data.dtypes)


# 使用Isnull检验数据表中的空值
#print(data.isnull())

# 使用Unique查看是否唯一值 只能对特定的列进行操作
print(data['订单状态'].unique())

# 用values查看数据表数值
#print(data.values)

# 用columns查看列名称
print(data.columns)

# 用head函数查看前n行数据
#print(data.head(5))

# 用tail函数查看后n行数据
#print(data.tail(3))

# Python处理空值可以用dropna函数删除包含空值的数据
# 或者使用fillna函数对空值进行填充
#print(data.dropna(how='any'))
# 使用数字0填充数据表中空值
#print(data.fillna(value=0))
# 使用均值来填充缺省值
#print(data['列名'].fillna(data['列名'].mean()))

# 清理空格特定列
# print(data['xuhao'].map(str.strip))

# 大小写转换
# print(data['xuhao'].str.upper())

# 使用astype函数修改数据格式
# print(data['序号'].astype('float'))

# 使用Rename函数修改列名称
#print(data.rename(columns={'订单编号': '订单标号'}))

# 使用drop_duplicates函数删除重复值
# print(data['序号'].drop_duplicates())
# 指定保留最后一位重复数
# print(data['序号'].drop_duplicates(keep='last'))

# 使用replace函数实现数据替换
#print(data['列名'].replace('指定值', 'A'))

# 使用merge函数实现excel表格的合并，合并方式为inner,内连接，取交集
# df_inner = pd.merge(df1, df2, how='inner')
# print(df_inner.shape)
# # 对df_inner数据表设置索引列
# df_inner.set_index('id')
#
# # 使用sort_values函数或sort_index函数对数据排序
# # 特定列的值排序
# df_inner.sort_values(by=['age'])
# # 按索引对数据进行排序
# df_inner.sort_index()
#
# # 使用where对数据进行判断和分组，并使用group字段进行标记
# # 如果price列的值>3000,group列显示hinh,否则显示low
# df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
# # 对符合多个条件的数据进行分组标记
# # 下面代码中对city列等于beijing且price列大于等于4000的数据标记为1
# df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1
#
# # 使用split函数对字段进行拆分，并将拆分后的数据表匹配回源数据表中
# # 假设category列中的数据包含两个信息，前面的数字类别为id,后面的字母为size,中间以连字符进行连接
# # 对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size
# pd.DataFrame((x.split('-') for x in df_inner['category']), index=df_inner.index, columns=['category', 'size'])
# # 将完成分列后的数据表与原df_inner数据表进行匹配
# df_inner = pd.merge(df_inner, split, right_index=True, left_index=True)
#
# # 数据提取，主要使用loc和iloc及ix三个函数实现。
# # loc函数按标签值进行提取，iloc函数按位置进行提取，ix函数可以同时按标签和位置进行提取
# # 按索引提取单行的数值
# df_inner.loc[3]
# # 按索引提取区域行的数值
# df_inner.loc[0:5]
#
# # Res_index函数用于恢复索引
# # 重设索引
# df_inner.reset_index()
# # 设置日期为索引
# df_inner = df_inner.set_index('date')
# # 提取4日(指定日期)之前的所有数据
# df_inner[:'2013-01-04']
#
# # 使用iloc按位置区域提取数据
# df_inner.iloc[:3, :2]
# # iloc函数除了可以按区域提取数据，还可以按位置逐条提取
# # 前方括号中的数据表示所在行的位置，后面括号中的数表示所在列的位置
# df_inner.iloc[[0, 2, 5], [4, 5]]
#
# # 使用ix索引标签(行)和位置(列)混合提取数据
# df_inner.ix[:'2013-01-04', :4]
#
# # 按条件提取数据
# # 使用isin函数对city中的值是否为beijing进行判断
# # 判断city列的值是否为beijing
# df_inner['city'].isin(['beijing'])
# # 先判断city列里是否包含beijing和shanghai,然后将符合条件的数据提取出来
# df_inner.loc[df_inner['city'].isin(['beijing'])]
#
# # 使用与，或，非三个条件配合大于，小于和等于对数据进行筛选，并进行计数和求和
# # 使用“与”条件进行筛选 年龄大于25且城市为北京
# df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']]
# # 使用“或”条件进行筛选 年龄大于25或城市为北京
# df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort(['age'])
#
# # 使用sum对字段进行求和
# # 对筛选后的数据按price字段进行求和
# df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender','price']].sort(['age']).price.sum()
#
# # 使用"非"条件进行筛选
# df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id'])
# # 使用count进行计数
# #对筛选后的数据按city列进行计数
# df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()
# # 使用query函数进行筛选
# df_inner.query('city == ["beijing", "shanghai"]')
# # 对筛选后的结果按price进行求和
# df_inner.query('city == ["beijing", "shanghai"]').price.sum()
#
# # python中使用groupby和pivot_table对数据进行汇总
# # groupby按列名称出现的顺序进行分组，同时要制定分组后的汇总方式，常见的是计数和求和两种
# # 对所有列进行计数汇总
# df_inner.groupby('city').count()
# # 可以在groupby中设置列名称来对特定的列进行汇总
# # 下面代码中按城市对id字段进行汇总计数
# # 对特定的id列进行计数汇总
# df_inner.groupby('city')['id'].count()
# # 分别对city和size两个字段进行计数汇总
# df_inner.groupby(['city', 'size'])['id'].count()
# # 除了计数和求和外，还可以对汇总后的数据同时按照多个维度进行计算
# # 下面的代码中按城市对price字段进行汇总，并分别计算price的数量，总金额和平均数
# # 对city字段进行汇总并计算price的合计和均值
# df_inner.groupby('city')['price'].agg([len, np.sum, np.mean])
#
# # 通过pivot_table函数实现数据透视表功能
# # 下面的代码中设定city为行字段，size为列字段，price为值字段
# # 分别计算price的数量和金额并且按照行与列进行汇总
# # 数据透视表
# pd.pivot_table(df_inner, index=['city'], values=['price'], columns=['size'], aggfunc=[len,np.sum], fill_value=0, margins=True)
#
# # python通过sample函数完成数据采样
# # sample是进行数据采样的函数，设置n的数量就可以，自动返回
# # 简单的数据采样
# df_inner.sample(n=3)
# # weights参数是采样的权重，通过设置不同的权重可以更改采样的结果，权重高的数据将更有希望被选中
# # 手动设置采样权重
# weights = [0, 0, 0, 0, 0.5, 0.5]
# df_inner.sample(n=2, weights=weights)
# # sample函数中的参数replace用来设置采样后是否放回
# # 采样后不放回
# df_inner.sample(n=6, replace=False)
# # 采样后放回
# df_inner.sample(n=6, replace=True)
#
# # python通过describe对数据进行描述统计
# # describe函数自动生成数据的数量，均值，标准差等数据
# # 下面的代码对数据表进行描述统计，并使用round函数设置结果显示的小数位，并进行转置
# # 数据表描述性统计
# df_inner.describe().round(2).T
# # python中使用std函数用来计算特定数据列的标准差
# df_inner['price'].std()
# # Python使用cov函数计算亮哥字段或数据表中各字段间的协方差
# # 计算两个特定字段间的协方差
# df_inner['price'].cov(df_inner['m-point'])
# # 计算数据表中所有字段间的协方差
# df_inner.cov()
# # Python中使用corr函数完成数据相关分析的操作，并返回相关系数
# # 计算两个特定字段间的相关性
# df_inner['price'].corr(df_inner['m-point'])
# # 计算整个数据表的相关性
# df_inner.corr()
#
# # 导出文件
# # 输出到excel格式
# df_inner.to_Excel('Excel_to_Python.xlsx', sheet_name='bluewhale_cc')
# # 输出到csv文件
# df_inner.to_csv('Excel_to_Python.csv')