import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

"""
This module transforms Donations data to a file with (Project ID, total_donation) format.
his transformation is written to 'total_donation_trimmed.csv'
"""


donations = pd.read_csv('Donations.csv', na_values=[' '])
# some donation amounts are missing. Using default interpolate() method
donations['Donation Amount'] = donations['Donation Amount'].interpolate()
donations = donations.loc[:, ['Project ID', 'Donation Amount']]

# https://pandas.pydata.org/pandas-docs/stable/groupby.html
grouped = donations.groupby('Project ID')
total_donation = grouped['Donation Amount'].sum()

# print total_donation.index.values, len(total_donation.index.values)
# print len(total_donation.tolist())

# Creating a new DataFrame (Note: total_donation is in Series data structure)
dict = {'Project ID': total_donation.index.values, 'Total Donation': total_donation.tolist()}
df = pd.DataFrame(data=dict)
df.to_csv('total_donation_trimmed.csv')