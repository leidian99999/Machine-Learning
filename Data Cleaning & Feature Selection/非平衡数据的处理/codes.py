# 导入第三方包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics
from imblearn.over_sampling import SMOTE

# 读取数据
churn = pd.read_excel(r'C:\Users\Administrator\Desktop\Customer_Churn.xlsx')
churn.head()

# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 为确保绘制的饼图为圆形，需执行如下代码
plt.axes(aspect = 'equal')
# 统计交易是否为欺诈的频数
counts = churn.churn.value_counts()
# 绘制饼图
plt.pie(x = counts, # 绘图数据
        labels=pd.Series(counts.index).map({'yes':'流失','no':'未流失'}), # 添加文字标签
        autopct='%.2f%%' # 设置百分比的格式，这里保留一位小数
       )
# 显示图形
plt.show()


# 数据清洗
# 删除state变量和area_code变量
churn.drop(labels=['state','area_code'], axis = 1, inplace = True)

# 将二元变量international_plan和voice_mail_plan转换为0-1哑变量
churn.international_plan = churn.international_plan.map({'no':0,'yes':1})
churn.voice_mail_plan = churn.voice_mail_plan.map({'no':0,'yes':1})
churn.head()


# 用于建模的所有自变量
predictors = churn.columns[:-1]
# 数据拆分为训练集和测试集
X_train,X_test,y_train,y_test = model_selection.train_test_split(churn[predictors], churn.churn, random_state=12)

# 构建决策树
dt = tree.DecisionTreeClassifier()
dt.fit(X_train,y_train)
# 模型在测试集上的预测
pred = dt.predict(X_test)

# 模型的预测准确率
print(metrics.accuracy_score(y_test, pred))
# 模型评估报告
print(metrics.classification_report(y_test, pred))


# 绘制ROC曲线
# 计算流失用户的概率值，用于生成ROC曲线的数据
y_score = dt.predict_proba(X_test)[:,1]
fpr,tpr,threshold = metrics.roc_curve(y_test.map({'no':0,'yes':1}), y_score)
# 计算AUC的值
roc_auc = metrics.auc(fpr,tpr)

# 绘制面积图
plt.stackplot(fpr, tpr, color='steelblue', alpha = 0.5, edgecolor = 'black')
# 添加边际线
plt.plot(fpr, tpr, color='black', lw = 1)
# 添加对角线
plt.plot([0,1],[0,1], color = 'red', linestyle = '--')
# 添加文本信息
plt.text(0.5,0.3,'ROC curve (area = %0.3f)' % roc_auc)
# 添加x轴与y轴标签
plt.xlabel('1-Specificity')
plt.ylabel('Sensitivity')
# 显示图形
plt.show()


# 对训练数据集作平衡处理
over_samples = SMOTE(random_state=1234) 
over_samples_X,over_samples_y = over_samples.fit_sample(X_train, y_train)
# 重抽样前的类别比例
print(y_train.value_counts()/len(y_train))
# 重抽样后的类别比例
print(pd.Series(over_samples_y).value_counts()/len(over_samples_y))


# 基于平衡数据重新构建决策树模型
dt2 = tree.DecisionTreeClassifier()
dt2.fit(over_samples_X,over_samples_y)
# 模型在测试集上的预测
pred2 = dt2.predict(np.array(X_test))

# 模型的预测准确率
print(metrics.accuracy_score(y_test, pred2))
# 模型评估报告
print(metrics.classification_report(y_test, pred2))


# 计算流失用户的概率值，用于生成ROC曲线的数据
y_score = dt2.predict_proba(np.array(X_test))[:,1]
fpr,tpr,threshold = metrics.roc_curve(y_test.map({'no':0,'yes':1}), y_score)
# 计算AUC的值
roc_auc = metrics.auc(fpr,tpr)

# 绘制面积图
plt.stackplot(fpr, tpr, color='steelblue', alpha = 0.5, edgecolor = 'black')
# 添加边际线
plt.plot(fpr, tpr, color='black', lw = 1)
# 添加对角线
plt.plot([0,1],[0,1], color = 'red', linestyle = '--')
# 添加文本信息
plt.text(0.5,0.3,'ROC curve (area = %0.3f)' % roc_auc)
# 添加x轴与y轴标签
plt.xlabel('1-Specificity')
plt.ylabel('Sensitivity')
# 显示图形
plt.show()


