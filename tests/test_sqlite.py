from autoreport.ingestion import read_sqlite

df = read_sqlite("data/sales.db", "sales")

print(df)