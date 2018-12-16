import pandas as ps

1、pd.set_option('expand_frame_repr', False)

True就是可以换行显示。设置成False的时候不允许换行

2、pd.set_option('display.max_rows', 10)

pd.set_option('display.max_columns', 10)

显示的最大行数和列数，如果超额就显示省略号，这个指的是多少个dataFrame的列。如果比较多又不允许换行，就会显得很乱。

3、pd.set_option('precision', 5)

显示小数点后的位数

4、pd.set_option('large_repr', A)

 truncate表示截断，info表示查看信息，一般选truncate

5、pd.set_option('max_colwidth', 5)

列长度

6、pd.set_option('chop_threshold', 0.5)

绝对值小于0.5的显示0.0

7、pd.set_option('colheader_justify', 'left')

 显示居中还是左边，

8、pd.set_option('display.width', 200)

横向最多显示多少个字符， 一般80不适合横向的屏幕，平时多用200.