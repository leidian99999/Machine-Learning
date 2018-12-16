import pandas as pd

#生成数据
newdata=pd.DataFrame([[1,1,1,1],[1,1,1,1],[2,1,4,3],[5,6,7,9],[5,4,2,1],[2,1,4,9]],columns=['A','B','C','D'])
print(newdata)
'''
参数：
subset=  ：对应的值是列名，表示只考虑这两列，将这两列对应值相同的行进行去重。默认值为subset=None表示考虑所有列。

keep= ：'first'表示保留第一次出现的重复行，是默认值。keep另外两个取值为"last"和False，分别表示保留最后一次出现的重复行和去除所有重复行。

inplace= ：  True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本。
'''
#四列中都重复的行删除，不保留
new1 = newdata.drop_duplicates(subset=['A','B','C','D'],keep=False)
print(new1)
#AB两列中的重复行删除，保留一个重复元素
new2 = newdata.drop_duplicates(subset=['A','B'],keep='first')
print(new2)

new3 = newdata.drop_duplicates(subset=['A'],keep='first')
print(new3)