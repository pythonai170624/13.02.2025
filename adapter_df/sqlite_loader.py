import sqlite3
import pandas as pd

def create_sqlite_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory =  sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE sales (
        Product TEXT,
        Region TEXT,
        Sales REAL,
        Quantity INTEGER
    )
    """)
    cursor.executemany("""
    INSERT INTO sales (Product, Region, Sales, Quantity) VALUES (?, ?, ?, ?)
    """, [
        ("Phone", "North", 5000, 25),
        ("Laptop", "South", 8000, 30),
        ("Tablet", "East", 3000, 20),
        ("Phone", "West", 5500, 27),
        ("Laptop", "North", 8500, 35),
        ("Tablet", "South", None, 15),
    ])
    conn.commit()
    return conn

