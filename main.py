import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
from google.cloud import bigquery


# Reading a csv using pandas
df = pd.read_csv('response.csv', delimiter=",")
#print(df)

# Sending the raw data to Google BigQuery table
# Note: Make sure that your bigquery credentials are on 'secrets.json' file
client = bigquery.Client.from_service_account_json('secrets.json')

project_id = "project_id"
destination_table = "project_id.dataset.table_name"
credentials = service_account.Credentials.from_service_account_file('secrets.json')

try:
  pandas_gbq.to_gbq(dataframe=df,
                    destination_table=destination_table,
                    project_id=project_id,
                    credentials=credentials,
                    if_exists="replace")# replacing table to a brand new one table
  print('Data has been sent to BigQuery')
except Exception as e:
  print(f'Error: {e}')
