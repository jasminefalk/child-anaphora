import os
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# deep magenta: #AD1963
# green (complementary): #19AD63

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/processed_data/'

def scatterplot(file1, file2, x_col, y_col, x_label, y_label, title):
    df1 = pd.read_csv(data_dir + file1, index_col=0)
    df2 = pd.read_csv(data_dir + file2, index_col=0)
    y1 = df1[y_col]
    y2 = df2[y_col]
    x = df1[x_col]
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.scatter(x, y1, label='Child', color='#AD1963')
    ax.scatter(x, y2, label='Parent', color='#19AD63')
    ax.legend()
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()


# ROI TARGET CORRECTNESS
file1 = 'avg_correct_child.csv'
file2 = 'avg_correct_parent.csv'
y = 'overall accuracy'
x = 'age'
x_label = 'Age of Child (in months)'
y_label = 'Anaphora Resolution Accuracy (%)'
title = 'Comparison of Parent and Child Resolution Accuracy'

# scatterplot(file1, file2, x, y, x_label, y_label, title)
# exit(1)



# ROI TARGET PROPORTION
# filename = 'avg_time_utterance.csv'
# y1 = 'child target avg'
# y2 = 'parent target avg'
# x = 'age'
# title = 'ROI Target Proportion'

# scatterplot(filename, x, y1, y2, title)



def single_scatter(filename, x_col, y_col, x_label, y_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.scatterplot(x, y, color='#AD1963')
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

# ROI TARGET CORRECTNESS
filename = 'child_stats_mcdi_removed.csv'
y = 'overall accuracy'
x = 'MCDI ProdCountNoun'
x_label = 'MCDI'
y_label = 'Anaphora Resolution Accuracy (%)'
title = 'MCDI vs. Anaphora Resolution Accuracy'

single_scatter(filename, x, y, x_label, y_label, title)