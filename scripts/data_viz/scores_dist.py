'''
scores_dist.py

Script to generate distribution plot of resolution accuracy scores

AUTHOR: JASMINE FALK
'''
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# get name of data file
curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
master_dir = os.path.dirname(parent_dir)
data_file = master_dir + '/data/data_analysis/processed_data/avg_correct_child-EDITED.csv'

sns.set(style="white", palette="muted", color_codes=True)

# Plot a histogram and kernel density estimate
df = pd.read_csv(data_file, index_col=0)
d = df['Resolution Accuracy Score']
sns.distplot(d, color="m", hist=True, fit=norm)
plt.title('Distribution of Child Anaphora Resolution Accuracy Scores')
plt.show()