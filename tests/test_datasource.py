from autoreport.data_source import CSVDataSource

source = CSVDataSource("data/sales.csv")

df = source.read()

print(df)