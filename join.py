'''
Write JOIN queries that will accomplish the following:

- Return the ProductName and CategoryName for all products in the category “Condiments”
- Return the TerritoryDescription for all Territories in the “Southern” region
'''

import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

q1 = '''
SELECT ProductName, CategoryName
FROM Product
	JOIN Category
		ON Product.CategoryId=Category.Id
WHERE CategoryName="Condiments"
'''

q2 = '''
SELECT TerritoryDescription
FROM Territory
	JOIN Region
		ON Territory.RegionId=Region.Id
WHERE Region.RegionDescription="Southern"
'''

q3 = '''
SELECT Employee.FirstName, Employee.LastName,  [Order].Id, [Order].OrderDate
FROM [Order]
	JOIN Employee
		ON [Order].EmployeeId = Employee.Id
WHERE Employee.LastName = "Peacock"
ORDER BY [Order].OrderDate DESC
LIMIT 10
'''


for q in [q1, q2, q3]:
    cur.execute(q)  
    for row in cur:
        print(row)
    print('-' * 60)
conn.close()