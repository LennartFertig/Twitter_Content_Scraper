import pandas as pd

data = pd.read_pickle(r"./data/elonmusk_last_500.pkl")

print(data.info())