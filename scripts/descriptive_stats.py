'''
descriptive_stats.py

Script to compile descriptive statistics for the following metrics:
    1) Parent speech rate (# of utterances per min)
    2) Anaphora use rate (# of anaphora utterance per min)
    3) Anaphora use ratio (2 / 1)
    4) Prop of anaphor utterances that are child driven
    5) Prop of anaphor utterances with a visual cue
Mean, stdev, range for each metric

AUTHOR: JASMINE FALK
'''
import os
import csv 
import sys
import statistics

# COLUMN NUMBERS FOR BASIC_STATS
TOTAL_UTTERANCES = 1
NUM_ANAPHORA = 2
TOTAL_TIME = 5

# COLUMN NUMBERS FOR EXTRA_VARS
CHILD_DRIVEN_PROP = 11
VISUAL_CUE_PROP = 12

# get parent directory name
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/processed_data/by_subject_child/extra_variables/'
basic_stats_file = parent_dir + '/data/data_analysis/basic_stats.csv'
output_file = parent_dir + '/data/data_analysis/descriptive_stats.csv'
extra_vars_file = parent_dir + '/data/data_analysis/processed_data/avg_correct_child-EXTRA.csv'

# extract info from basis_stats.csv
basic_stats = []
with open(basic_stats_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)     # skip header line
    for row in reader:
        basic_stats.append(row)

speech_rates = []
anaphora_utt_rates = []
anaphora_use_ratios = []

for row in basic_stats:
    curr_speech_rate = float(row[TOTAL_UTTERANCES]) / float(row[TOTAL_TIME])
    curr_anaphora_utt_rate = float(row[NUM_ANAPHORA]) / float(row[TOTAL_TIME])
    curr_anaphora_use_ratio = curr_anaphora_utt_rate / curr_speech_rate

    speech_rates.append(curr_speech_rate)
    anaphora_utt_rates.append(curr_anaphora_utt_rate)
    anaphora_use_ratios.append(curr_anaphora_use_ratio)

# SPEECH RATE
speech_rate_row = ['parent utterances per min']
avg_speech_rate = str(statistics.mean(speech_rates))
speech_rate_row.append(avg_speech_rate)

stdev_speech_rate = str(statistics.stdev(speech_rates))
speech_rate_row.append(stdev_speech_rate)

min_speech_rate = str(min(speech_rates))
speech_rate_row.append(min_speech_rate)

max_speech_rate = str(max(speech_rates))
speech_rate_row.append(max_speech_rate)

# ANAPHORA UTTERANCE RATE
anaphora_utt_rate_row = ['anaphora utterances per min'] 
avg_anaphora_utt_rate = str(statistics.mean(anaphora_utt_rates))
anaphora_utt_rate_row.append(avg_anaphora_utt_rate)

stdev_anaphora_utt_rate = str(statistics.stdev(anaphora_utt_rates))
anaphora_utt_rate_row.append(stdev_anaphora_utt_rate)

min_anaphora_utt_rate = str(min(anaphora_utt_rates))
anaphora_utt_rate_row.append(min_anaphora_utt_rate)

max_anaphora_utt_rate = str(max(anaphora_utt_rates))
anaphora_utt_rate_row.append(max_anaphora_utt_rate)

# ANAPHORA USE RATIO
anaphora_use_ratio_row = ['anaphora use ratio']
avg_anaphora_use_ratio = str(statistics.mean(anaphora_use_ratios))
anaphora_use_ratio_row.append(avg_anaphora_use_ratio)

stdev_anaphora_use_ratio = str(statistics.stdev(anaphora_use_ratios))
anaphora_use_ratio_row.append(stdev_anaphora_use_ratio)

min_anaphora_use_ratio = str(min(anaphora_use_ratios))
anaphora_use_ratio_row.append(min_anaphora_use_ratio)

max_anaphora_use_ratio = str(max(anaphora_use_ratios))
anaphora_use_ratio_row.append(max_anaphora_use_ratio)

# extract info from extra_vars file
extra_vars = []
with open(extra_vars_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)     # skip header line
    for row in reader:
        extra_vars.append(row)

child_driven_props = []
visual_cue_props = []
for row in extra_vars:
    child_driven_props.append(float(row[CHILD_DRIVEN_PROP]) / 100)
    visual_cue_props.append(float(row[VISUAL_CUE_PROP]) / 100)

# CHILD DRIVEN PROPORTION
child_driven_row = ['child-driven anaphora prop']
avg_child_driven_prop = str(statistics.mean(child_driven_props))
child_driven_row.append(avg_child_driven_prop)

stdev_child_driven_prop = str(statistics.stdev(child_driven_props))
child_driven_row.append(stdev_child_driven_prop)

min_child_driven_prop = str(min(child_driven_props))
child_driven_row.append(min_child_driven_prop)

max_child_drive_prop = str(max(child_driven_props))
child_driven_row.append(max_child_drive_prop)

# VISUAL CUE PROPORTION
visual_cue_row = ['visual cue anaphora prop']
avg_visual_cue_prop = str(statistics.mean(visual_cue_props))
visual_cue_row.append(avg_visual_cue_prop)

stdev_visual_cue_prop = str(statistics.stdev(visual_cue_props))
visual_cue_row.append(stdev_visual_cue_prop)

min_visual_cue_prop = str(min(visual_cue_props))
visual_cue_row.append(min_visual_cue_prop)

max_visual_cue_prop = str(max(visual_cue_props))
visual_cue_row.append(max_visual_cue_prop)

header = [ '', 'mean', 'stdev', 'min', 'max' ]

# write to output file
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerow(speech_rate_row)
    writer.writerow(anaphora_utt_rate_row)
    writer.writerow(anaphora_use_ratio_row)
    writer.writerow(child_driven_row)
    writer.writerow(visual_cue_row)