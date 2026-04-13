import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values
    df = df.fillna("N/A")
    return df