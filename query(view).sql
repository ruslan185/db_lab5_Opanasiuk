-- Кількість команд в якій перебував кожен гравець
create view CommandsByPlayer as
select player_name, count(team_id) as total
from playersinteams
left outer join player on playersinteams.player_id = player.player_id
group by player_name;

-- Частка трьохочкових кожного гравця
create view ThreePointPercentage as
select player_name, three_points_goals
from playerstats
left outer join player on player.player_id = playerstats.player_id;

-- Загальна кількість зароблених очок кожного гравця
create view PlayerTotalPoints as
select player_name, total_points
from playerstats
left outer join player on player.player_id = playerstats.player_id;
