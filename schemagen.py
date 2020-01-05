# conda install -c anaconda psycopg2
import psycopg2

#create the db schema for spark rdbms performance testing

conn = psycopg2.connect(
    "db_name",
    "host_name",
    "username",
    "password")



#############################################


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE CITIZEN (
                NIN INTEGER,
                NAME VARCHAR(124),
                BENEFITS INTEGER,
                ADDRESS VARCHAR(124),
                BALANCE DOUBLE,
                ACC_NAME VARCHAR(124)
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
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()


#############################################

cur = conn.cursor()
cur.execute("""SELECT * from cit""")
rows = cur.fetchall()

# Print out the results
for row in rows:
    print(row)

# Close the connection when finished
conn.close()