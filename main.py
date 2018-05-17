import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Alternative but perhaps a less ef
# with open('sample.csv') as f_input:
#     filedata = f_input.read()
#
# filedata = filedata.replace('""', '').strip()
#
# with open('sample1.csv', 'w') as outputFile:
#     outputFile.write(filedata)
########################################################################


"""
Part 1: Read Projects.csv in required format in projects DataFrame.
This step needs "cleaning on account of the unstructured quotations in the original file
"""

# Snippet to get csv data in dataFrame in correct format
inputFile = open('Projects.csv', 'r')
outputFile = open('sample1.csv', 'w')

i = 0
for line in inputFile:
    if line != '\n':
        line = line.rstrip()
        if i == 0:
            headers = line.split(',')
            i += 1
        else:
            outputFile.write(line.replace('""', '').strip())
            outputFile.write('\n')

inputFile.close()
outputFile.close()


projects = pd.read_csv('sample1.csv', names=headers, quotechar='"', skipinitialspace=True)
rel_para = ['Project ID', 'Project Cost', 'Project Subject Category Tree', 'Project Grade Level Category', 'Project Resource Category']
projects = projects.loc[:, rel_para]
projects = projects.dropna()

# projects.loc[:, ['Project Subject Category Tree']] = str(projects.loc[:, ['Project Subject Category Tree']].values).replace('"', '')
# print projects.loc[:, ['Project Subject Category Tree']]
# exit(1)
# projects.loc[:, ['Project Subject Category Tree']] = projects.loc[:, ['Project Subject Category Tree']].str.replace('"', '')

# # print projects['Project Cost'].describe()
# #
# # plt.hist(np.log(projects['Project Cost']), color='blue')
# # plt.show()

"""
Part 2: Read total_donation_trimmed.csv in donations DataFrame.
total_donation_trimmed.csv is a compact version of Donations,csv where rows correspond to
Project ID and total donation for the project.
"""

donations = pd.read_csv('total_donation_trimmed.csv', na_values=[' '])
donations = donations.loc[:, ['Project ID', 'Total Donation']]
print donations.head()

# Interesting representation of the distribution of total donations
# (for better representation limited to max donation of 1000)
# plt.hist(donations[donations['Total Donation'] < 1000]['Total Donation'], bins=200, color='blue')
# plt.show()


#print donations.index.values, donations.columns.values
# Write redundantly for readability
# donations = donations.loc[:, ['Project ID', 'Donation ID', 'Donation Amount']]
# donations = donations.dropna()
# print donations

project_donations = pd.merge(projects, donations)
print project_donations.head()
project_donations.to_csv('project_donations.csv')