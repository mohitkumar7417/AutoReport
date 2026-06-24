import pandas as pd

df = pd.read_csv("data/sales.csv", sep=",")

print(df)
print(df.columns)