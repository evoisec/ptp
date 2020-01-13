import psycopg2
from psycopg2 import Error

###################################################################
#
# tool to generate table data for performance testing in PostgressSQL
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

    postgres_insert_query = """ INSERT INTO CITIZEN (NIN, NAME, BENEFITS) VALUES (%s,%s,%s)"""

    for nin in range(0, 30):
        record_to_insert = (nin, 'John Evans', 950)
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    #print (count, "Record inserted successfully into mobile table")
    print(nin, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")