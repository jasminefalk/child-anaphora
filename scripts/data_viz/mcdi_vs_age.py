'''
mcdi_vs_age.py

Script to generate plot of MCDI scores vs. age

AUTHOR: JASMINE FALK
'''
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# get name of data file
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/data/data_analysis/processed_data/child_stats_mcdi_removed.csv'

# deep magenta: #AD1963
# green (complementary): #19AD63

# plot a basic scatterplot (no regression line) for MCDI ProdTotal
df = pd.read_csv(data_file, index_col=0)
x = df['age']
y = df['MCDI ProdTotal']
ax = sns.regplot(x, y, data=df, color='#AD1963')
ax.set(xlabel='Age (in months)', ylabel='MCDI ProdToal')
plt.title('MCDI ProdTotal vs. Age')
plt.show()

# plot a basic scatterplot (no regression line) for MCDI ProdCountNoun
df = pd.read_csv(data_file, index_col=0)
x = df['age']
y = df['MCDI ProdCountNoun']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='Age (in months)', ylabel='MCDI ProdCountNoun')
plt.title('MCDI ProdCountNoun vs. Age')
plt.show()