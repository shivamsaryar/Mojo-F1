from google.cloud import bigquery
import os

bigquery_credentials = '/Users/shivamsaryar/Documents/GitHub/MojoF1/mojo-f1-service-account.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = bigquery_credentials

bq_client = bigquery.Client()

sql_query = """ 
    SELECT *
    FROM `mojo-f1.f1_raw.seasons`
    LIMIT 10 
"""
query_job = bq_client.query(sql_query)

print("Year  |  Wiki")
for row in query_job.result():
    print(row[0], " | ", row[1])