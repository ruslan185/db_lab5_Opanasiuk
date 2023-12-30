import csv
import psycopg2

username = 'Ruslan'
password = '123'
database = 'lab5_DB'
host = 'localhost'
port = '5432'
output_file = 'nba_DB_{}.csv'

tables = [
    'Team',
    'Player',
    'PlayerStats',
    'PlayersInTeams',
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in tables:
        cur.execute(f'select * FROM {table_name}')
        fieldnames = [x[0] for x in cur.description]
        with open(output_file.format(table_name), 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for row in cur:
                writer.writerow(row)