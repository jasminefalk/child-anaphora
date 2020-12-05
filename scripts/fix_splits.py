'''
fix_splits.py

Script to correct accuracy scores that are incorrect 
due to split anaphora being counted separately

AUTHOR: JASMINE FALK
'''
import os
import csv 

# split type variable
SPLIT = '2'

# output file name
output_file = 'post-split-fix-child.csv'

# column numbers
SUB_ID = 0
ONSET = 1
OFFSET = 2
REF_ID = 3
CUE = 4
TYPE = 5
PROP_TARGET = 6
PROP_OTHER = 7

ADD_COL = 7

# go to correct directory
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/'

# read in data from the combined spreadsheet
with open(data_dir + 'pre-split-fix-child.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        data.append(row)

# write header
with open(data_dir + output_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data[0])

# iterate through each row in the data, skipping rows that are checked by inner loop
# end when there are no more rows to check
i = 1       # skip header row
while i < len(data):
    if data[i][TYPE] == SPLIT:
        # store rows corresponding to the same anaphor in temp array
        same_split = []
        same_split.append(data[i])

        # while loop until the timestamp is different OR not a split anaphor
        time = data[i][ONSET]
        j = i + 1
        while data[j][TYPE] == SPLIT and data[j][ONSET] == time:
            same_split.append(data[j])
            j += 1

        # FOR TESTING: print out same_split
        # for row in same_split:
        #     print(row)

        # combine the rows of the same_split array
        combined_IDs = ''
        total_target_prop = 0
        for i, row in enumerate(same_split):
            curr_id = int(row[REF_ID])
            combined_IDs += str(curr_id)
            if i < len(same_split)-1:
                combined_IDs += ', '
                
            # search the cat-x cols for target prop value
            total_target_prop = float(same_split[0][ADD_COL + curr_id])

        total_other_prop = 1 - total_target_prop

        combined_line = same_split[0]
        combined_line[REF_ID] = combined_IDs
        combined_line[PROP_TARGET] = total_target_prop
        combined_line[PROP_OTHER] = total_other_prop

        with open(data_dir + output_file, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(combined_line)

        # once while loop is finished, skip to the row it ended on 
        i = j
    # else move to the next row
    else:
        with open(data_dir + output_file, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[i])
        i += 1