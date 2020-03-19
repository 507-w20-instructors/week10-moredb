'''
Write and test queries to get the following data:

- Get the last names of all employees with a title of “Sales Representative”
- Get the CompanyName of all Suppliers in the “Eastern Asia” region.
- Get the names of all products with a CategoryId of 2.
'''

import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()


q1 = '''
SELECT LastName
FROM Employee
WHERE Title="Sales Representative"
'''

q2 = '''
SELECT CompanyName
FROM Supplier
WHERE Region="Eastern Asia"
'''

q3 = '''
SELECT ProductName
FROM Product
WHERE CategoryId=2
'''

for q in [q1, q2, q3]:
    cur.execute(q)  
    for row in cur:
        print(row)
    print('-' * 60)
conn.close()