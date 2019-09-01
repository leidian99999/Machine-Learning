import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from impala.dbapi import connect
import warnings
from matplotlib.font_manager import FontProperties
chinese = FontProperties(fname = 'C:/Windows/Fonts/msyh.ttc')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
# %matplotlib inline
plt.style.use('ggplot') # 绘图风格
warnings.filterwarnings('ignore')
pd.set_option('max_colwidth',1000)

# 查询所有字段
def list_col(localhost,database, port,tabls_name):
    db = connect(localhost,port,database)
    cursor = db.cursor()
    cursor.execute("select * from %s" % tabls_name)
    col_name_list = [tuple[0] for tuple in cursor.description]
    db.close()
    return col_name_list

# 列出所有的表
def list_table(localhost,database,port):
    db = connect(localhost,database,port)
    cursor = db.cursor()
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    db.close()
    return table_list

# 每月用户购买商品数(订单数)
def month_order_products(df):
    plt.figure(figsize=(10, 6))
    ax= df.groupby('month').buy_num.sum().plot()
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("商品购买数", fontproperties=chinese)
    ax.set_title("各月用户购买商品数(订单数)", fontproperties=chinese)
    plt.show()

# 每月用户支付金额
def month_order_amount(df):
    ax = df.groupby('month').payable_rmb_amount.sum().plot()
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("实付金额", fontproperties=chinese)
    ax.set_title("各月用户支付金额", fontproperties=chinese)
    plt.show()

# 基于某特征分组的二特征散点图
def scatter_2features(df,groupby,feature1,feature2):
    ax= df.groupby(groupby) .sum().plot.scatter(feature1,feature2) # 数据维度转换为用户
    ax.set_xlabel("实付金额", fontproperties=chinese)
    ax.set_ylabel("购买商品数", fontproperties=chinese)
    ax.set_title("各用户实付金额与购买商品数关系", fontproperties=chinese)
    plt.show()

# 基于某特征分组的二特征直方图
def hist_2features(df,groupby,feature1,feature2):
    plt.figure(figsize=(16, 6))
    plt.subplot(121)
    ax = df.groupby(groupby)[feature1].sum().hist(bins=50)
    ax.set_xlabel("实付金额", fontproperties=chinese)
    ax.set_ylabel("用户数", fontproperties=chinese)
    ax.set_xlim(0, 150)
    ax.set_title("用户消费金额分布", fontproperties=chinese)
    plt.subplot(122)
    ax = df.groupby(groupby)[feature2].count().hist(bins=50)
    ax.set_xlabel('商品购买数', fontproperties=chinese)
    ax.set_ylabel("用户数", fontproperties=chinese)
    ax.set_xlim(0, 2000)
    ax.set_title("用户购买商品数分布", fontproperties=chinese)
    plt.show()

def FuGou(df_pivot):
    '''消费两次及以上的记为1，一次记为0，没有消费记为NaN'''
    df_FuGou_transf= df_pivot.applymap(lambda x: 1 if x > 1 else np.NaN if x == 0 else 0)
    # 计算复购率并作图
    ax = (df_FuGou_transf.sum() / df_FuGou_transf.count()).plot(figsize=(10, 4))
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("复购百分比", fontproperties=chinese)
    ax.set_title("各月复购率", fontproperties=chinese)
    plt.show()
def FuGou_compare(df_pivot):
    df_FuGou_transf = df_pivot.applymap(lambda x: 1 if x > 1 else np.NaN if x == 0 else 0)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df_FuGou_transf.count())
    ax.plot(df_FuGou_transf.sum())
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("购买人数", fontproperties=chinese)
    ax.set_title("各月二次消费与总消费用户数对比")
    legends = ["总消费人数", "多于二次消费人数"]
    ax.legend(legends, prop=chinese, loc='upper right')
    plt.show()

def purchase_return(data):
    '''
    #定义函数，每个月都要跟后面一个月对比下，
    #本月有消费且下月也有消费，则本月记为1，
    #本月有消费且下月没有消费，则本月记为0，
    #本月没有消费则为NaN，
    #由于最后个月没有下月数据，规定全为NaN
    '''
    status = []
    for i in range(6):
        if data[i] == 1:
            if data[i+1] == 1:
                status.append(1)
            if data[i+1] == 0:
                status.append(0)
        else:
            status.append(np.NaN)
    status.append(np.NaN)
    return pd.Series(status)

def HuiGou(df_pivot,df):
    '''购买过为1，没买为0'''
    df_HuiGou_transf = df_pivot.applymap(lambda x: 1 if x > 0 else 0)
    df_HuiGou_return = df_HuiGou_transf.apply(purchase_return, axis=1)
    columns = df.month.sort_values().unique()
    df_HuiGou_return.columns = columns
    ax = (df_HuiGou_return.sum() / df_HuiGou_return.count()).plot(figsize=(10, 4))
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("百分比", fontproperties=chinese)
    ax.set_title("各月回购率", fontproperties=chinese)
    plt.show()

