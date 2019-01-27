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


# Create an "in-memory" database and establish a connection
conn = sqlite3.connect(':memory:')

# Create a cursor.  The cursor is what allows you to actually manipulate the
# database (I.e. add tables, data, etc.).
c = conn.cursor()

# Create a table in the db
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


# Function for inserting an employee into the database
def insert_emp(emp):
    # Using a context manager, we'll insert the new employee into the database.
    # This practice prevents us from having to worry about managing a cursor.
    # If all goes well with the transaction, the data will be written and
    # committed.  If the transaction fails, the data will be rolled back to a
    # point before the add.
    with conn:
        c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
        WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE first = :first
                     AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


# Use the employee class to create data
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)

remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

# It's important to close the connection to the database when finished
conn.close()
