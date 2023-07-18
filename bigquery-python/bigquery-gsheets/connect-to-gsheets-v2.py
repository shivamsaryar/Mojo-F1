import time
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

# Set BigQuery table ID
table_id = 'circuits'

# Set BigQuery table schema
column_schema = [
    bigquery.SchemaField("circuitId", "string"),
    bigquery.SchemaField("circuitRef", "string"),
    bigquery.SchemaField("name", "string"),
    bigquery.SchemaField("location", "string"),
    bigquery.SchemaField("country", "string"),
    bigquery.SchemaField("lat", "string"),
    bigquery.SchemaField("lng", "string"),
    bigquery.SchemaField("alt", "string"),
    bigquery.SchemaField("url", "string") 
]

# Create BigQuery table object
mTable = bigquery.Table(dataset_ref.table(table_id), schema=column_schema)

# Configure Google Sheets connection
external_config = bigquery.ExternalConfig("GOOGLE_SHEETS") 
gsheet_url = 'https://docs.google.com/spreadsheets/d/1hfJUiVzsn5_CrmKQk0TrfQ2Cn4-2V-C7JyVigSV9ndc/edit#gid=0'
external_config.source_uris = [gsheet_url]

# Configure external tables (sheets/tabs) to be imported from Google Sheets
options = external_config.google_sheets_options

options.skip_leading_rows = 1 #optionally skip header row
options.range = (
    "circuits"
)

mTable.external_data_configuration = external_config

# Create the table in BigQuery
table = bq_client.create_table(mTable)

# Call table creation functions
#createTable_circuits()