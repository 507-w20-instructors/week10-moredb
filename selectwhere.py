


'''
    Instructions: Write a short program that will print 
    out the 10 products that are least well-stocked, in 
    order from least to most well stocked, with output 
    of the form

    `We have <N> units of <Product name> in stock, and <M> units on order.`

'''


import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

q1 = '''
SELECT FirstName, LastName
FROM Employee
WHERE Title <> "Sales Managers"
'''

q2 = '''
SELECT ProductName
FROM Product
WHERE UnitsOnOrder >=50
'''

q3 = '''
SELECT FirstName
FROM Employee
WHERE BirthDate BETWEEN "1980_01_01" AND "1989_12_31"
'''

q4 = '''
SELECT FirstName
FROM Employee
WHERE BirthDate LIKE "198%"
'''

q5 = '''
SELECT CompanyName
FROM Customer
WHERE (Country = "Sweden" OR Country = "Finland")
'''
q6 = '''
SELECT CompanyName
FROM Customer
WHERE Country IN ("Sweden", "Finland")
'''

for q in [q1, q2, q3, q4, q5, q6]:
    cur.execute(q)  
    for row in cur:
        print(row)
    print('-' * 60)
conn.close()