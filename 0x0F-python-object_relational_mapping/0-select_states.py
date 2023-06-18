#!/usr/bin/python3
"""
select states from db
Usage: ./0-select_states.py user pass db
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    result = cur.fetchall()
    for res in result:
        print(res)
