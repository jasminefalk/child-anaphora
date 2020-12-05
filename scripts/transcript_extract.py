'''
JASMINE FALK

Script to extract anaphora instances from speech transcripts.
Speech transcripts are text files with three columns separated by 1 tab:
    1) video start time of line (in seconds)
    2) video end time of line (in seconds)
    3) words spoken

Using speech_16963.txt to test.

USAGE: python3 transcript_extract.py [output_file.csv] [it] [they] ...
'''
import os
import sys
import csv
import re

# STEP 0: parse command line args to determine which anaphora to search for 
regex = r''
regex += sys.argv[1]
# for i, arg in enumerate(sys.argv):
#     if i != 0 and i != 1:
#         if i == len(sys.argv)-1:
#             regex += r'\b' + arg + r'\b'
#         else:
#             regex += r'\b' + arg + r'\b|'

basepath = 'transcripts/'
for file in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, file)) and file != ".DS_Store":
        # get participant id
        p_id = file.split('_')[1].split('.')[0]

        # STEP 1: read in text file and store as 2d array

        # transcript data structure:
        # [[start_time, end_time, 'speech string'],
        #  [...],
        #  ...]
        txt_file = "transcripts/" + file
        transcript = list(csv.reader(open(txt_file, "r"), delimiter = '\t'))

        # STEP 2: search for anaphora using regex
        anaphora = []
        for i, line in enumerate(transcript):
            if re.search(regex, line[2]):
                # first el line before, second el target line, third el line after
                context = []
                if i == 0:
                    context.append('')
                else:
                    context.append(transcript[i-1])
                context.append(line)
                if i == len(transcript)-1:
                    context.append('')
                else:
                    context.append(transcript[i+1])

                anaphora.append(context)

        # STEP 3: write to csv file
        write_file = "output/" + p_id + "_" + sys.argv[1] + ".csv"
        with open(write_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            for row in anaphora:
                csvwriter.writerow(row)