import psycopg2
import pandas as pd
def pg_connect():
# Establish the connection
 conn = psycopg2.connect(
    dbname="telecom",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# Create a query to fetch only the top 10 rows
 query = "SELECT * FROM xdr_data;"
def reading ():
# Load data into a DataFrame
 df = pd.read_sql(query, conn)

# Close the connection
 conn.close()