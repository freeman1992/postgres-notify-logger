# Notifier
Example console application for logging notifications from postgresql database.

## Environment specifications
   * OS: Ubuntu 18.04.3 LTS (WSL)
   * Database: PostgreSQL 11.6
   * Python version: Python 3.7

## Additional details
   * Virtual environment: conda 4.7.12
   
## Download and Installation

To begin working with this script, make sure you have installed and running postgres server and setup a database.
* Clone the repo: `git clone https://github.com/freeman1992/postgres-notify-logger.git`


### To run script
1. go to directory `cd postgres-notify-logger`
2. create a virtual environemt or not `conda create -n notifier python=3.7`
3. enter virtual environment `conda activate notifier` 
4. install psycopg2 library `pip install psycopg2`
5. install pgpubsub library `pip install pgpubsub`
6. edit configuration file accroding to your database `vim settings.ini`
7. create default table on database `python notifier.py --create`
8. insert new entry into the default database table `python notifier.py --insert`
9. start the script, you should see "Listening..." in stdout and YYYY-MM-DD_LOG.log file is created within the directory
    `python notifier.py`
10. enter to web or any other postgres database client (pgadmin4) `http://127.0.0.1/pgadmin4/browser/`
11. go to your database which you specified in settings.ini
12. change the value for `status` column in newly created row
13. you should see the output in newly created file YYYY-MM-DD_LOG.log


#### Help for optional arguments
    * --table (You can always specify table name to execute script functions on to specific table on target database)
    * --create $NAME (NAME argument is optional and it does specify the name of table to create on target database)
    * --insert (Inserts a new row into database table)

