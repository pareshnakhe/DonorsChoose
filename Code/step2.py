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
outputFile = open('Projects_clean.csv', 'w')

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


projects = pd.read_csv('Projects_clean.csv', names=headers, quotechar='"', skipinitialspace=True)
rel_para = ['Project ID', 'School ID', 'Project Cost', 'Project Subject Category Tree', 'Project Grade Level Category', 'Project Resource Category']
projects = projects.loc[:, rel_para]
projects = projects.dropna()


"""
Part 2: Read total_donation_trimmed.csv in donations DataFrame.
total_donation_trimmed.csv is a compact version of Donations,csv where rows correspond to
Project ID and total donation for the project.
"""

donations = pd.read_csv('total_donation_trimmed.csv', na_values=[' '])
donations = donations.loc[:, ['Project ID', 'Total Donation']]
# print donations.head()


schools = pd.read_csv('Schools.csv', na_values=[' '])
schools = schools.loc[:, ['School ID', 'School Metro Type', 'School Percentage Free Lunch', 'School State']]
schools = schools.dropna()
# print schools.head()


project_donations = pd.merge(projects, donations)
# print project_donations.head()
project_donations_schools = pd.merge(project_donations, schools)
# print project_donations_schools.head()
project_donations_schools.to_csv('project_donations_schools.csv')