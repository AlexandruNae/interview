'''
Here the code outputs 3 figures which represents the correlation between the occurence of various types of errors
 regarding every subfeature of feature1, feature2, feature3
'''

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig2, ax3 = plt.subplots()

path = Path(__file__).parent / 'data.csv'
data = pd.read_csv(path)


print(data.apply(lambda x: x.factorize()[0]).corr())
sns.heatmap(pd.crosstab(data.error, data.feature1), ax = ax1)
sns.heatmap(pd.crosstab(data.error, data.feature2), ax = ax2)
sns.heatmap(pd.crosstab(data.error, data.feature3), ax = ax3)
plt.show()