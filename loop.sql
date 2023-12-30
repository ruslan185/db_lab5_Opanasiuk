-- create table playerstatscopy as select * from playerstats

-- DO $$
-- DECLARE
--     rank_id_val INT := 6;
--     player_id_val INT := 6;
--     total_points_val INT;
--     total_games_val INT;
--     points_per_game_val INT;
--     three_points_goals_val INT;
--     free_shots_val INT;
--     field_goals_val INT;
-- BEGIN
--     WHILE rank_id_val < 100 LOOP
--         total_points_val := FLOOR(RANDOM() * (39200 - 20000 + 1)) + 20000;
--         total_games_val := FLOOR(RANDOM() * (1611 - 791 + 1)) + 791;
--         points_per_game_val := FLOOR(RANDOM() * (30.1 - 14.5 + 1)) + 14.5;
--         three_points_goals_val := FLOOR(RANDOM() * (3492 + 1));
--         free_shots_val := FLOOR(RANDOM() * (9787 - 2783 + 1)) + 2783;
--         field_goals_val := FLOOR(RANDOM() * (15800 - 7305 + 1)) + 7305;

--         INSERT INTO playerstatscopy(rank_id, total_points, total_games, points_per_game, three_points_goals, free_shots, field_goals, player_id)
--         VALUES (rank_id_val, total_points_val, total_games_val, points_per_game_val, three_points_goals_val, free_shots_val, field_goals_val, player_id_val);

--         rank_id_val := rank_id_val + 1;
--         player_id_val := player_id_val + 1;
--     END LOOP;
-- END $$;

select *
from playerstatscopy;
