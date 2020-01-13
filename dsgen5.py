import psycopg2
import uuid
import random

###################################################################
#
# tool to generate table data for performance testing in PostgressSQL
# can be run on multiple threads (from e.g. multiple terminal windows) and
# each with different ranges for the primary key
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

    postgres_delete_query = """DELETE FROM CITIZEN"""
    cursor.execute(postgres_delete_query)

    postgres_insert_query = """ INSERT INTO CITIZEN (NIN, NAME, BENEFITS) VALUES (%s,%s,%s)"""

    #To Do: implement optimization by inserting batches of records at once, rather than individual records
    for nin in range(0, 30):
        record_to_insert = (nin, str(uuid.uuid4()), random.random())
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    #print (count, "Record inserted successfully into mobile table")
    print(nin+1, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")