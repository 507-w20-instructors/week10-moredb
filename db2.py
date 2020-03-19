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

query = '''
    SELECT ProductName, UnitsInStock, UnitsOnOrder
    FROM Product
    ORDER BY UnitsInStock 
    LIMIT 10
'''
cur.execute(query)

for row in cur:
    print(f'We have {row[1]} units of {row[0]}, and {row[2]} on order.')

conn.close()