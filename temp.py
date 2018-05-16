import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


data = pd.read_csv('project_donations.csv', index_col=0)

temp_percent_full = data.loc[:, ['Total Donation']].values / data.loc[:, ['Project Cost']].values
data = data.assign(percent_full=temp_percent_full)
data = data.drop(columns=['Project ID', 'Project Cost', 'Total Donation'])

print data.head()