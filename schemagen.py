# conda install -c anaconda psycopg2
import psycopg2

#create the db schema for spark rdbms performance testing

conn = psycopg2.connect(user="sysadmin",
                              password="pynative@#29",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres_db")



#############################################


""" create tables in the PostgreSQL database"""
commands = (
    """
    CREATE TABLE CITIZEN (
            NIN INTEGER,
            NAME VARCHAR(300),
            BENEFITS INTEGER,
            ADDRESS VARCHAR(300),
            BALANCE double precision,
            ACC_NAME VARCHAR(300)
    )
    """,
    """
    CREATE TABLE TEST (
            id INTEGER PRIMARY KEY,
            pid INTEGER NOT NULL,

    )
    """)

try:
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)

    # commit the changes
    conn.commit()

    #############################################

    postgres_insert_query = """ INSERT INTO CITIZEN (NIN, NAME, BENEFITS, ADDRESS, BALANCE, ACC_NAME) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (5, 'asdasd', 950, 'assdad',0.34324,'asdsad')
    cur.execute(postgres_insert_query, record_to_insert)

    cur.execute("""SELECT * from CITIZEN""")
    rows = cur.fetchall()

    # Print out the results
    for row in rows:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

