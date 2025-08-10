# plot_type2.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_and_plot(data):
    # Здесь ваша сложная обработка для типа 2
    plt.figure()
    sns.scatterplot(x='A', y='B', data=data)
    plt.title('График типа 2')
    plt.savefig('plot_type2.png')
    plt.close()
