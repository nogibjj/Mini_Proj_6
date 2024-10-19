
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import run_query



def test_extract():
    """test extract"""
    test1 = extract()
    assert test1 is not None


def test_load():
    extract()
    data = load()
    if data:
        print("Database loading successful:")
        for row in data:
            print(row)
    else:
        print("Failed to load the database.")


def test_run_query():
    print("Querying...")
    complex_query = """
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
    """
    res = run_query(complex_query)
    assert res is None


if __name__ == "__main__":
    test_extract()
    test_load()
    test_run_query()
