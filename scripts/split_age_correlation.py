'''
one_age_correlation.py

Script to determine if correlation of one accuracy scores 
compared to age is statistically significant

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
AGE      = 1
ACCURACY = 2

# get name of data file
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/split_age_accuracy.csv'

# output filenames (should already exist)
output_file = master_dir + '/Anaphora/data/data_analysis/correlation_sig/age_correlations.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=float, skiprows=1)
age = data.T[AGE]
accuracy = data.T[ACCURACY]

output_data = {}
output_data['split accuracy'] = stats.pearsonr(accuracy, age)

# append to existing csv files
with open(output_file, 'a') as csvfile:
    writer = csv.writer(csvfile)
    for key, data in output_data.items():
        writer.writerow([key, data[0], data[1]])
