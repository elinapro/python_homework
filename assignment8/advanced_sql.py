import os
import sqlite3

# Connect to a new SQLite database
# Create the file here, so that it is not pushed to GitHub!
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")

# Task 1
cursor.execute("""
SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5
""")
result = cursor.fetchall()
for row in result:
    print(row)

# Task 2
cursor.execute("""
SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) sub ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id
""")
result = cursor.fetchall()
for row in result:
    print(row)

# Task 3

cursor.execute(
    "SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
row = cursor.fetchone()
if row is None:
    print("Customer not found")
    conn.close()
    exit(1)
customer_id = row[0]

cursor.execute(
    "SELECT employee_id FROM employees WHERE first_name = 'Miranda' and last_name = 'Harris'")
row = cursor.fetchone()
if row is None:
    print("Employee not found")
    conn.close()
    exit(1)
employee_id = row[0]

# 5 lease expensive products
cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
rows = cursor.fetchall()
if not rows:
    print("No products found.")
    conn.close()
    exit(1)
product_ids = [row[0] for row in rows]

conn.execute("BEGIN")

# inserting an order
cursor.execute("""
INSERT INTO orders (customer_id, employee_id, date)
VALUES (?, ?, DATE('now'))
RETURNING order_id     
""", (customer_id, employee_id))

row = cursor.fetchone()
if row is None:
    print("Order insert failed- no order_id returned")
    conn.rollback()
    conn.close()
    exit(1)
order_id = row[0]

# insert 5 line items
for product_id in product_ids:
    cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, ?)
    """, (order_id, product_id, 10))


conn.commit()

# printing the new lines
cursor.execute("""
SELECT li.line_item_id, li. quantity, p.product_name
FROM line_items li
JOIN products p ON li.product_id = p.product_id
WHERE li.order_id = ?   
""", (order_id,))
result = cursor.fetchall()
for row in result:
    print(row)


# Task 4
cursor.execute("""
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5
""")
result = cursor.fetchall()
for row in result:
    print(row)


conn.close()
