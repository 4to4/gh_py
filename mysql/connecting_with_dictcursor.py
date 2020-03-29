import MySQLdb
import MySQLdb.cursors # do not forget this one

db = MySQLdb.connect(
                    user="root",
                    passwd="root",
                    host="localhost",
                    db="sakila",
                    cursorclass=MySQLdb.cursors.DictCursor
                    )

cursor = db.cursor()
cursor.execute("SELECT * from film_text where film_id > 100 and film_id < 150 limit 10,10")
data=cursor.fetchall()
# data=cursor.fetchone()

print(data)

for row in data:
    print("Row ", row)
    # for k,v in row.items():
    #     print (f"{k} => {v}")

db.close() # close db

#https://mysqlclient.readthedocs.io




#https://stackoverflow.com/questions/4960048/how-can-i-connect-to-mysql-in-python-3-on-windows
""" with pymysql 
import pymysql 

# Open database connection
db = pymysql.connect("localhost","root","root","sakila" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select * from film_text")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone() # to fetch one row
data = cursor.fetchall()
print(data[0])
print(f"Row count {cursor.rowcount}")

# disconnect from server
db.close()
"""


"""
There are currently a few options for using Python 3 with mysql:

https://pypi.python.org/pypi/mysql-connector-python

Officially supported by Oracle
Pure python
A little slow
Not compatible with MySQLdb
https://pypi.python.org/pypi/pymysql

Pure python
Faster than mysql-connector
Almost completely compatible with MySQLdb, after calling pymysql.install_as_MySQLdb()
https://pypi.python.org/pypi/cymysql

fork of pymysql with optional C speedups
https://pypi.python.org/pypi/mysqlclient

Django's recommended library.
Friendly fork of the original MySQLdb, hopes to merge back some day
The fastest implementation, as it is C based.
The most compatible with MySQLdb, as it is a fork
Debian and Ubuntu use it to provide both python-mysqldb andpython3-mysqldb packages.
benchmarks here: https://github.com/methane/mysql-driver-benchmarks
"""