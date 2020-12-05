'''
analyze_by_ID.py
Script to analyze each subject separately and write data to separate files
'''
import csv
import os

# column numbers
C_TARGET = 9
C_OTHER = 10
P_TARGET = 15
P_OTHER = 16

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/'

# read in data from the combined spreadsheet
with open(data_dir + 'anaphora_speech_combined.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        data.append(row)
    
header = data[:4]   # header information
data = data[4:]     # actual data

sub_ids = []
for data_row in data:
    curr_id = data_row[0]
    # new subject ID gets a new csv file
    if curr_id not in sub_ids:
        sub_ids.append(curr_id)
        with open(data_dir + 'by_subject/' + curr_id + '.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            # write header information to start off the file
            for head_row in header:
                writer.writerow(head_row)
            # write first row of data
            writer.writerow(data_row)
    else:
        # subject has been seen before, write to the same csv file as before
        with open(data_dir + 'by_subject/' + curr_id + '.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data_row)
            
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

def get_mcdi():
    with open(data_dir + 'mcdi_exp12.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        score_data = {}
        for row in reader:
            score_data[row[0]] = row[1]

def utter_avg():
    with open(data_dir + 'by_subject/avg_time_utterance.csv', 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(['subID', 'age', 'child target avg', 'child-other avg', 'parent target avg', 'parent other avg'])
        for curr_id in sub_ids:
            age = sub_age[curr_id]
            with open(data_dir + 'by_subject/' + curr_id + '.csv', 'r') as sub_file: 
                reader = csv.reader(sub_file)            

                c_target_total = 0
                c_other_total = 0
                p_target_total = 0
                p_other_total = 0

                data = []
                for row in reader:
                    data.append(row)
                
                header = data[:4]
                data = data[4:]
                num_anaphora = float(len(data))
                
                for row in data:
                    c_target_total += float(row[C_TARGET])
                    c_other_total += float(row[C_OTHER])
                    p_target_total += float(row[P_TARGET])
                    p_other_total += float(row[P_OTHER])

                c_target_avg = c_target_total / num_anaphora
                c_other_avg = c_other_total / num_anaphora
                p_target_avg = p_target_total / num_anaphora
                p_other_avg = p_other_total / num_anaphora

            writer.writerow([curr_id, age, c_target_avg, c_other_avg, p_target_avg, p_other_avg])


def correct_avg():
    with open(data_dir + 'by_subject/avg_correct.csv', 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(['subID', 'age', 'child correct avg', 'parent correct avg'])
        for curr_id in sub_ids:
            age = sub_age[curr_id]
            with open(data_dir + 'by_subject/' + curr_id + '.csv', 'r') as sub_file: 
                reader = csv.reader(sub_file)            

                c_target_counter = 0
                p_target_counter = 0
                
                data = []
                for row in reader:
                    data.append(row)
                
                header = data[:4]
                data = data[4:]
                num_anaphora = float(len(data))
                
                for row in data:
                    if float(row[C_TARGET]) >= 0.1:
                        c_target_counter += 1
                    if float(row[P_TARGET]) >= 0.1:
                        p_target_counter += 1
                
                c_target_avg = c_target_counter / num_anaphora
                p_target_avg = p_target_counter / num_anaphora

            writer.writerow([curr_id, age, c_target_avg, p_target_avg])


utter_avg()
correct_avg()