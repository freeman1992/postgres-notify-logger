# Notifier
Example console application for logging notifications from postgresql database.

## Environment specifications
   * OS: Ubuntu 18.04.3 LTS (WSL)
   * Database: PostgreSQL 11.6
   * Python version: Python 3.7

## Additional details
   * Virtual environment: conda 4.7.12

### To run script
    1. git clone https://github.com/freeman1992/postgres-notify-logger.git
    2. cd postgres-notify-logger
    3. conda create -n notifier python=3.7 # creates virtual environment 
    4. conda activate notifier # activates virtual environment
    5. pip install psycopg2
    6. pip install pgpubsub
    7. vim settings.ini # edit configuration file accroding to your database
    8. python notifier.py --create
    9. python notifier.py --insert
    10. python notifier.py # keep the script running, you should see "Listening..." in stdout and YYYY-MM-DD_LOG.log is created
    11. enter to web or any other postgres database client
    12. go to your database which you specified in settings.ini
    13. change the value for `status` column in newly created row
    14. you should see the output in newly created file YYYY-MM-DD_LOG.log


#### Help for optional arguments
    * --table (You can always specify table name to execute script functions on to specific table on target database)
    * --create $NAME (NAME argument is optional and it does specify the name of table to create on target database)
    * --insert (Inserts a new row into database table)

