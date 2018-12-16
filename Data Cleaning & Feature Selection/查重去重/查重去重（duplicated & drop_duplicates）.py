#选取重复的项(每个重复取单个)
df2 = df1.drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep='first')
df3 = df1.drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep=False)
df4 = df2.append(df3).drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep=False)
df4.to_excel(outer,index=False)

#选取所有重复项明细
df1["重复行"] = df1.duplicated(subset=['配送省份名称','入网用户姓名'],keep=False)
df1["重复行"].value_counts()
df2 = df1[df1["重复行"]==True]
df2.to_excel(outer,index=False)