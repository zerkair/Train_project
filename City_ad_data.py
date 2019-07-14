import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import datetime

data = pd.read_csv(r'E:\TemporaryData\Railway\JiNan_commutation.csv',encoding = 'GB2312')
data_total = pd.read_csv(r'E:\TemporaryData\Railway\JiNan.csv',encoding = 'GB2312')
data.head()
data_total.head()

data['date'] = pd.to_datetime(data['date'])
data_total['date'] = pd.to_datetime(data_total['date'])
Zibo = data.loc[data['station_one'] == '淄博']
WeiFang = data.loc[data['station_one'] == '潍坊']
QingDao = data.loc[data['station_one'] == '青岛']

'''
week_day = []
def weekday_list(row_data):#显示对应日期的星期几
    week_day = []
    for i in row_data['date']:
        week_day.append(i.weekday())

    return week_day
'''

#判断日期time0是否在数据中
def time_in_S(time0, row_data):
    for i in row_data['date']:
        if time0 == i:
            return True

    return False


#判断是否包含从一个完整的星期，从星期I开始，抽出这些日子
def week_data(start, row_data):
    week_data_record = []
    #week_day = weekday_list(row_data)
    for i in row_data['date']:
        if i.weekday() == start - 1 and time_in_S(i + datetime.timedelta(days = 7), row_data):
            week_data_record.append(i)

    return week_data_record

week_data_record = week_data(start = 2, row_data = data_total)

#画出每星期的变化图
def show_weekly(start, row_data):
    data_chart = []
    week_data_record = week_data(start, row_data)
    for i in range(len(week_data_record)):
        data_chart.append(pd.DataFrame())
        data_chart[i] = row_data.loc[row_data['date'] == week_data_record[i]]
        for j in range(1,7):
            data_chart[i] = data_chart[i].append(row_data.loc[row_data['date'] == week_data_record[i] + datetime.timedelta(days = j)])
    
    print(data_chart)
    for t in data_chart:
        plt.plot((0,1,2,3,4,5,6),t['num_arrive'])

    plt.show()

show_weekly(start = 2, row_data = data_total)





import math
propotion = []
for (i,j) in zip(Zibo['num_one2two'],data_total['num_arrive']):
    propotion.append(math.log(int(j)) - math.log(int(i)))




plt.plot(Zibo['date'],propotion)
plt.show()

Zibo = data.loc[data['station_one'] == '淄博']
plt.plot(Zibo.loc[:,['num_one2two','num_two2one']])
plt.show()

#from datetime import datetime
#trans_time = [datetime.strptime(i,'%Y-%m-%d') for i in Zibo['date']]


plt.plot(Zibo['date'],Zibo['num_one2two'])
plt.plot(Zibo['date'],WeiFang['num_one2two'])
plt.plot(Zibo['date'],QingDao['num_one2two'])
plt.plot(Zibo['date'],Zibo['num_two2one'])
plt.plot(Zibo['date'],WeiFang['num_two2one'])
plt.plot(Zibo['date'],QingDao['num_two2one'])
plt.show()

#用weekday()来表示星期几


