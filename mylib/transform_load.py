"""
Transforms and Loads data into the local databricks database

"""
import csv
from dotenv import load_dotenv
from databricks import sql
import os

#load the csv file and insert into a new databricks database
def load(dataset1="data/customers.csv", dataset2="data/orders.csv"):
    """"Transforms and Loads data into the local databricks database"""
    payload = csv.reader(open(dataset1, newline=""), delimiter=",")
    next(payload)
    payload2 = csv.reader(open(dataset2, newline=""), delimiter=",")
    next(payload2)

    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            print("1")

            # customer_id, customer_name, city, signup_date
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS xjh_customers 
                           (customer_id INT, 
                            customer_name STRING, 
                            city STRING, 
                            signup_date DATE);
                """
            )
            print("2")
            cursor.execute("SELECT * FROM xjh_customers")
            result = cursor.fetchall()
            if not result:
                print("xjh_customers is blank, start intsert")
            
                string_sql = "INSERT INTO xjh_customers VALUES"
                for i in payload:
                    string_sql += "\n" + str(tuple(i)) + ","
                string_sql = string_sql[:-1] + ";"
                print(string_sql)

                cursor.execute(string_sql)

            # order_id, customer_id, order_amount, order_date
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS xjh_orders 
                           (order_id INT,
                            customer_id INT,
                            order_amount INT,  
                            order_date DATE);
                """
            )

            cursor.execute("SELECT * FROM xjh_orders")
            result = cursor.fetchall()
            if not result:
                print("xjh_orders is blank, start intsert")
            
                string_sql = "INSERT INTO xjh_orders VALUES"
                for i in payload2:
                    string_sql += "\n" + str(tuple(i)) + ","
                string_sql = string_sql[:-1] + ";"
                print(string_sql)

                cursor.execute(string_sql)

            cursor.close()
            connection.close()
    return "already loaded"

