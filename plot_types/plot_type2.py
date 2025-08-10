# plot_type2.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_and_plot(data, x='A', y='B', title='Type 2 Plot'):
    # Here is your complex processing for type 2
    plt.figure()
    sns.scatterplot(x='A', y='B', data=data)
    plt.title(title)
    plt.savefig('plot_type2.png')
    plt.close()
