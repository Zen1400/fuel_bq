# fuel_bq
Small project to automate downloading a csv daily and upload it to BigQuery

## Steps

- Create a service account and give it the role "BigQueryAdmin"



🕰️ Cron Jobs Crash Course
What is a Cron Job?
A Cron Job is a time-based job scheduler in Unix-like operating systems. It allows you to run commands or scripts at specified times and intervals.

Cron Syntax
A cron expression is a string consisting of five fields separated by spaces:

* * * * *
│ │ │ │ │
│ │ │ │ └── Day of the week (0 - 7) (Sunday is both 0 and 7)
│ │ │ └──── Month (1 - 12)
│ │ └────── Day of the month (1 - 31)
│ └──────── Hour (0 - 23)
└────────── Minute (0 - 59)
Common Examples
0 0 * * * - Every day at midnight
0 12 * * * - Every day at noon
0 18 * * 5 - Every Friday at 6 PM
*/15 * * * * - Every 15 minutes
Special Characters
* - Matches any value
, - Separates items of a list
- - Defines a range
/ - Specifies a step value
Example Cron Job
To run a script every day at 1 PM CET:

schedule:
  - cron: "0 12 * * *"
Useful Resources
Crontab Guru - An easy-to-use cron expression editor
GitHub Actions - Documentation for GitHub Actions
