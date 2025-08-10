# data_loader_excel.py
import pandas as pd

def load_and_preprocess(file_path):
    # Загрузка и предобработка Excel
    data = pd.read_excel(file_path)
    # Здесь ваша специфическая обработка
    return data
