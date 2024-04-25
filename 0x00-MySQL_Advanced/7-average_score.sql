DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_total_score INT;
    DECLARE v_total_projects INT;
    DECLARE v_average_score FLOAT;

    -- Calculate total score for the user
    SELECT SUM(score) INTO v_total_score FROM corrections WHERE user_id = p_user_id;

    -- Calculate total number of projects for the user
    SELECT COUNT(DISTINCT project_id) INTO v_total_projects FROM corrections WHERE user_id = p_user_id;

    -- Calculate average score
    IF v_total_projects > 0 THEN
        SET v_average_score = v_total_score / v_total_projects;
    ELSE
        SET v_average_score = 0;
    END IF;

    -- Update average score for the user
    UPDATE users SET average_score = v_average_score WHERE id = p_user_id;
END//

DELIMITER ;
