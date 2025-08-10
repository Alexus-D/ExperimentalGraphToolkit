# plot_type1.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_and_plot(data, x='X', y='Y', title='Type 1 Plot'):
    # Here is your complex processing for type 1
    plt.figure()
    sns.lineplot(x='X', y='Y', data=data)
    plt.title(title)
    plt.savefig('plot_type1.png')
    plt.close()
