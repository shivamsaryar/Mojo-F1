import os
print('s')
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mojo-f1-service-account.json'

client = bigquery.Client()

sql_query = """
    SELECT *
    FROM `mojo-f1.f1_primary_dataset.drivers`
    LIMIT 10
"""

query_job = client.query(sql_query)

print(query_job)

for row in query_job.result():
    print(row)