'''
age_correlations-EXTRA.py

Script to determine if correlations compared to
age are statistically significant for extra variables

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
AGE                      = 1
PERCENT_PARENT_INST      = 10
PERCENT_CHILD_INST       = 11
PERCENT_EXTRA_CUE        = 12
PERCENT_NONREQ_EXTRA_CUE = 14
PERCENT_REQ_EXTRA_CUE    = 15
PARENT_INST_SCORE        = 24
EXTRA_CUE_SCORE          = 25

# header line for output file
header = [ 'covariate', 'pearson r', 'p-value' ]

# get name of data files
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/avg_correct_child-EXTRA.csv'

# output filename
output_file = master_dir + '/Anaphora/data/data_analysis/correlation_sig/age_correlations-EXTRA.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=str, skiprows=1)

age                      = data.T[AGE].astype(np.float)
percent_parent_inst      = data.T[PERCENT_PARENT_INST].astype(np.float)
percent_child_inst       = data.T[PERCENT_CHILD_INST].astype(np.float)
percent_extra_cue        = data.T[PERCENT_EXTRA_CUE].astype(np.float)
percent_nonreq_extra_cue = data.T[PERCENT_NONREQ_EXTRA_CUE].astype(np.float)
percent_req_extra_cue    = data.T[PERCENT_REQ_EXTRA_CUE].astype(np.float)
parent_inst_score        = data.T[PARENT_INST_SCORE].astype(np.float)
extra_cue_score          = data.T[EXTRA_CUE_SCORE].astype(np.float)

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
output_data['percent parent instigated'] = stats.pearsonr(percent_parent_inst, age)
output_data['percent child instigated'] = stats.pearsonr(percent_child_inst, age)
output_data['percent extra cues'] = stats.pearsonr(percent_extra_cue, age)
output_data['percent nonreq extra cues'] = stats.pearsonr(percent_nonreq_extra_cue, age)
output_data['percent req extra cues'] = stats.pearsonr(percent_req_extra_cue, age)
output_data['parent instigated accuracy'] = stats.pearsonr(parent_inst_score, age)
output_data['extra cue accuracy'] = stats.pearsonr(extra_cue_score, age)

# write to csv file
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for key, data in output_data.items():
        writer.writerow([key, data[0], data[1]])