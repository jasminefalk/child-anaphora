'''
percent_reqCue_total.py

Script to generate plots of percentage of anaphoric 
utterances paired with extratextual cues that were required
for resolving the references out of all anaphoric instances
as a function of 1) age, and 2) MCDI scores

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
mcdi_data = master_dir + '/data/data_analysis/processed_data/child_stats_mcdi_removed-EXTRA.csv'
age_data = master_dir + '/data/data_analysis/processed_data/avg_correct_child-EXTRA.csv'

# deep magenta: #AD1963
# green (complementary): #19AD63

# plot a scatterplot with regression line for age
df = pd.read_csv(age_data, index_col=0)
x = df['age']
y = df['percent required of total anaphora']
ax = sns.regplot(x, y, data=df, color='#AD1963')
ax.set(xlabel='Age (in months)', ylabel="% of Anaphoric Utterances")
plt.title('Age vs. Percentage of Total Anaphoric Utterances with Required Extratextual Cues')
plt.show()

# plot a scatterplot with regression line for MCDI ProdTotal
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdTotal']
y = df['percent required of total anaphora']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdTotal', ylabel="% of Anaphoric Utterances")
plt.title('MCDI ProdTotal vs. Percentage of Total Anaphoric Utterances with Required Extratextual Cues')
plt.show()

# plot a scatterplot with regression line for MCDI ProdCountNoun
df = pd.read_csv(mcdi_data, index_col=0)
x = df['MCDI ProdCountNoun']
y = df['percent required of total anaphora']
ax = sns.regplot(x, y, data=df, color='#19AD63')
ax.set(xlabel='MCDI ProdCountNoun', ylabel="% of Anaphoric Utterances")
plt.title('MCDI ProdCountNoun vs. Total Anaphoric Utterances with Required Extratextual Cues')
plt.show()