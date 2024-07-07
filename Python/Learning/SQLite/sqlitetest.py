import sqlite3

# Step 2: Connect to the SQLite3 database
# If the database file does not exist, it will be created
conn = sqlite3.connect('example.db')

# Step 3: Create a cursor object
cur = conn.cursor()

# Step 4: Execute SQL commands
# For example, creating a table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Inserting data into the table
cur.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cur.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Suraj', 34))

# Fetching data from the table
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

# Step 5: Commit the changes (if any write operation was performed)
conn.commit()

# Step 6: Close the connection
conn.close()