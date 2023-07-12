import time
from google.cloud import bigquery

#Construct a BigQuery client object
client = bigquery.Client()

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=False,
)

#set table_id to the ID of the table to be created
table_id = "mojo-f1.raw-f1-datasets.circuits"

with open(r'circuits.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

while job.state != 'DONE':
    time.sleep(2)
    job.reload()
    print(job.state)

print(job.result())

table = client.get_table(table_id)
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)    