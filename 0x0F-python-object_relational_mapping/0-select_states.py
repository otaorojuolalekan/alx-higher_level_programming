#!/usr/bin/python3
"""
select states from db
"""
import sys
import MySQLdb

def main():
    """
    main function to ensure it doesn't
    run on import"""

    db=MySQLdb.connect(user=sys.argv[1],
                       passwd=sys.argv[2],
                       database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    result = cur.fetchall()
    for res in result:
        print(res)

if __name__ == '__main__':
    main()