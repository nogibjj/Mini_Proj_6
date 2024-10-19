# Xianjing_Huang_Mini_Proj_6
[![CI](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_5/actions/workflows/cicd.yml)

### Directory Tree Structure
```
Xianjing_Huang_Mini_Proj_6/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── cicd.yml
├── data/
│   ├── customers.csv
│   └── orders.csv
├── imgs/
├── mylib/
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── Query_log.md
├── README.md
├── requirements.txt
├── setup.sh
└── test_main.py
```
extract.py: Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well.

transform_load.py: Transforms and Loads data into the local SQLite3 database.

query.py:
- `log`: Record query in query_log.md.
- `create_CRUD`: Insert a new record in database.
- `read_CRUD`: Retrieve all the records in database.
- `update_CRUD`: Replace a record with new data.
- `delete_CRUD`: Delete a record in database.

main.py: Call all the functions in mylib/ to perform CRUD and add log.

test_main.py: Test for main.

Makefile: Defines scripts for common project tasks such as testing.

cicd.yml: Defines the GitHub Actions workflow for install, lint, format, test, generate_and_push.

### Requirements
* Design a complex SQL query involving joins, aggregation, and sorting
* Provide an explanation for what the query is doing and the expected results


### Preparation
1. Open codespaces
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed
3. If running locally, `git clone` the repository and use `make install`
   ![0](/imgs/000.png)

### Check format and test errors
1. Format code `make format`

   ![1](/imgs/001.png)
2. Lint code `make lint`

   ![2](/imgs/002.png)
3. Test code `make test`

   ![3](/imgs/003.png)

### Connect to a SQL database
Extract a dataset from a URL("https://raw.githubusercontent.com/nogibjj/Xianjing_Huang_Mini_Proj_test/main/play_tennis.csv"
). Transforms and Loads data into the local SQLite3 database.

play_tennis.csv

<img src="/imgs/006.png" alt="0" height="300">

### Complex Query
Explanations of query:
```sql
SELECT 
    c.customer_name, 
    c.city, 
    COUNT(o.order_id) AS total_orders, 
    SUM(o.order_amount) AS total_amount
FROM 
    mini6.xjh_customers c
JOIN 
    mini6.xjh_orders o
ON 
    c.customer_id = o.customer_id
GROUP BY 
    c.customer_name, c.city
HAVING 
    total_amount > 200
ORDER BY 
    total_amount DESC;
```
This query joins the customers and orders tables, aggregates the data by counting the number of orders per customer, and sums the order amounts. It filters results to show only customers with a total order amount greater than 200, and sorts them in descending order by total amount.
<img src="/imgs/004.png" alt="0" height="400">
<img src="/imgs/005.png" alt="0" height="450">

### Log of database operations
Record query in query_log.md.

<img src="/imgs/007.png" alt="0" height="350">

### Continuous Integration (CI/CD Pipeline)
Perform CRUD and add SQL log via CI/CD.

<img src="/imgs/008.png" alt="0" height="350">

