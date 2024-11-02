#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, this one is safe from MySQL injections !
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for state in cursor.fetchall():
        if str(state[1]) == sys.argv[4]:
            print(state)
    cursor.close()
    db.close()
