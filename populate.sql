insert into Team (team_name,team_id)
values
	('Cleveland Cavaliers', 1),
	('Miami Heat', 2),
	('Milwaukee Bucks', 3),
	('Los Angeles Lakers', 4),
	('Utah Jazz', 5),
	('Chicago Bulls', 6),
	('Washington Wizards', 7);

insert into Player (player_id, player_name, pos)
values
	(1, 'LeBron James', 'SF'),
	(2, 'Kareem Abdul-Jabbar', 'C'),
	(3, 'Karl Malone', 'PF'),
	(4, 'Kobe Bryant', 'SG'),
	(5, 'Michael Jordan', 'SG');

insert into PlayerStats (rank_id,total_points,total_games,points_per_game,three_points_goals,free_shots,field_goals,player_id)
values
	(1, 39201, 1443, 27.2, 2311, 8178, 14356, 1),
	(2, 38387, 1560, 24.6, 1, 6712, 15828, 2),
	(3, 36928, 1476, 25, 85, 9787, 13528, 3),
	(4, 33643, 1346, 25, 1827, 8378, 11719, 4),
	(5, 32292, 1072, 30.1, 581, 7327, 12192, 5);

insert into PlayersInTeams (player_id, team_id)
values
	(1, 1),
	(1, 2),
	(1, 4),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 4),
	(4, 4),
	(5, 6),
	(5, 7);