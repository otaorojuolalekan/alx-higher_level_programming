#!/usr/bin/env python3
"""
select states from db
"""
def main():
    """
    main function to ensure it doesn't
    run on import"""
    import sys
    import MySQLdb
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