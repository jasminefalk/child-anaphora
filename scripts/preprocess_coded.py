'''
Script to convert coded transcripts into exportable data format
'''

import csv
import re
import sys

# CONSTANTS
# column numbers in transcript file 
ONSET = 0   # onset time
OFFSET = 1  # offset time
WORD = 2    # anaphora word
REF = 3     # referent object ID
TYPE = 4    # anaphora type
CUE = 5     # cue type

# subject ID
SUBJ_ID = sys.argv[1]

# output file names
WORD_FILE = 'export_data/' + SUBJ_ID + '/cevent_speech_anaphora-word.csv'
REF_FILE = 'export_data/' + SUBJ_ID + '/cevent_speech_anaphora-referent.csv'
TYPE_FILE = 'export_data/' + SUBJ_ID + '/cevent_speech_anaphora-type.csv'
CUE_FILE = 'export_data/' + SUBJ_ID + '/cevent_speech_anaphora-cue.csv'

# other-object referents to be changed 
OTHER_REFS = set(['27', '29', '30', '31', '32', '34', '35', 
                  '36', '37', '38', '39', '41', '42', '43'])
OTHER_ID = '26'
PERSON_ID = '25'

# CONVERT TRANSCRIPT INTO CSV FILES BY FIELD
transcript_file = 'export_data/'+ SUBJ_ID + '/speech_' + SUBJ_ID + '-coded.txt'
transcript = list(csv.reader(open(transcript_file, 'r'), delimiter = '\t'))

# build csv files 
def makeCSV(field, output_file):
    output_data = []
    for row in transcript:
        # remove lines with no anaphora and anaphora referencing non-present objects
        if row[field] != '':
            field_row = [row[ONSET], row[OFFSET]]
            # duplicate line with (single) split anaphora 
            if ',' not in row[field]:
                if '/' in row[field]:
                    refs = row[field].split('/')
                    for obj_id in refs:
                        field_row.append(obj_id)
                        output_data.append(field_row)
                        field_row = [row[ONSET], row[OFFSET]]
                else:
                    field_row.append(row[field])
                    output_data.append(field_row)

            # duplicate lines with multiple anaphora
            else:
                anaphora = re.split(r'/|, ', row[field])
                # print(anaphora)
                for inst in anaphora:
                    field_row.append(inst)
                    output_data.append(field_row)
                    field_row = [row[ONSET], row[OFFSET]]          

    # convert type names to number codes 
    if field == TYPE:
        convert_type(output_data)
    if field == REF:
        convert_refs(output_data)

    with open(output_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in output_data:
            writer.writerow(row)

# convert anaphora type coding into numers: 1 = ONE
#                                           2 = SPLIT
#                                           3 = PRONOUN
def convert_type(output_data):
    for row in output_data:
        if row[2] == 'one' or row[2] == 'one ':
            row[2] = 1
        elif row[2] == 'split' or row[2] == 'split ':
            row[2] = 2
        elif row[2] == 'pronoun' or row[2] == 'pronoun ':
            row[2] = 3
        else:
            error_msg = 'ERROR: invalid type code ' + row[2]
            print(error_msg)
            exit(1)
    return output_data

def convert_refs(output_data):
    for row in output_data:
        if row[2] == '40' or row[2] == '28':
            row[2] = PERSON_ID
        elif row[2] in OTHER_REFS:
            row[2] = OTHER_ID

makeCSV(WORD, WORD_FILE)
makeCSV(REF, REF_FILE)
makeCSV(TYPE, TYPE_FILE)
makeCSV(CUE, CUE_FILE)