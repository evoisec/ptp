# conda install -c anaconda psycopg2
import psycopg2

#create the db schema for spark rdbms performance testing

conn = psycopg2.connect(
    "db_name",
    "host_name",
    "username",
    "password")



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

    sql = """INSERT INTO CITIZENS(NIN) VALUES(%i)"""
    cur.execute(sql, (223,))
    conn.commit()

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

