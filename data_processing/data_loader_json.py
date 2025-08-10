# data_loader_json.py
import pandas as pd

def load_and_preprocess(file_path):
    # Загрузка и предобработка JSON
    data = pd.read_json(file_path)
    # Здесь ваша специфическая обработка
    return data
