'''
accuracy_score.py

Script to generate plots of split anaphora accuracy
scores as a function of 1) age, and 2) MCDI scores

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
age_data = master_dir + '/data/data_analysis/processed_data/split_age_accuracy.csv'
mcdi_data = master_dir + '/data/data_analysis/processed_data/split_mcdi_accuracy.csv'

# deep magenta: #AD1963
# green (complementary): #19AD63

# plot a basic scatterplot (with no regression line) for age
df = pd.read_csv(age_data, index_col=0)
x = df['age']
y = df['split accuracy']
ax = sns.regplot(x, y, data=df, color='#AD1963')
ax.set(xlabel='Age (in months)', ylabel="Split anaphora resolution accuracy")
plt.title('Age vs. Split Anaphora Resolution Accuracy Score')
plt.show()

# plot a basic scatterplot (with no regression line) for MCDI ProdTotal
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdTotal']
y = df['split accuracy']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdTotal', ylabel="Split anaphora resolution accuracy")
plt.title('MCDI ProdTotal vs. Split Anaphora Resolution Accuracy Score')
plt.show()

# plot a basic scatterplot (with no regression line) for MCDI ProdCountNoun
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdCountNoun']
y = df['split accuracy']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdCountNoun', ylabel="Split anaphora resolution accuracy")
plt.title('MCDI ProdCountNoun vs. Split Anaphora Resolution Accuracy Score')
plt.show()