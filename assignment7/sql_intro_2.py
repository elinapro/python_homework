import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT
        li.line_item_id,
        li.quantity,
        li.product_id,
        p.product_name,
        p.price
    FROM line_items li
    JOIN products p ON line_items.product_id = products.product_id
    """

df = pd.read_sql_query(sql_statement, conn)

# print the first 5 rows
print(df.head())

# 4 add a column to the dataframe- total column

df['total'] = df['quantity'] * df['price']
print(df[:5])

# 5 Add groupby() code to group by the product_id

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

print(summary(head))

# 6 Sort the DataFrame by the product_name column.
summary = summary.sort_values(by='product_name')

# 7 write to CSV
summary.to_csv("order_summary.csv", index=False)


#     # adding to order_summary.csv

# print("\nGrouped and Sorted Summary Data:")
# print(summary_df.head())
