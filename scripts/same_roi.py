'''
same_roi.py

How often are parents and children looking at 
the same ROI (even if its not the target)?
'''

import csv
import os

# column numbers
SUB_ID = 0
CEYE_1 = 7
CEYE_25 = 36
PEYE_1 = 82
PEYE_25 = 106

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/'

# read in data from the combined spreadsheet
with open(data_dir + 'anaphora_speech_referent.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        data.append(row)

# header = data[:3]   # header information
data = data[4:]     # actual data

gaze_dict = {}

for utterance in data:
    curr_id = utterance[SUB_ID]

    ceye_roi = set()
    peye_roi = set()

    for i in range(CEYE_1, CEYE_25):
        if utterance[i] != '0':
            roi = i - 6
            ceye_roi.add(roi)

    for i in range(PEYE_1, PEYE_25):
        if utterance[i] != '0':
            roi = i - 81
            peye_roi.add(roi)
        
        num_same = len(ceye_roi.intersection(peye_roi))

    if curr_id not in gaze_dict:
        gaze_dict[curr_id] = [num_same]
    else:
        gaze_dict[curr_id].append(num_same)

output_dict = {}
for key, val in gaze_dict.items():
    output_dict[key] = (sum(val), len(val), (sum(val)/len(val)*100)) 

# WRITE DATA ANALYSIS RESULTS TO CSV FILE
sub_age = {
    '1201': 24.3,
    '1202': 20.7,
    '1203': 18.8,
    '1204': 18.2,
    '1205':	18.1,
    '1206': 17.5,
    '1207': 25.3,
    '1208': 15.2,
    '1209': 16.2,
    '1210': 19.2,
    '1211': 24.2,
    '1212': 21.7,
    '1213': 17.3,
    '1214': 18.5,
    '1215': 18.2,
    '1216': 17.8,
    '1217': 17.5,
    '1218': 21.5,
    '1219': 19.7,
    '1220': 19.6,
    '1221': 21.6,
    '1222': 22.1,
    '1223': 21.8,
    '1224': 17.9,
    '1225': 21.1,
    '1226': 18.4,
    '1227': 22,
    '1228': 17.9,
    '1229': 16.3,
    '1230': 17.7,
    '1231': 22.1,
    '1232': 14.1,
    '1233': 12.3,
    '1234': 15.9,
    '1235': 13.8,
    '1236': 15.2,
    '1237': 13
}

with open(data_dir + 'by_subject/same_roi.csv', 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(['subID', 'age', 'num same roi', 'total utter', 'percent same'])
        for key, val in output_dict.items():
            writer.writerow([key, sub_age[key], val[0], val[1], val[2]])
