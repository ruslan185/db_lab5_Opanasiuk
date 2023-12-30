import psycopg2
import matplotlib.pyplot as plt

username = 'Ruslan'
password = '123'
database = 'lab_BD'
host = 'localhost'
port = '5432'

query_1 = '''
select player_name, count(team_id) as total
from playersinteams
left outer join player on playersinteams.player_id = player.player_id
group by player_name;
'''

query_2 = '''
select player_name, three_points_goals
from playerstats
left outer join player on player.player_id = playerstats.player_id;
'''

query_3 = '''
select player_name, total_points
from playerstats
left outer join player on player.player_id = playerstats.player_id;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

##########################
    print("Кількість команд в якій перебував кожен гравець")
    cur.execute(query_1)
    for row in cur.fetchall():
        print(row)

##########################
    print("\nЧастка трьохочкових кожного гравця")
    cur.execute(query_2)
    for row in cur.fetchall():
        print(row)

##########################
    print("\nЗагальна кількість зароблених очок кожного гравця")
    cur.execute(query_3)
    for row in cur.fetchall():
        print(row)



