import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

data = pd.read_csv('project_donations_schools.csv', index_col=0)

temp_percent_full = data.loc[:, ['Total Donation']].values / data.loc[:, ['Project Cost']].values
data = data.assign(percent_full=temp_percent_full)

"""
There are 36615 projects which got more money than their costs.
Since I am using a logistic regression model, I am resetting the
values in column 'percent_full' to 1.0 if they are greater than 1.0
"""
# print data[data['percent_full'] > 1.0].count()
# print max(data['percent_full']), min(data['percent_full'])

data.loc[data['percent_full'] > 1.0, 'percent_full'] = 1.0
# print data[data['percent_full'] > 1.0].count()
print max(data['percent_full']), min(data['percent_full'])
data = data.drop(columns=['Project ID', 'School ID', 'Project Cost', 'Total Donation'])

data = pd.get_dummies(data)
print len(data.columns.values)
# exit(1)

# divide the 'percent_full' values into buckets so that it is categorical data.
# I am doing this to use logistic regression out-of-the-box
# data.loc[:, 'percent_full'] = pd.cut(data.loc[:, 'percent_full'].values, 2, labels=range(2))
# print data.head()

data.loc[data['percent_full'] > 0.250, 'percent_full'] = 1
data.loc[data['percent_full'] <= 0.250, 'percent_full'] = 0

data.to_csv('clean_classfn_data.csv')


X = data.drop(['percent_full'], axis=1)
y = data['percent_full']

print len(y.values)
for C in np.arange(1.0, 100.0, 20.0):
    clf = LogisticRegression(C=C, penalty='l1', tol=0.01).fit(X, y)
    print("training score : %.3f" % (clf.score(X, y)))
