import requests
from google.cloud import bigquery
import os
from datetime import datetime
import pandas as pd
import json



# Get the credentials from the environment variable (using GH secrets)
credentials_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
credentials_info = json.loads(credentials_json)

# URL of the CSV file + path to save it
URL = "https://www.data.gouv.fr/fr/datasets/r/edd67f5b-46d0-4663-9de9-e5db1c880160"
CSV_FILE_PATH = 'daily_prices.csv'



# BigQuery configuration      (Update with your GCP project ID, dataset ID and table ID)
PROJECT_ID = 'trans-engine-356414'    # Update with your GCP project ID
DATASET_ID = 'fuel'    # Update with your dataset ID
TABLE_ID = 'daily_price'


# Download and read the CSV file
r = requests.get(URL)

with open(CSV_FILE_PATH, 'wb') as f:
    f.write(r.content)


# Read the df with Pandas and then ceate a csv (was needed because of an error reading columns with french accents)
df = pd.read_csv(CSV_FILE_PATH, sep = ';')

df.columns = ["station_id", "latitude", "longitude", "code_postal", "pop", "adresse", "ville", "services", "prix", "rupture",
              "horaires", "geom", "prix_gazole_updated", "prix_gazole", "prix_sp95_updated", "prix_sp95",
              "prix_e85_updated", "prix_e85", "prix_gplc_updated", "prix_gplc", "prix_e10_updated", "prix_ep10",
              "prix_sp98_updated", "prix_sp98", "debut_rupture_e10", "type_rupture_e10",
              "debut_rupture_sp98", "type_rupture_sp98", "debut_rupture_sp95", "type_rupture_sp95",
              "debut_rupture_e85", "type_rupture_e85", "debut_rupture_glpc", "type_rupture_glpc",
              "debut_rupture_gazole", "type_rupture_gazole", 'carburants_dispos','carburants_indispos',
              'carburants_rupture_tempo', 'carburants_rupture_def', 'automate_24', 'services_propos', 'departement',
              'code_depart', 'region', 'code_region', 'horaires_detail']


df.to_csv(CSV_FILE_PATH, index=False)



# Upload to BigQuery
client = bigquery.Client.from_service_account_info(credentials_info)
table_ref = client.dataset(DATASET_ID).table(TABLE_ID)



# Configure load job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    field_delimiter=',',
    skip_leading_rows=1,  # Adjust if your CSV doesn't have header
    autodetect=True,      # Automatically detect schema
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE   # to override the table by the new csv everyday
)


# Upload file to BQ
with open(CSV_FILE_PATH, 'rb') as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config
        )

job.result()
