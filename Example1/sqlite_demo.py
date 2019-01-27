#! python
#
# Python SQLite Tutorial: Complete Oververview - Creating a Database, Table and
# Running [YouTube video]
# Corey Schafer [YouTube channel]
# I do not claim this work as my own so much as what I did while following
# along with the video I watched (see reference above).  This recreation is for
# my own reference purposes and may contain slight variations not depicted in
# the original video.
# sqlite3 is in the standard library
import sqlite3
# local import
from employee import Employee


# Create a connection to our database
# Note, you can specify a database or specify an "in memory" database by using
# the line below
# If the db doesn't exist, sqlite3 module will create it for you in the
# directory that this script is run from
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('employee.db')

# Create a cursor.  The cursor is what allows you to actually manipulate the
# database (I.e. add tables, data, etc.).
c = conn.cursor()

# We can now run commands with the cursor.  For the purposes of this demo,
# we'll be creating an employee table for the employee databse.
# Note, the use of docstring (3 double-quotes) is per python documentation
# convention and not strictly necessary. This simply allows for the use of a
# multi-line string without the use of special characters.  Additionally, using
# caps (CAPS) for SQL commands is convention as well
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")

# Manually adding data to the database
# c.execute("INSERT INTO employees VALUES ('Jean', 'Doe', 70000)")
# conn.commit()

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# The command below is one way to prevent sql injection attacks, it uses ?
# instead of string formatting ("{}".format(<replacemnet_var>)).
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last,
#                                                      emp_1.pay))

# A different way to do proper placeholders for inserting variables into db
# query statement
# c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# Query database - this will produce an object that we can itterate through
c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))

# This will get the next row in our results and if there are none it will
# return none
# c.fetchone()
# This will return up to however many records you put in as an argument as a
# list, can return an empty list
# c.fetchmany(<num>)
# Get all remaining rows - if there are none it will be an empty list
# c.fetchall()
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

print(c.fetchall())

# This will commit any transaction that happened to the database
conn.commit()

# It's important to close the connection to the database when finished
conn.close()

################
# FOOTER NOTES #
################
# 1. SQLite datatypes:
#   Null:  The value is a NULL value
#   Integer:  The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8
#             bytes depending on the magnitude of the value
#   Real:  The value is a floating point value, stored as an 8-byte IEEE
#          floating point value
#   Text:  The value is a text string, stored using the database encoding
#          (UTF-8, UTF-16BE, or UTF-16LE)
#   Blog:  The value is a blob of data, stored exactly as it was input
# 2. Attempting to create a table after it already exists will cause an error
#    to be thrown (sqlite3.OperationalError: table <table_name> already exists)
