import pandas as pd
import psycopg2

def gather_data():
    conn = psycopg2.connect(dbname='tests',
                            user='candidate5611',
                            password='#PASSWORD GOES HERE#',
                            host='#AWS HOST SERVER#',
                            port='5432')
    pd.set_option('display.max_columns', None)
    c = conn.cursor()

    c.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'cases'""")
    pre = c.fetchall()
    tables = [i for sub in pre for i in sub]
    print(tables)

    for table in tables:
        print(table)
        df = pd.read_sql_query("select * from cases.{};".format(table), conn)
        df.to_csv("C:/Users/dande/Desktop/{}.csv".format(table))
