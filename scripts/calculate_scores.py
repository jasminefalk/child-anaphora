'''
calculate_scores.py

Script to calculate anaphora resolution accuracy scores for each subject,
generates csv file with a number of metric scores for each subject

AUTHOR: JASMINE FALK
'''
import os
import csv 
import sys

# TYPE VARIABLES
ONE = '1'
SPLIT = '2'
PRONOUN = '3'

# CUE VARIABLES
VERBAL = '1'
VISUAL = '2'

# INSTIGATOR VARIABLES
PARENT = '0'
CHILD = '1'

# EXTRA CUE VARIABLES
NO_EXTRA = '1'
NONREQUIRED_EXTRA = '2'
REQUIRED_EXTRA = '3'

# COLUMN NUMBERS
SUB_ID = 0
ONSET = 1
OFFSET = 2
REF_ID = 3
CUE = 4
TYPE = 5
INSTIGATOR = 6
EXTRA_CUE = 7
PROP_TARGET = 8
PROP_OTHER = 9

MCDI_TOTAL = 1
MCDI_NOUN = 2

# TARGET PROPORTION THRESHOLD
MIN_PROP = 0.1

# header line for output file
header = [ 'subID',
           'age',
           'MCDI ProdTotal',
           'MCDI ProdCountNoun',
           'total num anaphora', 
           'percent one',
           'percent split',
           'percent pronoun', 
           'percent verbal',
           'percent visual',
           'percent parent instigated', 
           'percent child instigated',
           'percent extra cues', 
           'percent no extra cue',
           'percent not required of total anaphora',
           'percent required of total anaphora',
           'percent not required of total extra cues',
           'percent required of total extra cues',
           'overall accuracy',
           'one accuracy',
           'split accuracy',
           'pronoun accuracy',
           'verbal cue accuracy',
           'visual cue accuracy',
           'parent instigated accuracy', 
           'extra cue accuracy',
           'required extra cue accuracy',
           'not required extra cue accuracy']

# get parent directory name
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)

# command line argument to toggle between parent and child folders
if len(sys.argv) != 2:
    print('Incorrect number of args.')
    exit(0)
else:
    # set up for child's directory
    if sys.argv[1] == '-c' or sys.argv == '-C':
        data_dir = parent_dir + '/data/data_analysis/processed_data/by_subject_child/extra_variables/'
        output_file = parent_dir + '/data/data_analysis/processed_data/avg_correct_child.csv'
    # set up for parent's directory
    elif sys.argv[1] == '-p' or sys.argv == '-P':
        data_dir = parent_dir + '/data/data_analysis/processed_data/by_subject_parent/'
        output_file = parent_dir + '/data/data_analysis/processed_data/avg_correct_parent.csv'
    else:
        print('Invalid arg.')
        exit(0)

# write header for output file
with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

