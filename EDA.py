'''
1. Perform an EDA step

Here the code outputs the number of items produced every day in a new data frame

(for correlation see correlation.py)
(for algorithm see algorithm.py)
'''
import pandas as pd
from pathlib import Path
from dateutil import parser

path = Path(__file__).parent / 'data.csv'
data = pd.read_csv(path)

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