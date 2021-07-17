# encoding: utf-8
from jqdatasdk import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

auth('18483692910','Hu19950615')
count=get_query_count()
print("初始化登录 今日可查询:"+ str(count['spare']))
#
# finance.run_query(
#     query(
#         finance.FUT_MEMBER_POSITION_RANK).
#         filter(finance.FUT_MEMBER_POSITION_RANK.code==code).limit(n))

#查询qihuo最新一个交易日的持仓量龙虎榜数据
q=query(
finance.FUT_MEMBER_POSITION_RANK.day,
        finance.FUT_MEMBER_POSITION_RANK.rank_type,
        finance.FUT_MEMBER_POSITION_RANK.rank,
        finance.FUT_MEMBER_POSITION_RANK.member_name,
finance.FUT_MEMBER_POSITION_RANK.indicator_increase,
finance.FUT_MEMBER_POSITION_RANK.indicator,).filter(finance.FUT_MEMBER_POSITION_RANK.code=='UR2109.XZCE',
                                                    finance.FUT_MEMBER_POSITION_RANK.rank_type_ID==501001).order_by\
    (finance.FUT_MEMBER_POSITION_RANK.day.desc()).limit(20)
print(finance.FUT_MEMBER_POSITION_RANK.day.desc('2021-7-14'))

df=finance.run_query(q)
df2=pd.DataFrame(df.sort_values(by="rank",ascending=True))
df2=df2.sort_values(by="rank",ascending=True).iloc[::-1]#排序
df2.reset_index(inplace = True)#刷新票签

#设置
y=np.array(list(df2.index))
x=np.array(list(df2['indicator']))
xticks1=list(df2.index)

df2.plot(kind='barh',x='member_name',y="indicator")



for a,b in zip(x,y):
 plt.text(a+60, b-0.5, '%.0f' % a, ha='center', va= 'bottom',fontsize=7)

plt.title("尿素龙虎榜")
plt.xlabel("成交量")
plt.ylabel("席位")
plt.legend(['多单成交'])
plt.show()

#交易日
#print(get_trade_days(start_date='2021-5-1', end_date='2021-7-14'))

print(df2)




