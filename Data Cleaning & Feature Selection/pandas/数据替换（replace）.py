#Series对象值替换
s = df.iloc[2]#获取行索引为2数据
#单值替换
s.replace('?',np.nan)#用np.nan替换？
s.replace({'?':'NA'})#用NA替换？
#多值替换
s.replace(['?',r'$'],[np.nan,'NA'])#列表值替换
s.replace({'?':np.nan,'$':'NA'})#字典映射
#同缺失值填充方法类似
s.replace(['?','$'],method='pad')#向前填充
s.replace(['?','$'],method='ffill')#向前填充
s.replace(['?','$'],method='bfill')#向后填充
#limit参数控制填充次数
s.replace(['?','$'],method='bfill',limit=1)
#DataFrame对象值替换
#单值替换
df.replace('?',np.nan)#用np.nan替换？
df.replace({'?':'NA'})#用NA替换？
#按列指定单值替换
df.replace({'EMPNO':'?'},np.nan)#用np.nan替换EMPNO列中?
df.replace({'EMPNO':'?','ENAME':'.'},np.nan)#用np.nan替换EMPNO列中?和ENAME中.
#多值替换
df.replace(['?','.','$'],[np.nan,'NA','None'])##用np.nan替换？用NA替换. 用None替换$
df.replace({'?':'NA','$':None})#用NA替换？ 用None替换$
df.replace({'?','$'},{'NA',None})#用NA替换？ 用None替换$
#正则替换
df.replace(r'\?|\.|\$',np.nan,regex=True)#用np.nan替换？或.或$原字符
df.replace([r'\?',r'\$'],np.nan,regex=True)#用np.nan替换？和$
df.replace([r'\?',r'\$'],[np.nan,'NA'],regex=True)#用np.nan替换？用NA替换$符号
df.replace(regex={r'\?':None})
#value参数显示传递
df.replace(regex=[r'\?|\.|\$'],value=np.nan)#用np.nan替换？或.或$原字符


dict = {'焦作市':'河南','河南省':'河南','河北省':'河北','贵州省':'贵州','湖南省':'湖南','广东省':'广东','江苏省':'江苏','山西省':'山西',
        '吉林省':'吉林','山东省':'山东','广西壮族自治区':'广西','湖北省':'湖北','陕西省':'陕西','浙江省':'浙江','福建省':'福建',
        '内蒙古自治区':'内蒙古','云南省':'云南','辽宁省':'辽宁','江西省':'江西','四川省':'四川','黑龙江省':'黑龙江','安徽省':'安徽',
        '甘肃省':'甘肃','西藏自治区':'西藏','青海省':'青海','宁夏回族自治区':'宁夏',
        '海南省':'海南','六安市':'安徽','东莞市':'广东','新疆维吾尔自治区':'新疆'}

df1 = df.replace(dict)