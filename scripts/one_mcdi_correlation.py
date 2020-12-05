'''
one_mcdi_correlation.py

Script to determine if correlations of one accuracy scores 
compared to MCDI scores are statistically significant

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
MCDI_TOTAL = 1
MCDI_NOUN  = 2
ACCURACY   = 3

# get name of data file
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/one_mcdi_accuracy.csv'

# output filenames (should already exist)
mcdiTotal_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiTotal_correlations.csv'
mcdiNoun_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiNoun_correlations.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=float, skiprows=1)

mcdi_total = data.T[MCDI_TOTAL]
mcdi_noun  = data.T[MCDI_NOUN]
accuracy   = data.T[ACCURACY]

total_output = {}
total_output['one accuracy'] = stats.pearsonr(accuracy, mcdi_total)

noun_output  = {}
noun_output['one accuracy'] = stats.pearsonr(accuracy, mcdi_noun)

# append to existing csv files
with open(mcdiTotal_output, 'a') as csvfile:
    writer = csv.writer(csvfile)
    for key, data in total_output.items():
        writer.writerow([key, data[0], data[1]])

with open(mcdiNoun_output, 'a') as csvfile:
    writer = csv.writer(csvfile)
    for key, data in noun_output.items():
        writer.writerow([key, data[0], data[1]])