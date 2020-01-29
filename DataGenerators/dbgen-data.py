import psycopg2
import uuid
import random
import string

###################################################################
#
# tool to generate table data for performance testing in PostgressSQL
# can be run on multiple threads (from e.g. multiple terminal windows) and
# each with different ranges for the primary key
#
###################################################################

def randString(stringLength):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=stringLength))
    return res

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

    postgres_delete_query = """DELETE FROM CITIZEN"""
    cursor.execute(postgres_delete_query)

    postgres_insert_query = """ INSERT INTO CITIZEN (NIN, NAME, BENEFITS, ADDRESS, BALANCE, ACC_NAME) VALUES (%s,%s,%s,%s,%s,%s)"""

    # To Do: implement optimization by inserting batches of records at once, rather than individual records
    for nin in range(0, 30):
        record_to_insert = (nin, str(uuid.uuid4()), random.random(), randString(10), random.random(), randString(20))
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    #print (count, "Record inserted successfully into mobile table")
    print(nin+1, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")