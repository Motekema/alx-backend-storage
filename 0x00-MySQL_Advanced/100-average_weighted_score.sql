-- Stored procedure to compute and store the average weighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE weighted_avg_score FLOAT;
    
    -- Initialize variables
    SET total_weighted_score = 0;
    SET total_weight = 0;

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
END//

DELIMITER ;
