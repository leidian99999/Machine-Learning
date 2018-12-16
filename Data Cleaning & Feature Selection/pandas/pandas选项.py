'''
get_option() 显示设置默认值
set_option() 修改设置默认值
reset_option() 还原默认值
describe_option()
option_context()

参数：
display.max_rows:要显示的最大行数
display.max_columns:显示最大列数
display.expand_frame_repr:显示数据帧以拉伸页面
display.maxcolwidth:显示最大列宽
display.precision:显示十进制数的精度
'''

import pandas as pd

# get_option(param)


# display.max_rows默认60
print("display.max_rows = ",pd.get_option("display.max_rows"))

# display.max_columns 默认20
print ("display.max_columns = ", pd.get_option("display.max_columns"))
print("*"*30)

# set_option(param,value)

# display.max_rows 更改默认值
print("before set display.max_rows = ",pd.get_option("display.max_rows"))
pd.set_option("display.max_rows",80)
print("after set display.max_rows = ",pd.get_option("display.max_rows"))

# display.max_columns 更改默认值
print("befor set display.max_columns = ",pd.get_option("display.max_columns"))
pd.set_option("display.max_columns",32)
print("after set display.max_columns = ",pd.get_option("display.max_columns"))
print("*"*30)

# reset_option(param)

pd.set_option("display.max_rows",32)
print("after set display.max_rows = ",pd.get_option("display.max_rows"))
pd.reset_option("display.max_rows")
print("reset display.max_rows = ",pd.get_option("display.max_rows"))
print("*"*30)

# describe_option(param) 打印参数的描述
# pd.describe_option("display.max_rows")

# option_context() 
# 上下文管理器用于临时设置语句中的选项。当退出使用块时，选项值将自动恢复

with pd.option_context("display.max_rows",10):
	print(pd.get_option("display.max_rows"))
	print(pd.get_option("display.max_rows"))

# 请参阅第一和第二个打印语句之间的区别。第一个语句打印由option_context()设置的值，该值在上下文中是临时的。
# 在使用上下文之后，第二个打印语句打印配置的值。