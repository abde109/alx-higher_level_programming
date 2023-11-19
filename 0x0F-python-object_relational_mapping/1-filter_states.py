#!/usr/bin/python3
"""
list all states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS LIKE 'N%';")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
