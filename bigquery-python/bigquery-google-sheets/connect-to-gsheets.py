import time
from google.cloud import bigquery
import google.auth

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
credentials, project = google.auth.default (
    scopes=[
        "https: //www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery"
    ]
)

#Construct BigQuery client object
bqClient = bigquery.Client(credentials=credentials, project=project)