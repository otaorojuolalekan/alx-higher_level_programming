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

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT c.name, s.name FROM cities c\
                LEFT JOIN states s on c.state_id = s.id\
                ORDER BY c.id ASC"
    state_input = (sys.argv[4])
    cur.execute(query)
    result = cur.fetchall()
    # create an empty list to store results
    res_list = []
    for res in result:
        if res[1] == state_input:
            res_list.append(res[0])
    print(', '.join(res_list))


if __name__ == '__main__':
    main()
