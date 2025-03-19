# Project Context
Automate the downloading of a CSV from a URL, then clean and upload it to BigQuery.

We use GitHub Actions to schedule the Python

## Requirements

- Create a service account and give it the role "BigQueryAdmin"


- Use GitHub Secrets to store your service account json keys as an environment variable.
  In "data_pipeline.yml", it creates an environment variable "GOOGLE_APPLICATION_CREDENTIALS"
  from the GH secret 'GCP_CREDENTIALS_JSON'


- Create your own BQ table

- Update BigQuery info in ***script.py*** (project, dataset...) by putting your own configs


- (optional) Install dependencies from requirements.txt if you want to test code locally
  (command in README.md)


____________________________________

# Guide GitHub Actions

## Key Concepts


- ***Workflows***: Automated processes defined in YAML files located in the .github/workflows directory.


- ***Jobs***: A workflow is made up of one or more jobs, which run in parallel by default.


- ***Steps***: Each job consists of a sequence of steps. Steps can run commands or use actions.


- ***Actions***: Reusable units of code that can be shared and used in workflows.


## Steps to create an Action

1) Create a Repository

2) Create the workflow file
  - In your repository, create a directory named .github/workflows.
  - Inside this directory, create a YAML file (e.g., actions.yml).


3) define the workflow


- ***events*** : Specify when the workflow should run. Common events include push, pull_request, schedule, and workflow_dispatch

```
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'  # Runs daily at midnight UTC

```

- ***Jobs*** : Define the jobs in your workflow. Each job runs on a specified runner.
