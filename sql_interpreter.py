import sqlite3

# Create connection to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()


# CREATE TABLE statement interpreter
def interpret_create_table(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print("Error:", e)


# ALTER TABLE statement interpreter
def interpret_alter_table(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Table altered successfully")
    except Exception as e:
        print("Error:", e)


# DROP TABLE statement interpreter
def interpret_drop_table(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Table dropped successfully")
    except Exception as e:
        print("Error:", e)


# SELECT statement interpreter
def interpret_select(query):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)


# INSERT statement interpreter
def interpret_insert(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Record inserted successfully")
    except Exception as e:
        print("Error:", e)


# UPDATE statement interpreter
def interpret_update(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Record updated successfully")
    except Exception as e:
        print("Error:", e)


# DELETE statement interpreter
def interpret_delete(query):
    try:
        cursor.execute(query)
        conn.commit()
        print("Record deleted successfully")
    except Exception as e:
        print("Error:", e)


# Prompt user for input queries
while True:
    query = input("Enter a SQL query (or 'quit' to exit): ")
    if query.lower() == 'quit':
        break

    # Determine query type and call appropriate interpreter
    query_type = query.split()[0].lower()
    if query_type == 'select':
        interpret_select(query)
    elif query_type == 'insert':
        interpret_insert(query)
    elif query_type == 'update':
        interpret_update(query)
    elif query_type == 'delete':
        interpret_delete(query)
    elif query_type == 'create':
        interpret_create_table(query)
    elif query_type == 'alter':
        interpret_alter_table(query)
    elif query_type == 'drop':
        interpret_drop_table(query)
    else:
        print("Invalid query type")

# Close connection to SQLite database
conn.close()
