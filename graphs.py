import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to database
conn = sqlite3.connect("retail.db")

# -------- Sales by Category --------
query1 = '''
SELECT "Category", SUM("Sales") as Total_Sales
FROM retail_sales
GROUP BY "Category"
'''

df1 = pd.read_sql_query(query1, conn)

plt.figure()
plt.bar(df1["Category"], df1["Total_Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()


# -------- Sales by Region --------
query2 = '''
SELECT "Region", SUM("Sales") as Total_Sales
FROM retail_sales
GROUP BY "Region"
'''

df2 = pd.read_sql_query(query2, conn)

plt.figure()
plt.bar(df2["Region"], df2["Total_Sales"])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()


# -------- Top 10 Cities --------
query3 = '''
SELECT "City", SUM("Sales") as Total_Sales
FROM retail_sales
GROUP BY "City"
ORDER BY Total_Sales DESC
LIMIT 10
'''

df3 = pd.read_sql_query(query3, conn)

plt.figure()
plt.bar(df3["City"], df3["Total_Sales"])
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

conn.close()