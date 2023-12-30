-- Кількість команд в якій перебував кожен гравець
select player_name, count(team_id) as total
from playersinteams
left outer join player on playersinteams.player_id = player.player_id
group by player_name;

-- Частка трьохочкових кожного гравця
select player_name, three_points_goals
from playerstats
left outer join player on player.player_id = playerstats.player_id;

-- Загальна кількість зароблених очок кожного гравця
select player_name, total_points
from playerstats
left outer join player on player.player_id = playerstats.player_id;
