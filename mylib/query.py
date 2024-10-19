"""Query the database"""

from dotenv import load_dotenv
from databricks import sql
import os

LOG_FILE = "query_log.md"


def log(query, result="none"):
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def run_query(sql_query):
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        c = connection.cursor()
        c.execute(sql_query)
        result = c.fetchall()
    c.close()
    log(f"{sql_query}", result)