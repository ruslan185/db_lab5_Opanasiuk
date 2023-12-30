import json
import psycopg2

username = 'Ruslan'
password = '123'
database = 'lab5_DB'
host = 'localhost'
port = '5432'

tables = [
    'Team',
    'Player',
    'PlayerStats',
    'PlayersInTeams',
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


data = {}
with conn:

    cur = conn.cursor()

    for table in tables:
        cur.execute('select * from ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('nba_DB.json', 'w') as outf:
    json.dump(data, outf, default = str)