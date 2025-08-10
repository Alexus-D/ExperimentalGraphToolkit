# data_loader_csv.py
import pandas as pd

def load_and_preprocess(file_path):
    # Загрузка и предобработка CSV
    data = pd.read_csv(file_path)
    # Здесь ваша специфическая обработка
    return data
