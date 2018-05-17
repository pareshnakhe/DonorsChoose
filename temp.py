import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

data = pd.read_csv('project_donations.csv', index_col=0)

temp_percent_full = data.loc[:, ['Total Donation']].values / data.loc[:, ['Project Cost']].values
data = data.assign(percent_full=temp_percent_full)

"""
There are 36615 projects which got more money than the their costs.
Since I am using a logistic regression model, I am resetting the
values in column 'percent_full' to 1.0 if they are greater than 1.0
"""
# print data[data['percent_full'] > 1.0].count()
# print max(data['percent_full']), min(data['percent_full'])

data.loc[data['percent_full'] > 1.0, 'percent_full'] = 1.0
# print data[data['percent_full'] > 1.0].count()
print max(data['percent_full']), min(data['percent_full'])

# This is interesting: there is a spike at 0.5 and 1.0
# i.e. there are a lot of projects which are close to 50% and 100% full.
# plt.hist(data['percent_full'], bins=100, color='blue')
# plt.show()
data = data.drop(columns=['Project ID', 'Project Cost', 'Total Donation'])

data = pd.get_dummies(data)
# print data.columns.values

# divide the 'percent_full' values into buckets so that it is categorical data.
# I am doing this to use logistic regression out-of-the-box
data.loc[:, 'percent_full'] = pd.cut(data.loc[:, 'percent_full'].values, 10, labels=range(10))
# print data.head()


X = data.drop(['percent_full'], axis=1)
y = data['percent_full']

print 'start'
clf = LogisticRegression(solver='sag', max_iter=100, random_state=42,
                             multi_class='multinomial', n_jobs=3).fit(X, y)

print("training score : %.3f" % (clf.score(X, y)))
