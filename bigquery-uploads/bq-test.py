import os
import time
import google.auth
from google.cloud import bigquery

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"
    ]
)

# Create a BigQuery client object (change project if required)
bq_client = bigquery.Client(credentials=credentials, project='mojo-f1')

# SQL query to test connection
sql_query = """ 
    SELECT *
    FROM `mojo-f1.f1_raw_csv.seasons`
    LIMIT 10 
"""
query_job = bq_client.query(sql_query)

print("Year  |  Wiki")
for row in query_job.result():
    print(row[0], " | ", row[1])