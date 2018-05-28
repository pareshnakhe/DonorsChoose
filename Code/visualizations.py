import pandas as pd
import numpy as np
import matplotlib
from collections import OrderedDict
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

### Part 1

data = pd.read_csv('project_donations_schools.csv', index_col=0)


State_list = data.loc[:, 'School State'].unique()
rsrc_catg_list = data.loc[:, 'Project Resource Category'].unique()


proj_dict = {}
rsrc_dict = {}
for state in State_list:
    proj_dict[state] = data.loc[data['School State'] == state, :].shape[0]

for rsrc in rsrc_catg_list:
    rsrc_dict[rsrc] = data.loc[data['Project Resource Category'] == rsrc, :].shape[0]

# https://docs.python.org/2/library/collections.html#collections.OrderedDict
ordered_proj_dict = OrderedDict(sorted(proj_dict.items(), key= lambda t: t[1], reverse=True))
ordered_rsrc_dict = OrderedDict(sorted(rsrc_dict.items(), key= lambda t: t[1], reverse=True))

# For plotting top 10 states in terms of number of projects
state_list = list()
num_proj_list = list()

for key, value in ordered_proj_dict.items():
    state_list.append(key)
    num_proj_list.append(value)

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
x = np.arange(10)
plt.bar(x, num_proj_list[:10], 0.5, fc='tab:purple')
plt.xticks(x, state_list[:10])
plt.ylabel('Num of Projects')
plt.title('Top 10 States in terms of Number of Projects')
plt.show()

# Project Resource Category

rsrc_list = list()
num_proj_list = list()

for key, value in ordered_rsrc_dict.items():
    rsrc_list.append(key)
    num_proj_list.append(value)

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
x = np.arange(7)
plt.bar(x, num_proj_list[:7], 0.5, fc='tab:purple')
plt.xticks(x, rsrc_list[:7])
plt.ylabel('Num of Projects')
plt.title('Distribution of Projects in terms of Resources Needed')
plt.show()

############## Donor - Donation #######
## Part 2

donors = pd.read_csv('Donors.csv', na_values='')
donors.dropna(how='any')
donors = donors.loc[:, ['Donor ID', 'Donor State']]
# print donors.head()

donations = pd.read_csv('Donations.csv')
donations.dropna(how='any')
donations = donations.loc[:, ['Donation ID', 'Donor ID', 'Donation Amount']]
# print donations.head()

donor_donations = pd.merge(donors, donations)

# donor_donations.to_csv('donor_donations.csv')
# donor_donations = pd.read_csv('donor_donations.csv', na_values='')


data = donor_donations.loc[:, ['Donor State', 'Donation Amount']]
State_list = data.loc[:, 'Donor State'].unique()
donor_dict = {}
for state in State_list:
    donor_dict[state] = data.loc[data['Donor State'] == state, 'Donation Amount'].values
    donor_dict[state] = [x for x in donor_dict[state] if str(x) != 'nan' and x <= 160.0]

# Plot Stacked Histogram
n_bins = 30
x = (np.array(donor_dict['Florida']), np.array(donor_dict['Texas']), np.array(donor_dict['New York']))

plt.hist(x, n_bins, normed=1, histtype='bar', stacked=True, label=['Florida', 'Texas', 'New York'])
plt.xlabel('Amount donated')
plt.title('Stacked Histogram: Donation Amounts')
plt.legend()
plt.show()