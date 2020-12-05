'''
mcdi_correlations.py

Script to determine if correlations compared to 
MCDI scores are statistically significant

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
AGE              = 1
MCDI_TOTAL       = 2
MCDI_NOUN        = 3
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
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/child_stats_mcdi_removed.csv'

# output filename
mcdiTotal_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiTotal_correlations.csv'
mcdiNoun_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiNoun_correlations.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=float, skiprows=1)

age              = data.T[AGE]
mcdi_total       = data.T[MCDI_TOTAL]
mcdi_noun        = data.T[MCDI_NOUN]
percent_anaphora = data.T[PERCENT_ANAPHORA]
percent_one      = data.T[PERCENT_ONE]
percent_split    = data.T[PERCENT_SPLIT]
percent_verbal   = data.T[PERCENT_VERBAL]
percent_visual   = data.T[PERCENT_VISUAL]
total_accuracy   = data.T[TOTAL_ACCURACY]
pronoun_accuracy = data.T[PRONOUN_ACCURACY]
verbal_accuracy  = data.T[VERBAL_ACCURACY]
visual_accuracy  = data.T[VISUAL_ACCURACY]

'''
Notes on Pearson's r: scipy.stats.pearsonr returns (r value, p-value)
r:       measures the linear relationship between two datasets with [-1, +1],
         0 indicating no correlation, -1 or +1 indiciating exact linear 
         relationships
p-value: indicates the probability of an uncorrelated system producing datasets
         that have a Pearson correlation at least as extreme as the one 
         computed from these datasets
'''

total_output = {}
total_output['age'] = stats.pearsonr(age, mcdi_total)
total_output['percent anaphora'] = stats.pearsonr(percent_anaphora, mcdi_total)
total_output['percent split'] = stats.pearsonr(percent_split, mcdi_total)
total_output['percent one'] = stats.pearsonr(percent_one, mcdi_total)
total_output['percent verbal'] = stats.pearsonr(percent_verbal, mcdi_total)
total_output['percent visual'] = stats.pearsonr(percent_visual, mcdi_total)
total_output['overall accuracy'] = stats.pearsonr(total_accuracy, mcdi_total)
total_output['pronoun accuracy'] = stats.pearsonr(pronoun_accuracy, mcdi_total)
total_output['verbal accuracy'] = stats.pearsonr(verbal_accuracy, mcdi_total)
total_output['visual accuracy'] = stats.pearsonr(visual_accuracy, mcdi_total)

noun_output = {}
noun_output['age'] = stats.pearsonr(age, mcdi_noun)
noun_output['percent anaphora'] = stats.pearsonr(percent_anaphora, mcdi_noun)
noun_output['percent split'] = stats.pearsonr(percent_split, mcdi_noun)
noun_output['percent one'] = stats.pearsonr(percent_one, mcdi_noun)
noun_output['percent verbal'] = stats.pearsonr(percent_verbal, mcdi_noun)
noun_output['percent visual'] = stats.pearsonr(percent_visual, mcdi_noun)
noun_output['overall accuracy'] = stats.pearsonr(total_accuracy, mcdi_noun)
noun_output['pronoun accuracy'] = stats.pearsonr(pronoun_accuracy, mcdi_noun)
noun_output['verbal accuracy'] = stats.pearsonr(verbal_accuracy, mcdi_noun)
noun_output['visual accuracy'] = stats.pearsonr(visual_accuracy, mcdi_noun)

# write to csv files
with open(mcdiTotal_output, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for key, data in total_output.items():
        writer.writerow([key, data[0], data[1]])

with open(mcdiNoun_output, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for key, data in noun_output.items():
        writer.writerow([key, data[0], data[1]])