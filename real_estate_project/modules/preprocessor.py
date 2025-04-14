
import pandas as pd

def preprocess_data(df: pd.DataFrame):
    df = df.dropna()
    X = df[['area']]
    y = df['price']
    return X, y
