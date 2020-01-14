import psycopg2
import uuid
import random
import string

###################################################################
#
# tool to inspect/check the generated table data for performance testing in PostgressSQL
#
###################################################################

def randString(stringLength):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=stringLength))
    return res

try:
    connection = psycopg2.connect(user="evo",
                                  password="Pwd1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="perftesting")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from citizen limit 10"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("NIN = ", row[0], )
        print("NAME = ", row[1])
        print("BENEFITS = ", row[2])
        print("ADDRESS = ", row[3])
        print("BALANCE = ", row[4])
        print("ACC_NAME  = ", row[5], "\n")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to select records from table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")