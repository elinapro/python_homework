import os
import sqlite3

# Function to add data


def add_publishers(cursor, id, name):
    try:
        cursor.execute(
            "INSERT INTO publishers (publisher_id, publisher_name) VALUES (?, ?)", (id, name))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_magazines(cursor, id, name, pid):
    try:
        cursor.execute(
            "INSERT INTO magazines (magazine_id, magazine_name, publisher_id) VALUES (?, ?, ?)", (id, name, pid))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_subscribers(cursor, id, name, address):
    try:
        cursor.execute(
            "INSERT INTO subscribers (subscriber_id, subscriber_name, subscriber_address) VALUES (?, ?, ?)", (id, name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_subscriptions(cursor, id, date, sid, mid):
    try:
        cursor.execute(
            "INSERT INTO subscriptions (subscription_id, expiration_date, subscriber_id, magazine_id) VALUES (?, ?, ?, ?)", (id, date, sid, mid))
    except sqlite3.IntegrityError:
        print(f"Subscription ID {id} is already in the database.")


# Connect to database
with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL UNIQUE,
        subscriber_address TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        expiration_date TEXT,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
        UNIQUE (subscriber_id, magazine_id)
    )
    """)

    # Insert data
    add_publishers(cursor, 10, 'Swan Books')
    add_publishers(cursor, 20, 'Harrys Way')
    add_publishers(cursor, 30, 'Who Dunnit')
    add_publishers(cursor, 40, 'Who Are You')
    add_magazines(cursor, 1, "People", 10)
    add_magazines(cursor, 2, "Bride", 20)
    add_magazines(cursor, 3, "Celebrity", 30)
    add_magazines(cursor, 4, "Hello Sunshine", 40)
    add_subscribers(cursor, 101, "Molly Moon", "550 Keynote Drive")
    add_subscribers(cursor, 102, "Henry Bet", "60 Balloon Drive")
    add_subscribers(cursor, 103, "Bettie Ray", "70 Hockey Ave")
    add_subscriptions(cursor, 1, 2027, 101, 1)
    add_subscriptions(cursor, 2, 2028, 102, 2)
    add_subscriptions(cursor, 3, 2029, 103, 3)

    conn.commit()
    print("Tables created and sample data inserted successfully.")


# SQL statements
# Write a query to retrieve all information from the subscribers table.

cursor.execute("SELECT * FROM subscribers")
result = cursor.fetchall()
for row in result:
    print(row)

# Write a query to retrieve all magazines sorted by name.
cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
result = cursor.fetchall()
for row in result:
    print(row)

# Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
cursor.execute(
    "SELECT m.* FROM magazines m JOIN publishers p ON m.publisher_id = p.publisher_id WHERE p.publisher_name = 'Who Dunnit'")
result = cursor.fetchall()
for row in result:
    magazine_id, magazine_name, publisher_name = row
    print(
        f"ID: {magazine_id}, Magazine: {magazine_name}, Publisher: {publisher_name}")
