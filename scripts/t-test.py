'''
t-test.py

Script to calculate statistical significance using independent 
t-test on sample groups split by the median MCDI and age score

AUTHOR: JASMINE FALK
'''

import os
import csv 
import sys
import statistics
from scipy import stats
import pandas as pd

# get name of data file
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_dir = master_dir + '/Anaphora/data/data_analysis/'

# process command line args
if len(sys.argv) != 2:
    print('Incorrect number of arguments.')
    exit(1)

if sys.argv[1] == 'mcdi':
    below_med_file = data_dir + 'below_med_MCDI.csv'
    above_med_file = data_dir + 'above_med_MCDI.csv'
    output_file = data_dir + 'MCDI_split_comparison.csv'
elif sys.argv[1] == 'age':
    below_med_file = data_dir + 'below_med_age.csv'
    above_med_file = data_dir + 'above_med_age.csv'
    output_file = data_dir + 'age_split_comparison.csv'

# data for below median MCDI group
df_below = pd.read_csv(below_med_file, index_col=0)

# parent speech stats
anaphora_rate_below = df_below['anaphora utterance rate']
child_driven_below = df_below['child-driven prop']
viz_cue_below = df_below['visual cue prop']
speech_rate_below = df_below['parent speech rate']
anaphora_ratio_below = df_below['anaphora use ratio']

# child resolution accuracy stats
overall_accuracy_below = df_below['overall accuracy']
one_accuracy_below = df_below['one accuracy']
split_accuracy_below = df_below['split accuracy']
pronoun_accuracy_below = df_below['pronoun accuracy']
verbal_accuracy_below = df_below['verbal cue accuracy']
visual_accuracy_below = df_below['extra cue accuracy']
parent_driven_accuracy_below = df_below['parent instigated accuracy']

# data for above median MCDI group
df_above = pd.read_csv(above_med_file, index_col=0)

# parent speech stats
anaphora_rate_above = df_above['anaphora utterance rate']
child_driven_above = df_above['child-driven prop']
viz_cue_above = df_above['visual cue prop']
speech_rate_above = df_above['parent speech rate']
anaphora_ratio_above = df_above['anaphora use ratio']

# child resolution accuracy stats
overall_accuracy_above = df_above['overall accuracy']
one_accuracy_above = df_above['one accuracy']
split_accuracy_above = df_above['split accuracy']
pronoun_accuracy_above = df_above['pronoun accuracy']
verbal_accuracy_above = df_above['verbal cue accuracy']
visual_accuracy_above = df_above['extra cue accuracy']
parent_driven_accuracy_above = df_above['parent instigated accuracy']

def build_row(metric_name, below_med, above_med):
    '''
    "The Levene test tests the null hypothesis that 
    all input samples are from populations with equal variances.

    returns: F-statistic and a significance value (p-value)
        - p > .05: can assume equal variance
        - p < .05: cannot assume equal variance
    '''
    f, p_levene = stats.levene(below_med, above_med)
    # print(f,p_levene)
    # exit(1)
    if p_levene > .05:
        # can assume equal variance (equal_var=True)
        t, p_t = stats.ttest_ind(below_med, above_med, equal_var=True)
    else:
        # cannot assume equal variance (equal_var=False)
        t, p_t = stats.ttest_ind(below_med, above_med, equal_var=False)

    return [metric_name, str(f), str(p_levene), str(t), str(p_t)]

header = [ '', "Levene's test", '', 't-test' ]
subheader = [ '', 'F', 'p', 't', 'p' ]

# write to output file
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerow(subheader)

    writer.writerow(build_row('parent speech rate', speech_rate_below, speech_rate_above))
    writer.writerow(build_row('anaphora utterance rate', anaphora_rate_below, anaphora_rate_above))
    writer.writerow(build_row('anaphora use ratio', anaphora_ratio_below, anaphora_ratio_above))
    writer.writerow(build_row('child-driven prop', child_driven_below, child_driven_above))
    writer.writerow(build_row('visual cue prop', viz_cue_below, viz_cue_above))

    writer.writerow(build_row('overall accuracy', overall_accuracy_below, overall_accuracy_above))
    writer.writerow(build_row('one accuracy', one_accuracy_below, one_accuracy_above))
    writer.writerow(build_row('split accuracy', split_accuracy_below, split_accuracy_above))
    writer.writerow(build_row('pronoun accuracy', pronoun_accuracy_below, pronoun_accuracy_above))
    writer.writerow(build_row('verbal cue accuracy', verbal_accuracy_below, verbal_accuracy_above))
    writer.writerow(build_row('visual cue accuracy', visual_accuracy_below, visual_accuracy_above))
    writer.writerow(build_row('parent instigated accuracy', parent_driven_accuracy_below, parent_driven_accuracy_above))