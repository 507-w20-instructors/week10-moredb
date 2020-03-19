'''

Write and test queries to get the following data:

- Return the number of customers in the North America Region
- Return the number of unique Titles held by Customers
- Return only the top 3 most heavily stocked Products (those with the largest UnitsInStock values)
'''

import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

q1 = '''
SELECT COUNT(*)
FROM Customer
WHERE Region="North America"
'''

q2 = '''
SELECT COUNT(DISTINCT ContactTitle)
FROM Customer
'''

q3 = '''
SELECT ProductName
FROM Product
ORDER BY UnitsInStock DESC
LIMIT 3
'''


for q in [q1, q2, q3]:
    cur.execute(q)  
    for row in cur:
        print(row)
    print('-' * 60)
conn.close()