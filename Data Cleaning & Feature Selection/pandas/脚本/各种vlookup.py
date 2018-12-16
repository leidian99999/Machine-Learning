'''
# 形式一
问题：A3:B7单元格区域为字母等级查询表，
表示60分以下为E级、60~69分为D级、70~79分为C级、80~89分为B级、90分以上为A级。
D:G列为初二年级1班语文测验成绩表，如何根据语文成绩返回其字母等级？
'''

df = pd.read_excel("test.xlsx", sheet_name=0)
def grade_to_point(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'E'
df['等级'] = df['语文'].apply(grade_to_point)

#
'''
形式二
在Sheet1里面如何查找折旧明细表中对应编号下的月折旧额？（跨表查询）
'''

df1 = pd.read_excel("test.xlsx", sheet_name='折旧明细表')
df2 = pd.read_excel("test.xlsx", sheet_name=1) #题目里的sheet1
df2.merge(df1[['编号', '月折旧额']], how='left', on='编号')


'''
形式三
类似于案例二，但此时需要使用近似查找
'''
df1 = pd.read_excel("test.xlsx", sheet_name='折旧明细表')
df3 = pd.read_excel("test.xlsx", sheet_name=3) #含有资产名称简写的表
df3['月折旧额'] = 0
for i in range(len(df3['资产名称'])):
    df3['月折旧额'][i] = df1[df1['资产名称'].map(lambda x:df3['资产名称'][i] in x)]['月折旧额']
print(df3)

'''
形式四
问题：在Excel中录入数据信息时，为了提高工作效率，用户希望通过输入数据的关键字后，自动显示该记录的其余信息，
例如，输入员工工号自动显示该员工的信命，输入物料号就能自动显示该物料的品名、单价等。
如图所示为某单位所有员工基本信息的数据源表，
在“2010年3月员工请假统计表”工作表中，当在A列输入员工工号时，
如何实现对应员工的姓名、身份证号、部门、职务、入职日期等信息的自动录入？

'''
df4 = pd.read_excel("test.xlsx", sheet_name='员工基本信息表')
df5 = pd.read_excel("test.xlsx", sheet_name='请假统计表')
df5.merge(df4[['工号', '姓名', '部门', '职务', '入职日期']], on='工号')

'''
形式五
问题：用VLOOKUP函数实现批量查找，VLOOKUP函数一般情况下只能查找一个，
那么多项应该怎么查找呢？如下图，如何把张一的消费额全部列出？
'''
df6 = pd.read_excel("test.xlsx", sheet_name='消费额')
df6[df6['姓名'] == '张一'][['姓名', '消费额']]


