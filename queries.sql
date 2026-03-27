SELECT * FROM retail_sales LIMIT 10;

SELECT Region, SUM(Sales) AS Total_Sales
FROM retail_sales
GROUP BY Region;

PRAGMA table_info(retail_sales);

SELECT "Category", SUM("Sales") AS Total_Sales
FROM retail_sales
GROUP BY "Category";

SELECT "Region", SUM("Sales") AS Total_Sales
FROM retail_sales
GROUP BY "Region";

SELECT "City", SUM("Sales") AS Total_Sales
FROM retail_sales
GROUP BY "City"
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT "Ship Mode", COUNT(*) AS Orders
FROM retail_sales
GROUP BY "Ship Mode";
