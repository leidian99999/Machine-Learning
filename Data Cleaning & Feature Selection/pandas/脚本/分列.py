import pandas as pd


print('合并前列数%s' % data.shape[1])
split = pd.DataFrame((x.split('/') for x in data['号码归属地']), index=data.index, columns=['所属省','地区'])
data = pd.merge(data,split,left_index=True,right_index=True)
print('合并后列数%s' % data.shape[1])