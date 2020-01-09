# Notifier
Example console application for logging notifications from postgresql database.

## Environment specifications
   * OS: Ubuntu 18.04.3 LTS (WSL)
   * Database: PostgreSQL 11.6
   * Python version: Python 3.7

## Additional details
   * Virtual environment: conda 4.7.12

### To run script
1. clone the repository `git clone https://github.com/freeman1992/postgres-notify-logger.git`
2. go to directory `cd postgres-notify-logger`
3. create a virtual environemt or not `conda create -n notifier python=3.7`
4. enter virtual environment `conda activate notifier` 
5. install psycopg2 library `pip install psycopg2`
6. install pgpubsub library `pip install pgpubsub`
7. edit configuration file accroding to your database `vim settings.ini`
8. create default table on database `python notifier.py --create`
9. insert new entry into the default database table `python notifier.py --insert`
10. keep the script running, you should see "Listening..." in stdout and YYYY-MM-DD_LOG.log is created 
    `python notifier.py`
11. enter to web or any other postgres database client
12. go to your database which you specified in settings.ini
13. change the value for `status` column in newly created row
14. you should see the output in newly created file YYYY-MM-DD_LOG.log


#### Help for optional arguments
    * --table (You can always specify table name to execute script functions on to specific table on target database)
    * --create $NAME (NAME argument is optional and it does specify the name of table to create on target database)
    * --insert (Inserts a new row into database table)

