'''
mcdi_correlations-EXTRA.py

Script to determine if correlations compared to 
MCDI scores are statistically significant for extra variables

AUTHOR: JASMINE FALK
'''
import os
import csv
import numpy as np
from scipy import stats

# column numbers
MCDI_TOTAL               = 2
MCDI_NOUN                = 3
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
data_file = master_dir + '/Anaphora/data/data_analysis/processed_data/child_stats_mcdi_removed-EXTRA.csv'

# output filename
mcdiTotal_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiTotal_correlations-EXTRA.csv'
mcdiNoun_output = master_dir + '/Anaphora/data/data_analysis/correlation_sig/mcdiNoun_correlations-EXTRA.csv'

data = np.loadtxt(data_file, delimiter=',', dtype=float, skiprows=1)

mcdi_total               = data.T[MCDI_TOTAL]
mcdi_noun                = data.T[MCDI_NOUN]
percent_parent_inst      = data.T[PERCENT_PARENT_INST]
percent_child_inst       = data.T[PERCENT_CHILD_INST]
percent_extra_cue        = data.T[PERCENT_EXTRA_CUE]
percent_nonreq_extra_cue = data.T[PERCENT_NONREQ_EXTRA_CUE]
percent_req_extra_cue    = data.T[PERCENT_REQ_EXTRA_CUE]
parent_inst_score        = data.T[PARENT_INST_SCORE]
extra_cue_score          = data.T[EXTRA_CUE_SCORE]

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
total_output['percent parent instigated'] = stats.pearsonr(percent_parent_inst, mcdi_total)
total_output['percent child instigated'] = stats.pearsonr(percent_child_inst, mcdi_total)
total_output['percent extra cues'] = stats.pearsonr(percent_extra_cue, mcdi_total)
total_output['percent nonreq extra cues'] = stats.pearsonr(percent_nonreq_extra_cue, mcdi_total)
total_output['percent req extra cues'] = stats.pearsonr(percent_req_extra_cue, mcdi_total)
total_output['parent instigated accuracy'] = stats.pearsonr(parent_inst_score, mcdi_total)
total_output['extra cue accuracy'] = stats.pearsonr(extra_cue_score, mcdi_total)

noun_output = {}
noun_output['percent parent instigated'] = stats.pearsonr(percent_parent_inst, mcdi_noun)
noun_output['percent child instigated'] = stats.pearsonr(percent_child_inst, mcdi_noun)
noun_output['percent extra cues'] = stats.pearsonr(percent_extra_cue, mcdi_noun)
noun_output['percent nonreq extra cues'] = stats.pearsonr(percent_nonreq_extra_cue, mcdi_noun)
noun_output['percent req extra cues'] = stats.pearsonr(percent_req_extra_cue, mcdi_noun)
noun_output['parent instigated accuracy'] = stats.pearsonr(parent_inst_score, mcdi_noun)
noun_output['extra cue accuracy'] = stats.pearsonr(extra_cue_score, mcdi_noun)

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