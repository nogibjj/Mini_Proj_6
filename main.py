"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import run_query


# Extract
print("Extracting data...")
extract()
print("Extracting data successfully!")

# Transform and load
print("Transforming data...")
load()
print("Transforming data successfully!")

# Query
print("Querying...")
complex_query = """
SELECT
    c.customer_name,
    c.city,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_amount
FROM
    xjh_customers c
JOIN
    xjh_orders o
ON
    c.customer_id = o.customer_id
GROUP BY
    c.customer_name, c.city
HAVING
    total_amount > 200
ORDER BY
    total_amount DESC;
"""
run_query(complex_query)
print("Running query successfully!")
