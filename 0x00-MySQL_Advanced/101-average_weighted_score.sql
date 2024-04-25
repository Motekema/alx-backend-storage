-- Stored procedure to compute and store the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE user_id INT;
    DECLARE weighted_avg_score FLOAT;
    
    -- Declare cursor for iterating over users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    
    -- Initialize variables
    SET total_weighted_score = 0;
    SET total_weight = 0;

    -- Open cursor
    OPEN user_cursor;
    
    -- Loop through users
    user_loop: LOOP
        -- Fetch user_id from cursor
        FETCH user_cursor INTO user_id;
        
        -- Check if cursor is empty
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Calculate total weighted score for the user
        SELECT SUM(projects.weight * corrections.score) INTO total_weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate total weight
        SELECT SUM(weight) INTO total_weight FROM projects;

        -- Calculate weighted average score
        IF total_weight > 0 THEN
            SET weighted_avg_score = total_weighted_score / total_weight;
        ELSE
            SET weighted_avg_score = 0;
        END IF;

        -- Update the users table with the computed average weighted score
        UPDATE users SET average_score = weighted_avg_score WHERE id = user_id;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
    
END//

DELIMITER ;
