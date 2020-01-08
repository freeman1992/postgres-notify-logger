# Notifier
Example console application for logging notifications from postgresql database.

## Environment specifications
   * OS: Ubuntu 18.04.3 LTS (WSL)
   * Database: PostgreSQL 11.6
   * Python version: Python 3.7

## Additional details
   * Virtual environment: conda 4.7.12

### Install required packages
    1. conda create -n notifier python=3.7
    2. conda activate notifier
    3. pip install psycopg2
    4. pip install pgpubsub

### To run script
    1. edit settings.ini
    2. run notifier.py --create
    3. run notifier.py --insert
    4. run notifier.py


#### Help for optional arguments
    * --table (You can always specify table name to execute script functions on to specific table on target database)
    * --create $NAME (NAME argument is optional and it does specify the name of table to create on target database)
    * --insert (Inserts a new row into database table)

