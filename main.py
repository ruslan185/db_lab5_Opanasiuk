import psycopg2
import matplotlib.pyplot as plt

username = 'Ruslan'
password = '123'
database = 'lab_BD'
host = 'localhost'
port = '5432'

query_1 = '''
select *
from CommandsByPlayer;
'''

query_2 = '''
select *
from ThreePointPercentage;
'''

query_3 = '''
select *
from PlayerTotalPoints;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()
    figure, (bar_ax, pie_ax, bar2_ax) = plt.subplots(1, 3)

##########################
    cur.execute(query_1)
    x1 = []
    y1 = []

    for row in cur:
        x1.append(row[0])
        y1.append(row[1])

    x_range = range(len(x1))
    
    bar_ax.bar(x_range, y1, label='Total')
    bar_ax.set_title('Кількість команд в якій перебував кожен гравець')
    bar_ax.set_xlabel('Гравці')
    bar_ax.set_ylabel('Кількість команд')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(x1, rotation='vertical')

##########################
    cur.execute(query_2)
    x2 = []
    y2 = []

    for row in cur:
        x2.append(row[0])
        y2.append(row[1])

    pie_ax.pie(y2, labels=x2, autopct='%1.1f%%')
    pie_ax.set_title('Частка трьохочкових кожного гравця')
##########################
    cur.execute(query_3)
    x3 = []
    y3 = []
  
    for row in cur:
        x3.append(row[0])
        y3.append(row[1])

    x_range = range(len(x3))
    
    bar2_ax.bar(x_range, y3, label='Total')
    bar2_ax.set_title('Загальна кількість зароблених очок кожного гравця')
    bar2_ax.set_xlabel('Гравці')
    bar2_ax.set_ylabel('Очки')
    bar2_ax.set_xticks(x_range)
    bar2_ax.set_xticklabels(x3, rotation='vertical')


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
