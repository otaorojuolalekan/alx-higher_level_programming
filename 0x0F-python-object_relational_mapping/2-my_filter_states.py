#!/usr/bin/python3
"""
select states from db
Usage: ./0-select_states.py user pass

"""
import sys
import MySQLdb


def main():
    """
    main function to ensure it doesn't
    run on import"""

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}'\
                ORDER BY id ASC".format(sys.argv[4]))
    result = cur.fetchall()
    for res in result:
        print(res)


if __name__ == '__main__':
    main()