# store subject age data
def get_ages():
    sub_ages = {}
    with open(parent_dir + '/data/data_analysis/age_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(csvfile)     # skip header line
        for row in reader:
            sub_ages[row[1]] = float(row[2])
    return sub_ages

sub_ages = get_ages()

# store subject MCDI data
def get_mcdi():
    sub_mcdi = {}
    with open(parent_dir + '/data/data_analysis/mcdi_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(csvfile)     # skip header line
        for row in reader:
            sub_mcdi[row[0]] = (float(row[MCDI_TOTAL]), float(row[MCDI_NOUN]))
    return sub_mcdi

sub_mcdi = get_mcdi()

# get list of all files in directory
file_list = os.listdir(data_dir)
for file in file_list:
    if file != '.DS_Store':
        file_data = []
        with open(data_dir + file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(csvfile)     # skip header line
            for row in reader:
                file_data.append(row)

        total_correct = 0
        total_overall = len(file_data)

        # type variables
        total_one_correct = 0
        total_one = 0
        total_split_correct = 0
        total_split = 0
        total_pronoun_correct = 0
        total_pronoun = 0
        
        # cue variables
        total_verbal_correct = 0
        total_verbal = 0
        total_visual_correct = 0
        total_visual = 0

        # instigator variables
        total_child_inst = 0
        total_parent_inst = 0
        total_parent_inst_correct = 0

        # extratextual cue variables
        total_no_extra_cue = 0
        total_no_extra_cue_correct = 0
        total_extra_cue = 0
        total_extra_cue_correct = 0
        total_req_cue = 0
        total_req_cue_correct = 0
        total_nonreq_cue = 0
        total_nonreq_cue_correct = 0

        for row in file_data:
            # calculate totals of each dependent variable
            if row[TYPE] == ONE:
                total_one += 1

            if row[TYPE] == SPLIT:
                total_split += 1

            if row[TYPE] == PRONOUN:
                total_pronoun += 1

            if row[CUE] == VERBAL:
                total_verbal += 1

            if row[CUE] == VISUAL:
                total_visual += 1
            
            if row[INSTIGATOR] == PARENT:
                total_parent_inst += 1
            
            if row[INSTIGATOR] == CHILD:
                total_child_inst += 1
            
            if row[EXTRA_CUE] == NO_EXTRA:
                total_no_extra_cue += 1

            if row[EXTRA_CUE] == NONREQUIRED_EXTRA:
                total_extra_cue += 1
                total_nonreq_cue += 1
            
            if row[EXTRA_CUE] == REQUIRED_EXTRA:
                total_extra_cue += 1
                total_req_cue += 1

            # calculate overall anaphora resolution accuracy
            if float(row[PROP_TARGET]) >= MIN_PROP:
                total_correct += 1

            # calculate anaphora resolution accuracy by type
            if float(row[PROP_TARGET]) >= MIN_PROP and row[TYPE] == ONE:
                total_one_correct += 1

            if float(row[PROP_TARGET]) >= MIN_PROP and row[TYPE] == SPLIT:
                total_split_correct += 1

            if float(row[PROP_TARGET]) >= MIN_PROP and row[TYPE] == PRONOUN:
                total_pronoun_correct += 1

            # calculate anaphora resolution accuracy by cue
            if float(row[PROP_TARGET]) >= MIN_PROP and row[CUE] == VERBAL:
                total_verbal_correct += 1
                    
            if float(row[PROP_TARGET]) >= MIN_PROP and row[CUE] == VISUAL:
                total_visual_correct += 1

            # calculate anaphora resolution accuracy by instigator
            if float(row[PROP_TARGET]) >= MIN_PROP and row[INSTIGATOR] == PARENT:
                total_parent_inst_correct += 1

            # calculate anaphora resolution accuracy by presence of extratextual cues
            if float(row[PROP_TARGET]) >= MIN_PROP and row[EXTRA_CUE] == NO_EXTRA:
                total_no_extra_cue_correct += 1
            
            if float(row[PROP_TARGET]) >= MIN_PROP and row[EXTRA_CUE] == REQUIRED_EXTRA:
                total_extra_cue_correct += 1
                total_req_cue_correct += 1

            if float(row[PROP_TARGET]) >= MIN_PROP and row[EXTRA_CUE] == NONREQUIRED_EXTRA:
                total_extra_cue_correct += 1
                total_nonreq_cue_correct += 1 
        
        # use counts to calculate averages
        overall_accuracy = total_correct / total_overall

        # accuracy based on type
        if total_one != 0:
            one_accuracy = total_one_correct / total_one
        else:
            one_accuracy = 0

        if total_split != 0:
            split_accuracy = total_split_correct / total_split
        else:
            split_accuracy = 0

        if total_pronoun != 0:
            pronoun_accuracy = total_pronoun_correct / total_pronoun
        else:
            pronoun_accuracy = 0

        # accuracy based on cue
        if total_verbal != 0:
            verbal_cue_accuracy = total_verbal_correct / total_verbal
        else:
            verbal_cue_accuracy = 0

        if total_visual != 0:
            visual_cue_accuracy = total_visual_correct / total_visual
        else:
            visual_cue_accuracy = 0

        if total_visual != 0:
            visual_cue_accuracy = total_visual_correct / total_visual
        else:
            visual_cue_accuracy = 0

        # accuracy based on instigator
        if total_parent_inst != 0:
            parent_inst_accuracy = total_parent_inst_correct / total_parent_inst
        else: 
            parent_inst_accuracy = 0

        # accuracy based on presence of extra cues
        if total_no_extra_cue != 0:
            no_extra_cue_accuracy = total_no_extra_cue_correct / total_no_extra_cue
        else: 
            no_extra_cue_accuracy = 0

        if total_nonreq_cue != 0:
            nonreq_cue_accuracy = total_nonreq_cue_correct / total_nonreq_cue
        else: 
            nonreq_cue_accuracy = 0

        if total_req_cue != 0:
            req_cue_accuracy = total_req_cue_correct / total_req_cue
        else: 
            req_cue_accuracy = 0

        if total_extra_cue != 0:
            extra_cue_accuracy = total_extra_cue_correct / total_extra_cue
        else:
            extra_cue_accuracy = 0

        # account for if no MCDI score available for some subjects to avoid KeyError
        if row[SUB_ID] in sub_mcdi:
            mcdi_total = sub_mcdi[row[SUB_ID]][0]
            mcdi_noun = sub_mcdi[row[SUB_ID]][1]
        else:
            mcdi_total = '-'
            mcdi_noun = '-'



        #    'required extra cue accuracy',
        #    'not required extra cue accuracy']
        sub_data = [ row[SUB_ID],                           # subID
                     sub_ages[row[SUB_ID]],                 # age               
                     mcdi_total,                            # MCDI ProdTotal score
                     mcdi_noun,                             # MCDI noun score
                     total_overall,                         # total num anaphora
                     total_one / total_overall,             # % ONE out of total anaphora
                     total_split / total_overall,           # % SPLIT out of total anaphora
                     total_pronoun / total_overall,         # % PRONOUN out of total anaphora
                     total_verbal / total_overall,          # % VERBAL out of total anaphora
                     total_visual / total_overall,          # % VISUAL out of total anaphora
                     total_parent_inst / total_overall,     # % PARENT INST out of total anaphora
                     total_child_inst / total_overall,      # % CHILD INST out of total anaphora
                     total_extra_cue / total_overall,       # % EXTRA CUE out of total anaphora
                     total_no_extra_cue / total_overall,    # % NO EXTRA CUE out of total anaphora
                     total_nonreq_cue / total_overall,      # % NONREQ EXTRA CUE out of total anaphora
                     total_req_cue / total_overall,         # % REQ EXTRA CUE out of total anaphora
                     total_nonreq_cue / total_extra_cue,    # % NONREQ EXTRA CUE out of EXTRA CUE anaphora
                     total_req_cue / total_extra_cue,       # % REQ EXTRA CUE out of EXTRA CUE anaphora
                     overall_accuracy,                      # overall anaphora res accuracy
                     one_accuracy,                          # ONE anaphora res accuracy
                     split_accuracy,                        # SPLIT anaphora res accuracy
                     pronoun_accuracy,                      # PRONOUN res accuracy
                     verbal_cue_accuracy,                   # VERBAL anaphora res accuracy
                     visual_cue_accuracy,                   # VISUAL anaphora res accuracy
                     parent_inst_accuracy,                  # PARENT INST anaphora res accuracy
                     extra_cue_accuracy,                    # EXTRA CUE anaphora accuracy
                     req_cue_accuracy,                      # REQUIRED EXTRA CUE anaphora accuracy
                     nonreq_cue_accuracy ]                  # NONREQUIRED EXTRA CUE anaphora accuracy


        with open(output_file, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(sub_data)