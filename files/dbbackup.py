#!/usr/bin/python

import os
import time
import datetime

# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'SenhaDoRoot!!!'
#DB_NAME = '/backup/dbnames.txt'
DB_NAME = 'wordpress'
BACKUP_PATH = '/backup/'

# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%m%d%Y-%H%M%S')

db = DB_NAME
dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + BACKUP_PATH + db + "_" + DATETIME + ".sql"
os.system(dumpcmd)

print "Backup script completed"
print "Your backups has been created in '" + BACKUP_PATH + "' directory"
