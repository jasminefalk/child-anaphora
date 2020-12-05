'''
mcdi_correlations.py

Script to determine if correlations compared to
age are statistically significant

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
AGE              = 1
PERCENT_ANAPHORA = 6
PERCENT_ONE      = 7
PERCENT_SPLIT    = 8
PERCENT_VERBAL   = 10
PERCENT_VISUAL   = 11
TOTAL_ACCURACY   = 12
PRONOUN_ACCURACY = 15
VERBAL_ACCURACY  = 16
VISUAL_ACCURACY  = 17

# header line for output file
header = [ 'covariate', 'pearson r', 'p-value' ]

# get name of data files
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/avg_correct_child-EDITED.csv'

# output filename
output_file = master_dir + '/Anaphora/data/data_analysis/correlation_sig/age_correlations.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=str, skiprows=1)

age              = data.T[AGE].astype(np.float)
percent_anaphora = data.T[PERCENT_ANAPHORA].astype(np.float)
percent_one      = data.T[PERCENT_ONE].astype(np.float)
percent_split    = data.T[PERCENT_SPLIT].astype(np.float)
percent_verbal   = data.T[PERCENT_VERBAL].astype(np.float)
percent_visual   = data.T[PERCENT_VISUAL].astype(np.float)
total_accuracy   = data.T[TOTAL_ACCURACY].astype(np.float)
pronoun_accuracy = data.T[PRONOUN_ACCURACY].astype(np.float)
verbal_accuracy  = data.T[VERBAL_ACCURACY].astype(np.float)
visual_accuracy  = data.T[VISUAL_ACCURACY].astype(np.float)

'''
Notes on Pearson's r: scipy.stats.pearsonr returns (r value, p-value)
r:       measures the linear relationship between two datasets with [-1, +1],
         0 indicating no correlation, -1 or +1 indiciating exact linear 
         relationships
p-value: indicates the probability of an uncorrelated system producing datasets
         that have a Pearson correlation at least as extreme as the one 
         computed from these datasets
'''

output_data = {}
output_data['percent anaphora'] = stats.pearsonr(percent_anaphora, age)
output_data['percent split'] = stats.pearsonr(percent_split, age)
output_data['percent one'] = stats.pearsonr(percent_one, age)
output_data['percent verbal'] = stats.pearsonr(percent_verbal, age)
output_data['percent visual'] = stats.pearsonr(percent_visual, age)
output_data['overall accuracy'] = stats.pearsonr(total_accuracy, age)
output_data['pronoun accuracy'] = stats.pearsonr(pronoun_accuracy, age)
output_data['verbal accuracy'] = stats.pearsonr(verbal_accuracy, age)
output_data['visual accuracy'] = stats.pearsonr(visual_accuracy, age)

# write to csv file
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for key, data in output_data.items():
        writer.writerow([key, data[0], data[1]])