from google.cloud import bigquery
import os

bigquery_credentials = '/Users/shivamsaryar/Documents/GitHub/MojoF1/mojo-f1-service-account.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = bigquery_credentials

bq_client = bigquery.Client()

sql_query = "SELECT * FROM `bigquery-public-data`.stackoverflow.stackoverflow_posts limit 10"

job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)

query_job = bq_client.query(sql_query, job_config=job_config)
print('This query will require {0} MB computing power'.format(query_job.total_bytes_processed // 1_000_000))
#print(query_job.total_bytes_processed)
