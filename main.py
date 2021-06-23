import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime
from dateutil import parser

data = pd.read_csv("/home/alex/PycharmProjects/interview/data.csv")

# print(data.shape)
print(data.head())
# print(data.columns)
# print(data.nunique(axis=0))
# print(pd.to_datetime(data))

timestamp_datetime=[]

n=0

days=[]
count_items_per_day=[]

switch=True
for index in data.index:
    if data['timestamp'][index][:10] not in days:
        days.append(data['timestamp'][index][:10])
        if switch==False:
            break
        count_day = 1
        # print('in if')
    else:
        # print('in else')
        switch=False
        count_day=count_day+1

days.clear()
for index in data.index:
    if data['timestamp'][index][:10] not in days:
        count_items_per_day.append(count_day)
        days.append(data['timestamp'][index][:10])
        # print('in if')
        switch=True
        count_day=1
    else:
        # print('in else')
        count_day=count_day+1

    # print(count_day)
    timestamp_datetime.append(parser.parse(data['timestamp'][index][:10]))

no_items_per_day_dict= zip(days,count_items_per_day)

new_df = pd.DataFrame(no_items_per_day_dict)
print(new_df)






