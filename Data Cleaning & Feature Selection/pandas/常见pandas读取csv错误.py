1.Initializing from file failed
解决方法：   
path = 'D:/GFZQ/GFZQ/project/7_30_test/data/conferences/ST獐岛2016年度业绩说明会.csv'
f = open(path,encoding='UTF-8')
df_data = pd.read_csv(f)

2.路径错误：文件名中存在中文名或转义字符\
FileNotFoundError: File b'../数据.csv' does not exist
当文件名存在中文和转义字符时，前面加上u或者r指定字符串编码，并且尽量避免使用中文作为文件名
# False
data = pd.read_csv(u'./数据.csv')  
# Right
data = pd.read_csv(u'./data.csv')


数据格式错误：由于字段中存在分隔符逗号，导致数据串行
Error tokenizing data. C error: Expected 3 fields in line 3, saw 5
3.当文件仅有很少的行出现错误时，如数据不是太重要，可选择跳过错误的行。

#跳过错误的行
data = pd.read_csv('./data.csv',error_bad_lines = False)
with open('./data.csv',r) as file:
    rows = len(file.readlines())-1

#打印跳过的行数
print(len(data)-rows)





编码错误：读取文件的解码模式不同于文件编码格式。例如文件使用utf-8编码，读取时指定编码格式为gbk。文本中存在一些特殊字符超出了解码范围，例如生僻繁体字或日文
'gbk/utf-8' codec can't decode byte 0xa2 in position 147: illegal multibyte sequence

2. 文件解码格式存在错误时，查看源文件编码或更换几个常用编码格式读取试试。

for i in ('gbk','utf-8','gb18030','ansi'): 
    try:
        data = pd.read_csv('./data.csv',encoding = i)
        print(i + 'decode success')
    except:
        print(i + 'decode fail')



4.在写入文件时，使用在未在字段中出现的符号作为分隔符！！！
#查看串行列分隔符规律
with open('./data.csv','r',encoding='utf-8') as file:
    rows = file.readlines()
    sep_cnt = rows[0].count(',')
    for i in rows:
        cnt = i.count(',')
        if cnt!=sep_cnt:
            print(i)

###查看报错行分隔符规律
吴哥,{"年龄":28,"兴趣":"拉面","口头禅":"又大又圆"},666

热猫,{"年龄":38,"兴趣":"交友","口头禅":"这是我的小老弟"},88

阿越,{"年龄":39,"兴趣":"打篮球","口头禅":"我觉得不行"},66

###利用正则表达式正确分隔
import pandas as pd
data = pd.read_csv('./data.csv',sep = ',(?!")',encoding='utf8')
data.head()


5.万能纠错模式
import pandas as pd

for decode in ('gbk','utf-8','gb18030'):
    try:    
        data = pd.read_csv('./data.csv',encoding=decode,error_bad_lines=False)
        print('data-' +  decode + '-success!!')
        break
    except:
        pass