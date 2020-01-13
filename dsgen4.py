import psycopg2
from psycopg2 import Error

###################################################################
#
# tool to create the schema for performance testing in PostgressSQL
#
###################################################################

try:
    connection = psycopg2.connect(user="evo",
                                  password="Pwd1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="perftesting")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    #create_table_query = '''DROP TABLE IF EXISTS CITIZEN; '''

    create_table_query = '''CREATE TABLE IF NOT EXISTS CITIZEN
          (NIN INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          BENEFITS         REAL); '''

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