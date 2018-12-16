import pandas as pd


out_xlsx=in_f_name+'-group.xlsx'

df_group=df.groupby(['推广计划','推广组']).describe().reset_index()

df_group.to_excel(out_xlsx, sheet_name='Sheet1',index=False)
