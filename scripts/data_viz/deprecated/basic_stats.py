import os
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# deep magenta: #AD1963
# green (complementary): #19AD63

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/'
filename = 'basic_stats.csv'

# Plot a basic scatterplot (no regression line)
def scatterplot(filename, x_col, y_col, x_label, y_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.scatterplot(x, y, data=df, color='#AD1963' )
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

# def scatterplot(filename, x_col, y1_col, y2_col, x_label, y1_label, y2_label, title):
#     df = pd.read_csv(data_dir + filename, index_col=0)
#     y1 = df[y1_col]
#     y2 = df[y2_col]
#     x = df[x_col]
#     fig = plt.figure()
#     ax = plt.subplot(111)
#     ax.scatter(x, y1, label=y1_label, color='#AD1963')
#     ax.scatter(x, y2, label=y2_label, color='#19AD63')
#     ax.legend()
#     plt.title(title)
#     plt.show()

# scatterplot(filename, x, y1, y2, x_label, y1_label, y2_label, title)


# Plot a scatterplot with a linear regression line
def regplot(filename, x_col, y_col, x_label, y_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.regplot(x, y, data=df, color='#AD1963')
    ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

# Plot a histogram and kernel density estimate
def distplot(filename, data_col):
    df = pd.read_csv(data_dir + filename, index_col=0)
    d = df[data_col]
    sns.distplot(d, color="m")
    plt.show()


y = '% anaphora'
x = 'age'
x_label = "Age (in months)"
title = 'Age vs. % Utterances with Anaphora per Total Utterances'

# regplot(filename, x, y, x_label, y_label, title)
# def scatterplot(filename, x_col, y1_col, y2_col, x_label, y1_label, y2_label, title):

#     ax.scatter(x, y1, label=y1_label, color='#AD1963')
#     ax.scatter(x, y2, label=y2_label, color='#19AD63')
def lineplot(filename, x_col, y1_col, y2_col, x_label, y1_label, y2_label, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y1 = df[y1_col]
    y2 = df[y2_col]
    x = df[x_col]
    ax = plt.subplot(111)
    ax = sns.lineplot(x, y1, label=y1_label, color='#AD1963')
    ax = sns.lineplot(x, y2, label=y2_label, color='#19AD63')
    # ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

y1 = '% multiple'
y2 = '%split'
x = 'age'
title = 'Age vs. Anaphora Complexity'
x_label = 'Age (in months)'
y1_label = "% Utterances with Multiple Referents"
y2_label = "% Utterances with Split Anaphora"

lineplot(filename, x, y1, y2, x_label, y1_label, y2_label, title)


y = '% multiple'
x = 'age'
x_label = "Age (in months)"
y_label = "%"
title = 'Age vs. % Anaphoric Utterances with Multiple Referents'

scatterplot(filename, x, y, x_label, y_label, title)

y = '%split'
x = 'age'
x_label = "Age (in months)"
y_label = "%"
title = 'Age vs. % Anaphoric Utterances with Split Anaphora'

scatterplot(filename, x, y, x_label, y_label, title)

data_col = '% anaphora'
# distplot(filename, data_col)

data_col = '% multiple'
# distplot(filename, data_col)

data_col = '%split'
# distplot(filename, data_col)