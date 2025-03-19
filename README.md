# Project Context
Automate the downloading of a CSV from a URL, then clean and upload it to BigQuery.

We use GitHub Actions to schedule the Python

## Requirements

- Create a service account and give it the role "BigQueryAdmin"


- Use GitHub Secrets to store your service account json keys as an environment variable.
  In "data_pipeline.yml", it creates an environment variable "GOOGLE_APPLICATION_CREDENTIALS"
  from the GH secret 'GCP_CREDENTIALS_JSON'


- (optional) Install dependencies from requirements.txt if you want to test code locally         (command in README.md)
