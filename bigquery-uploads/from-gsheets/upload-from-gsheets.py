import time
from google.cloud import bigquery
import google.auth
from schemaConfig_gsheets import *

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"
    ]
)

# Construct BigQuery client object
bq_client = bigquery.Client(credentials=credentials, project='mojo-f1')

#Configure BigQuery dataset ID and reference
dataset_id = "mojo-f1.f1_raw_gsheets"
dataset_ref = bq_client.get_dataset(dataset_id)

# Configure Google Sheets connection
external_config = bigquery.ExternalConfig("GOOGLE_SHEETS") 
gsheet_url = 'https://docs.google.com/spreadsheets/d/1hfJUiVzsn5_CrmKQk0TrfQ2Cn4-2V-C7JyVigSV9ndc/edit#gid=0'
external_config.source_uris = [gsheet_url]

def createTables():
    tables_list = [
        'circuits', 
        'constructor_results', 
        'constructor_standings', 
        'constructors', 
        'driver_standings', 
        'drivers',
        'lap_times',
        'pit_stops',
        'qualifying',
        'races',
        'results',
        'seasons',
        'sprint_results',
        'status'
    ]
    for t in tables_list:
        # Configure table schema
        column_schema = getSchema(t)
        
        # Set table ID
        table_id = t
    
        # Initialise a BigQuery table object
        bq_table = bigquery.Table(dataset_ref.table(table_id), schema=column_schema)

        # Configure the table options for the sheet/tab to be imported from Google Sheets
        options = external_config.google_sheets_options
        options.range = (
            str(t)
        )
        options.skip_leading_rows = 1 #skip header row
    
        # Add the table options to the table object
        bq_table.external_data_configuration = external_config

        # Create the table in BigQuery
        bq_client.create_table(bq_table)

        # Print
        print("Table created: ", t)

createTables()
print ('All tables successfully created in BigQuery')