def HuiGou_compare(df_pivot):
    df_HuiGou_return = df_pivot.apply(purchase_return, axis=1)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_HuiGou_return.count())  # 消费人数
    ax.plot(df_HuiGou_return.sum())  # 回购人数
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("用户数", fontproperties=chinese)
    legends = ["各月消费人数", "各月回购人数"]
    ax.legend(legends, prop=chinese, loc="upper right")
    plt.show()


def active_status(data):
    status = []
    for i in range(7):
        # 若本月没有消费
        if data[i] == 0:
            if len(status) > 0:
                if status[i - 1] == '未注册':
                    status.append('未注册')
                else:
                    status.append('不活跃')
            else:
                status.append('未注册')
        # 若本月有消费
        else:
            if len(status) == 0:
                status.append('新客')
            else:
                if status[i - 1] == '不活跃':
                    status.append('回流用户')
                elif status[i - 1] == '未注册':
                    status.append('新客')
                else:
                    status.append('活跃')
    return status

def user_active(df_pivot,df):
    df_FenCeng_transf = df_pivot.applymap(lambda x: 1 if x > 0 else 0)
    df_FenCeng_status = df_FenCeng_transf.apply(lambda x: pd.Series(active_status(x)), axis=1)
    columns = df.month.sort_values().unique()
    df_FenCeng_status.columns = columns
    # 统计每月各分类用户，未注册用户数不计数替换成NaN
    df_FenCeng_count = df_FenCeng_status.replace("未注册", np.NaN).apply(lambda x: pd.value_counts(x))
    ax = df_FenCeng_count.fillna(0).T.plot.area(figsize=(12, 6))
    ax.set_xlabel("月份", fontproperties=chinese)
    ax.set_ylabel("用户数", fontproperties=chinese)
    ax.set_title("各月各类用户占比", fontproperties=chinese)
    plt.show()

def return_user(df_pivot,df):
    df_FenCeng_transf = df_pivot.applymap(lambda x: 1 if x > 0 else 0)
    df_FenCeng_status = df_FenCeng_transf.apply(lambda x: pd.Series(active_status(x)), axis=1)
    columns = df.month.sort_values().unique()
    df_FenCeng_status.columns = columns
    # 统计每月各分类用户，未注册用户数不计数替换成NaN
    df_FenCeng_count = df_FenCeng_status.replace("未注册", np.NaN).apply(lambda x: pd.value_counts(x))
    # 回流占比：某个时间窗口内回流用户在总用户中的占比。
    return_rate = df_FenCeng_count.apply(lambda x: x / x.sum())
    print(return_rate)
    ax = return_rate.loc['回流用户'].plot(figsize=(12, 6))
    ax.set_xlabel('月份', fontproperties=chinese)
    ax.set_ylabel('占比', fontproperties=chinese)
    ax.set_title('每月回流用户占比', fontproperties=chinese)
    plt.show()

def active_user(df_pivot,df):
    df_FenCeng_transf = df_pivot.applymap(lambda x: 1 if x > 0 else 0)
    df_FenCeng_status = df_FenCeng_transf.apply(lambda x: pd.Series(active_status(x)), axis=1)
    columns = df.month.sort_values().unique()
    df_FenCeng_status.columns = columns
    df_FenCeng_count = df_FenCeng_status.replace("未注册", np.NaN).apply(lambda x: pd.value_counts(x))
    return_rate = df_FenCeng_count.apply(lambda x: x / x.sum())
    ax = return_rate.loc['活跃'].plot(figsize=(12, 6))
    ax.set_xlabel('月份', fontproperties=chinese)
    ax.set_ylabel('占比', fontproperties=chinese)
    ax.set_title('每月活跃用户占比', fontproperties=chinese)
    plt.show()

def user_amount(df,feature):
    '''
    计算累加值
    '''
    user_amount = df.groupby("user_id")[feature].sum().sort_values().reset_index()
    user_amount['amount_cumsum'] = user_amount[feature].cumsum()
    # 计算出各阶段金额占总金额的百分比
    amount_total = user_amount.amount_cumsum.max()
    user_amount['prop'] = user_amount.amount_cumsum.apply(lambda x: x / amount_total)
    ax = user_amount.prop.plot()
    ax.set_xlabel('人数（人）', fontproperties=chinese)
    ax.set_ylabel('百分数（%）', fontproperties=chinese)
    ax.set_title('用户累计贡献金额百分比', fontproperties=chinese)
    plt.show()

