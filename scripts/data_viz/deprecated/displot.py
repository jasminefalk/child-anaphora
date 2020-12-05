import os
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
data_dir = parent_dir + '/data/data_analysis/by_subject/'

sns.set(style="white", palette="muted", color_codes=True)


# Plot a histogram and kernel density estimate
df = pd.read_csv(data_dir + 'avg_correct.csv', index_col=0)
d = df['Child Anaphora Resolution Accuracy']
sns.distplot(d, color="m", hist=True, fit=norm)
# ax.set(xlabel=, ylabel=y_label)
plt.title('Distribution of Anaphora Accuracy Scores')
plt.show()