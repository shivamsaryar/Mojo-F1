import time
import os
from google.cloud import bigquery
import google.auth

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"
    ]
)

# Construct BigQuery client object
bq_client = bigquery.Client(credentials=credentials, project=project)

#Configure BigQuery dataset ID and reference
dataset_id = "mojo-f1.f1_raw_gsheets"
dataset_ref = bq_client.get_dataset(dataset_id)
#print("Dataset Ref: ", dataset_ref)

# Configure Google Sheets spreadsheet connection
external_config = bigquery.ExternalConfig("GOOGLE_SHEETS")
gsheet_url = 'https://docs.google.com/spreadsheets/d/1hfJUiVzsn5_CrmKQk0TrfQ2Cn4-2V-C7JyVigSV9ndc'
external_config.source_uris = [gsheet_url]

#-----------------------------------------------------------------------
# Configure external tables (sheets/tabs) to be imported from Google Sheets
options = external_config.google_sheets_options
print("options")
options.skip_leading_rows = 1 #optionally skip header row
options.range = (
    "circuits!A:Z"
)


# Set table schema
column_schema = [
    bigquery.SchemaField("circuitId", "STRING"),
    bigquery.SchemaField("circuitRef", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("location", "STRING"),
    bigquery.SchemaField("country", "STRING"),
    bigquery.SchemaField("lat", "STRING"),
    bigquery.SchemaField("lng", "STRING"),
    bigquery.SchemaField("alt", "STRING"),
    bigquery.SchemaField("url", "STRING")
]

# Set BigQuery table ID and reference
table_id = 'circuits'
table_ref = bigquery.Table(dataset_ref.table(table_id), schema=column_schema)
table_ref.external_data_configuration = external_config

# Create the table in BigQuery
table = bq_client.create_table(table_ref)

# Call table creation functions
#createTable_circuits()