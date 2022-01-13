import psycopg2

# test whether the tables are created
def create_test():
    """
    - Checks whether the tables are created
    """

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=YourUser password=YourPassword")
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("SELECT * FROM songplays LIMIT 5;")

    # close connection to sparkify database
    conn.close()

# run the function
create_test()