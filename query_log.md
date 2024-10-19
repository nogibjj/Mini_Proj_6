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

```response from databricks
[Row(customer_name='Helen', city='Houston', total_orders=1, total_amount=800), Row(customer_name='Evan', city='Durham', total_orders=1, total_amount=700), Row(customer_name='Charlie', city='New York', total_orders=2, total_amount=650), Row(customer_name='Ian', city='Los Angeles', total_orders=1, total_amount=600), Row(customer_name='Grace', city='New York', total_orders=1, total_amount=400), Row(customer_name='Alice', city='New York', total_orders=2, total_amount=350), Row(customer_name='David', city='Houston', total_orders=1, total_amount=300)]
```

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

```response from databricks
[Row(customer_name='Helen', city='Houston', total_orders=1, total_amount=800), Row(customer_name='Evan', city='Durham', total_orders=1, total_amount=700), Row(customer_name='Charlie', city='New York', total_orders=2, total_amount=650), Row(customer_name='Ian', city='Los Angeles', total_orders=1, total_amount=600), Row(customer_name='Grace', city='New York', total_orders=1, total_amount=400), Row(customer_name='Alice', city='New York', total_orders=2, total_amount=350), Row(customer_name='David', city='Houston', total_orders=1, total_amount=300)]
```

