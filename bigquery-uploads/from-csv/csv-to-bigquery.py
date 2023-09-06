from google.cloud import bigquery
import os
from pathlib import Path
import time
import google.auth

# import schemaConfig_csv
# import schemaConfig_defined
import schemaConfig_strings

def table_reference(project_id, dataset_id, table_id):
    dataset_ref = bigquery.DatasetReference(project_id, dataset_id)
    table_ref = bigquery.TableReference(dataset_id, table_id)
    return table_ref

def delete_dataset_tables(project_id, dataset_id):
    tables = bq_client.list_tables(f'{project_id}.{dataset_id}')
    for table in tables:
        bq_client.delete_table(table)
    print('Tables deleted.')

def upload_csv(client, table_name, table_ref, csv_file):
    load_job_config = bigquery.LoadJobConfig(
        source_format = bigquery.SourceFormat.CSV,
        skip_leading_rows = 1,
        autodetect = False,
        allow_quoted_newlines = True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    
    # load_job_config.schema = schemaConfig_csv.create_schema(csv_file)
    load_job_config.schema = schemaConfig_strings.getSchema(table_name)
    
    with open(csv_file, 'rb') as source_file:
        upload_job = bq_client.load_table_from_file(
            source_file,
            destination=table_ref,          
            location='US',
            job_config=load_job_config
        )

project_id = 'mojo-f1'
dataset_id = 'raw_csv_load'

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https://www.googleapis.com/auth/bigquery"
    ]
)

# Create a BigQuery client object (change project if required)
bq_client = bigquery.Client(credentials=credentials, project='mojo-f1')

data_file_folder = Path('/Users/shivamsaryar/Documents/GitHub/Mojo-F1/bigquery-uploads/data-source-files/csv-july-2023')

for file in os.listdir(data_file_folder):
    if file.endswith('.csv'):
        print("----")
        print('Processing file: {0}'.format(file))
        
        table_name = str(os.path.splitext(file)[0])
        print("Table name: ",table_name)
        
        csv_file = data_file_folder.joinpath(file)
        print("csv_file: ",csv_file)
        
        table_ref = project_id + "." + dataset_id + "." + table_name
        print("table_ref: ", table_ref)
        
        upload_csv(bq_client, table_name, table_ref, csv_file)

print("------CSV files uploaded successfully.------")