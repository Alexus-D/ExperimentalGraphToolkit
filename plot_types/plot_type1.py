# plot_type1.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_and_plot(data):
    # Здесь ваша сложная обработка для типа 1
    plt.figure()
    sns.lineplot(x='X', y='Y', data=data)
    plt.title('График типа 1')
    plt.savefig('plot_type1.png')
    plt.close()
