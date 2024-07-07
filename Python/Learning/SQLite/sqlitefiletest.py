import sqlite3

# Step 1: Read the SQL file
with open('example.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Step 2: Connect to the SQLite3 database
conn = sqlite3.connect('examplefile.db')

# Step 3: Create a cursor object
cur = conn.cursor()

# Step 4: Execute the SQL commands
cur.executescript(sql_script)

# Step 5: Commit the changes (if any write operation was performed)
conn.commit()

# Fetching data from the table
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

# Step 6: Close the connection
conn.close()
