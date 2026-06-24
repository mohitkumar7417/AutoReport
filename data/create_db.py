import sqlite3

conn = sqlite3.connect("data/sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    Product TEXT,
    Sales INTEGER
)
""")

cursor.execute("DELETE FROM sales")

cursor.executemany(
    "INSERT INTO sales VALUES (?, ?)",
    [
        ("Laptop", 50),
        ("Mobile", 80),
        ("Tablet", 30)
    ]
)

conn.commit()
conn.close()

print("Database created successfully!")