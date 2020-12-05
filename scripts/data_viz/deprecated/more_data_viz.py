import os
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/by_subject/'

def single_scatter(filename, x_col, y_col, x_label, y_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.scatterplot(x, y, data=df, color='#AD1963' )
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

filename = 'same_roi.csv'
y = 'percent same'
x = 'age'
x_label = 'Age (in months)'
y_label = 'Percent same'
title = 'Age vs. Same ROI Percent'

# single_scatter(filename, x, y, x_label, y_label, title)



def barplot(filename, x_col, y1_col, y2_col, x_label, y_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y1 = df[y1_col]
    y2 = df[y2_col]
    x = df[x_col]
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.barplot(x, y1, label='Child', color='#AD1963')
    ax.barplot(x, y2, label='Parent', color='#19AD63')
    ax.legend()
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

filename = 'avg_correct.csv'
y1 = 'child correct avg'
y2 = 'parent correct avg'
x = 'age'
x_label = 'Subject ID'
y_label = 'Target ROI fixations (% of total time)'
title = 'Parent vs. Child Fixation Accuracy'

barplot(filename, x, y1, y2, x_label, y_label, title)