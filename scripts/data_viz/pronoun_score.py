'''
accuracy_score.py

Script to generate plots of pronoun accuracy scores as 
a function of 1) age, and 2) MCDI scores

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
mcdi_data = master_dir + '/data/data_analysis/processed_data/child_stats_mcdi_removed.csv'
age_data = master_dir + '/data/data_analysis/processed_data/avg_correct_child-EDITED.csv'

# deep magenta: #AD1963
# green (complementary): #19AD63

# plot a basic scatterplot (with no regression line) for age
df = pd.read_csv(age_data, index_col=0)
x = df['age']
y = df['pronoun accuracy']
ax = sns.regplot(x, y, data=df, color='#AD1963')
ax.set(xlabel='Age (in months)', ylabel="Pronoun resolution accuracy")
plt.title('Age vs. Pronoun Resolution Accuracy Score')
plt.show()

# plot a basic scatterplot (with no regression line) for MCDI ProdTotal
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdTotal']
y = df['pronoun accuracy']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdTotal', ylabel="Pronoun resolution accuracy")
plt.title('MCDI ProdTotal vs. Pronoun Resolution Accuracy Score')
plt.show()

# plot a basic scatterplot (with no regression line) for MCDI ProdCountNoun
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdCountNoun']
y = df['pronoun accuracy']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdCountNoun', ylabel="Pronoun resolution accuracy")
plt.title('MCDI ProdCountNoun vs. Pronoun Resolution Accuracy Score')
plt.show()