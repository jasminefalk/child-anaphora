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
filename = 'mcdi_exp12.csv'

# Plot a basic scatterplot (no regression line)
def scatterplot(x_col, y_col, title):
    df = pd.read_csv(data_dir + filename, index_col=0)
    y = df[y_col]
    x = df[x_col]
    ax = sns.scatterplot(x, y, data=df, color='#AD1963')
    # ax.set(xlabel=x_label, ylabel=y_label)
    plt.title(title)
    plt.show()

scatterplot(x_col='MCDI ProdTotal',
            y_col='Child Anaphora Resolution Accuracy',
            title='MCDI ProdTotal vs. Accuracy')

scatterplot(x_col='MCDI ProdCountNoun',
            y_col='Child Anaphora Resolution Accuracy',
            title='MCDI ProdCountNoun vs. Accuracy')