def life_time(df):
    order_date_min = df.groupby('user_id').create_date.min()
    order_date_min = pd.to_datetime(order_date_min)
    order_date_max = df.groupby('user_id').create_date.max()
    order_date_max = pd.to_datetime(order_date_max)
    life_time = (order_date_max - order_date_min).reset_index()
    life_time['life_time'] = life_time.create_date / np.timedelta64(1, 'D')
    print("二次消费以上用户数：")
    print(len(life_time[life_time.life_time > 0]))
    print("生命周期在200天以上的用户数")
    print(len(life_time[life_time.life_time > 150]))
    print("生命周期总用户数平均值")
    print(life_time[life_time.life_time > 0].life_time.mean())
    ax = life_time[life_time.life_time > 0].life_time.hist(bins=100, figsize=(12, 6))
    ax.set_xlabel('天数（天）', fontproperties=chinese)
    ax.set_ylabel('人数（人）', fontproperties=chinese)
    ax.set_title('二次消费以上用户的生命周期直方图', fontproperties=chinese)
    plt.show()

def retention(df):
    order_date_min = df.groupby('user_id').create_date.min()
    order_date_min = pd.to_datetime(order_date_min)
    user_purchase_retention = pd.merge(left=df, right=order_date_min.reset_index(), how='inner', on='user_id',
                                       suffixes=('', '_min'))
    user_purchase_retention["create_date"] = pd.to_datetime(user_purchase_retention["create_date"])
    user_purchase_retention[ 'order_date_diff'] = user_purchase_retention.create_date - user_purchase_retention.create_date_min
    user_purchase_retention['date_diff'] = user_purchase_retention.order_date_diff.apply(lambda x: x / np.timedelta64(1, 'D'))
    bin = [0, 30, 60, 90, 120, 150, 180]
    user_purchase_retention['date_diff_bin'] = pd.cut(user_purchase_retention.date_diff, bins=bin)
    pivoted_retention= user_purchase_retention.groupby(['user_id','date_diff_bin']).payable_rmb_amount.sum().unstack()
    pivoted_retention2= user_purchase_retention.groupby(['user_id','date_diff_bin']).buy_num.sum().unstack()
    pivoted_retention_trans = pivoted_retention.fillna(0).applymap(lambda x: 1 if x > 0 else 0)
    ax = (pivoted_retention_trans.sum() / pivoted_retention_trans.count()).plot.bar(figsize=(12, 6))
    ax.set_xlabel('时间跨度（天）', fontproperties=chinese)
    ax.set_ylabel('百分数（%）', fontproperties=chinese)
    ax.set_title('各时间段的用户留存率', fontproperties=chinese)
    plt.show()
    return user_purchase_retention


def diff(group):
    d = group.date_diff - group.date_diff.shift(-1)
    return d

def Buying_Cycle(df):
    last_diff = df.groupby('user_id').apply(diff)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = last_diff.hist(bins=20)
    ax.set_xlabel('时间跨度（天）', fontproperties=chinese)
    ax.set_ylabel('人数（人）', fontproperties=chinese)
    ax.set_title('用户平均购买周期直方图', fontproperties=chinese)
    plt.show()


if __name__ == "__main__":
    data = pd.read_csv("D:/GitHub/datasets/shop_order_190101_190731.csv")
    # print(data.describe())
    # print(data.info())
    '''数据描述'''
    # month_order_amount(data)    # 每月用户支付金额
    # month_order_products(data)  # 每月用户购买商品数(订单数)
    # scatter_2features(data,"user_id","payable_rmb_amount","buy_num") #查看销量和销售额的散点图
    # hist_2features(data,"user_id","payable_rmb_amount","buy_num")
    # print("用户首次消费月份(每月新客数)")
    # print(data.groupby("user_id").month.min().value_counts())
    # print("用户末次消费月份：(末次消费)")
    # print(data.groupby('user_id').month.max().value_counts())
    df_pivot = data.pivot_table(index='user_id', columns='month', values='date', aggfunc='count').fillna(0) # 主表
    '''复购率:当月购买2次及以上为复购用户'''
    # FuGou(df_pivot) # 复购率
    # FuGou_compare(df_pivot) # 各月二次消费人数与总消费人数对比
    '''回购率:某时间段内消费的用户，在下个时间周期内仍消费的占比。'''
    # HuiGou(df_pivot,data) # 回购率
    # HuiGou_compare(df_pivot) # 各月回购人数总总消费人数对比
    '''用户分层'''
    # user_active(df_pivot,data) # 用户分类
    # return_user(df_pivot,data) # 回流用户占比
    # active_user(df_pivot,data)
    '''用户质量：高质量用户贡献了多少消费额'''
    # user_amount(data,"payable_rmb_amount")
    '''用户生命周期:定义第一次消费到最后一次为整个生命周期'''
    # life_time(data) # 生命周期
    '''留存率：第一次消费后有多少比率进行第二次消费'''
    user_purchase_retention = retention(data)
    '''平均购买周期：用户两次购买之间的间隔'''
    Buying_Cycle(user_purchase_retention)

    # print(data.shape)
