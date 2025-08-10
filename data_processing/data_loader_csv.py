# data_loader_csv.py
import pandas as pd

def load_and_preprocess(file_path):
    # Loading and preprocessing CSV
    data = pd.read_csv(file_path)
    # Here is your specific processing
    return data
