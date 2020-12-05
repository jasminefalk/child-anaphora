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
filename = 'type_data.csv'

# Plot a basic scatterplot (no regression line)
def scatterplot(x_col, y_col, xlabel, ylabel, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.scatterplot(x, y, data=df, color='#AD1963')
    ax.set(xlabel=xlabel, ylabel=ylabel)
    plt.title(title)
    plt.show()

scatterplot(x_col='age',
            y_col='% pronoun accurate',
            xlabel='Age',
            ylabel='Pronoun Resolution Accuracy',
            title='Child Pronoun Resolution Accuracy vs. Age')