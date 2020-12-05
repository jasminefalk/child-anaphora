'''
split_by_subject.py

Script to split up combined data by subject id

AUTHOR: JASMINE FALK
'''
import os
import csv 

# column number
ID_COL = 0

# go to correct directory
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/processed_data/'

# read in data from the combined spreadsheet
with open(data_dir + 'post-split-fix-parent.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        data.append(row)

i = 1       # skip header row
while i < len(data):
    curr_id = data[i][ID_COL]
    filename = data_dir + 'by_subject_parent/' + curr_id + '-parent.csv'
    # make a new file for each new subject & write header
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0])

    j = i
    while data[j][ID_COL] == curr_id:
        # copy data from combined file to new single subj file
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[j])
        j += 1
        if j >= len(data):
            break

    i = j