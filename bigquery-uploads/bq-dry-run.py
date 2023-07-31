from google.cloud import bigquery
import google.auth
import os

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"
    ]
)

# Create BigQuery client object (set project accordingly)
bq_client = bigquery.Client(credentials=credentials, project='mojo-f1')

sql_query = "SELECT * FROM `bigquery-public-data`.stackoverflow.stackoverflow_posts limit 10"

job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)

query_job = bq_client.query(sql_query, job_config=job_config)
print('This query will require {0} MB computing power'.format(query_job.total_bytes_processed // 1_000_000))
#print(query_job.total_bytes_processed)
