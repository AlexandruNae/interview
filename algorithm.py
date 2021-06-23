import operator
from pathlib import Path
import pandas as pd
from dateutil import parser

path = Path(__file__).parent / 'data.csv'
data = pd.read_csv(path)

pd.options.display.max_columns = None

class Item():
    def __init__(self, timestamp, id, error, time_delta=-1):
        self.timestamp = timestamp
        self.id = id
        self.error = error
        self.time_delta = time_delta


def density_function(error_name):
    objects = []
    time_delta_array=[]
    timeframe=[]
    count =0
    for index, row in data.iterrows():

        time=parser.parse(row['timestamp'])
        obj = Item(timestamp=time, id=str(row['item_id']), error=row['error'])
        if count == 0:
            time_start = obj.timestamp
            count = count+1
        if obj.error==error_name:
            obj.time_delta = obj.timestamp - time_start
            time_delta_array.append(obj.time_delta)
            objects.append(obj)

    n = len(time_delta_array)
    densities=[]
    hours_in_day = 24
    stop_i_increase_j = False
    for j in range(1, n-1):
        if not stop_i_increase_j:
            for i in range(0, j-1):

                # number of errors
                error_count = j - i

                #period of time between errors in hours
                time_delta = time_delta_array[j] - time_delta_array[i]
                time_delta = time_delta.days * hours_in_day + time_delta.seconds/360

                #density of error
                density = error_count / time_delta
                density = round(density, 6)
                densities.append(density)

                #timeframe of the density
                timeframe.append((time_delta_array[j]+time_start, time_delta_array[i]+time_start))
                if density < densities[len(densities)-1]:
                    stop_i_increase_j = True

        else:
            # number of errors
            error_count = j - i

            # period of time between errors in hours
            time_delta = time_delta_array[j] - time_delta_array[i]
            time_delta = time_delta.days * hours_in_day + time_delta.seconds / 360

            # density of error
            density = error_count / time_delta
            density = round(density, 6)
            densities.append(density)

            # timeframe of the density
            timeframe.append((time_delta_array[j] + time_start, time_delta_array[i] + time_start))

            if density < densities[len(densities)-1]:
                j = j - 1
                stop_i_increase_j = False
    print(len(densities))
    return dict(zip(timeframe, densities)) #densities, timeframe

def sort_the_dict(dictionar):
    return dict(sorted(dictionar.items(), key=operator.itemgetter(1), reverse=True))

def print_the_dict(dict_sorted):
    for x in dict_sorted.keys():
        x1 = str(x[0])
        x2 = str(x[1])
        print('from: ', x2, ' to: ', x1, ' -> density(no_err/time): ', dict_sorted[x])

def dict_to_dataframe(dict_sorted):
    date_from = []
    date_to = []
    density = []
    for k, v in dict_sorted.items():
        date_from.append(str(k[0]))
        date_to.append(str(k[1]))
        density.append(v)
    dict = {'From:': date_from, 'To:': date_to,'Density (no_errors/hours):':density  }
    return pd.DataFrame(dict)

dictionar = density_function('E')

dict_sorted = sort_the_dict(dictionar)

print(dict_to_dataframe(dict_sorted).head())

# print_the_dict(dict_sorted)


# lst = sorted(lst, key=float)
# print(lst[::-1])
# print(len(lst))






