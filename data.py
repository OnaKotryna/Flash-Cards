import pandas as pd


csv_data = "./data/de_1k.csv"
df = pd.read_csv(csv_data)


def get_languages():
    return df.columns.tolist()


def get_word():
    words = df.sample(n=1)
    return words.to_dict(orient="records")[0]
