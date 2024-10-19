# Xianjing_Huang_Mini_Proj_6
[![CI](https://github.com/nogibjj/Mini_Proj_6/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Mini_Proj_6/actions/workflows/ci.yml)

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
├── main.py
├── Makefile
├── query_log.md
├── README.md
├── requirements.txt
└── test_main.py
```
extract.py: Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well.

transform_load.py: Transforms and Loads data into Azure Databricks.

query.py: 
- `log`: Record query in query_log.md.
- `run_query`: Query the database from a db connection to Azure Databricks.

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
   ![1](/imgs/001.png)

### Check format and test errors
1. Format code `make format`

   ![2](/imgs/002.png)
2. Lint code `make lint`

   ![3](/imgs/003.png)
3. Test code `make test`

   ![4](/imgs/004.png)


### Complex Query
Explanations of query:
```sql
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
```
This query joins the customers and orders tables, aggregates the data by counting the number of orders per customer, and sums the order amounts. It filters results to show only customers with a total order amount greater than 200, and sorts them in descending order by total amount.

You can see the result here.
![0](/imgs/000.png)

### Log of database operations
Record query in query_log.md.

<img src="/imgs/005.png" alt="0" height="350">

### Continuous Integration (CI/CD Pipeline)
Perform query via CI/CD.

<img src="/imgs/006.png" alt="0" height="350">

