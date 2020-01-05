import psycopg2

#create the db schema for spark rdbms performance testing

conn = psycopg2.connect(
    "db_name",
    "host_name",
    "username",
    "password")

cur = conn.cursor()
cur.execute("""SELECT * from cit""")
rows = cur.fetchall()

# Print out the results
for row in rows:
    print(row)

# Close the connection when finished
conn.close()