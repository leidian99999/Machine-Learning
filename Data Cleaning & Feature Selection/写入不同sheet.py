writer=pd.ExcelWriter(r'G:\work\日报\短信反馈\新表.xlsx')
ages.to_excel(writer,sheet_name='sheet1')
category.to_excel(writer,sheet_name='sheet2')
 
#必须运行writer.save()，不然不能输出到本地
writer.save()