import psycopg2
from psycopg2 import Error

###################################################################
#
# tool to create the schema for performance testing in PostgressSQL
#
###################################################################

Config = {}

f = open('db.cfg', 'r')
line = f.readline()
while (line != ""):
    line = line.rstrip()
    x = line.split('=')
    print(x[0])
    print(x[1])
    Config[x[0]] = x[1]
    line = f.readline()

try:
    connection = psycopg2.connect(user=Config['user'],
                                  password=Config['password'],
                                  host=Config['host'],
                                  port=Config['port'],
                                  database=Config['database'])

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    drop_table_query = '''DROP TABLE IF EXISTS CITIZEN; '''
    cursor.execute(drop_table_query)

    create_table_query = '''CREATE TABLE IF NOT EXISTS CITIZEN
          (NIN INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          BENEFITS       REAL,
          ADDRESS        TEXT    NOT NULL,
          BALANCE        REAL,
          ACC_NAME       TEXT    NOT NULL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")