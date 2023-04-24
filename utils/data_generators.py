import pandas as pd
import numpy as np
import lorem
import matplotlib.pyplot as plt
from .excel_col import excel_col
import datetime as dt
import os


def generate_pie(n, save_path):
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    values = np.round(np.abs(np.random.rand(n)), 3)
    df = pd.DataFrame({'value': values})
    df['rank'] = df['value'].rank(method='max').astype(int)
    df['id'] = df.index + 1
    df['name'] = df['id'].apply(lambda x: excel_col(x))
    df['long_name'] = df['name'].apply(lambda name: f"{name} - {lorem.sentence()[:-1]}")
    os.makedirs(save_path, exist_ok=True)
    df.to_csv(f"{save_path}/n{n}-{timestamp}.csv", index=False)
    return df