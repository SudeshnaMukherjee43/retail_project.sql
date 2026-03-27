import pandas as pd
import sqlite3

# Step 1: read the CSV dataset
df = pd.read_csv("train.csv")

# Step 2: create/connect to SQLite database
conn = sqlite3.connect("retail.db")

# Step 3: import dataset into SQL table
df.to_sql("retail_sales", conn, if_exists="replace", index=False)

print("Data imported successfully!")