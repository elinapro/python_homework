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
    print(df[:5])

    #total column
    df['total'] = df['quantity'] * df['price'].)
    print(df[:5])

    #group_by product_id
    summary_df = df.groupby('product_id').agg(
    line_item_count=pd.NamedAgg(column='line_item_id', aggfunc='count'),
    total_paid=pd.NamedAgg(column='total', aggfunc='sum'),
    product_name=pd.NamedAgg(column='product_name', aggfunc='first')
).reset_index()
    
    #sort by product name
    summary_df = summary_df.sort_values(by='product_name')

    #adding to order_summary.csv

print("\nGrouped and Sorted Summary Data:")
print(summary_df.head())