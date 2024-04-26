'''
  This is the config file which includes all ccnfiguation info here
'''

import os

_DB_CONF = {
 'host': os.getenv('DB_HOST', 'student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com'),
 'port': int(os.getenv('DB_PORT', 3306)),
 'user': os.getenv('DB_USER', 'admin'),
 'passwd': os.getenv('DB_PASSWORD', 'Tosvert123#'),
 'db': os.getenv('DB_NAME', 'student')
}

