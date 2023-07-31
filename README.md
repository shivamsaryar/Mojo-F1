# Mojo F1 - Formula1 data project
The CSV files have been downloaded from kaggle

## Uploading CSV files to BigQuery
Uploading the source CSV files as raw tables in BigQuery can be done in one of the ways:

#### 1. Direct file upload
#### 2. Upload bulk CSV from local computer using VS Code (bigquery-uploads/from-csv/upload-bulk-csv.py)
#### 3. Upload data from Google Sheets using the Drive source in BigQuery.
- Advantages: External table
- Disadvantages: Takes time to create tables and declare schemas
#### 4. Upload data from Google Sheets using App Script
- Uploader sheet: https://docs.google.com/spreadsheets/d/1ShcEgYXYcqAqN4nh4zGdxrY7bw6v8F49Um1DZKajmHI
- Combined F1 dataset spreadsheet: https://docs.google.com/spreadsheets/d/1hfJUiVzsn5_CrmKQk0TrfQ2Cn4-2V-C7JyVigSV9ndc
- Advantages: Quick table creation, external table