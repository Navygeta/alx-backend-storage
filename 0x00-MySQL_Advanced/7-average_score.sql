-- Procedure ComputeAverageScoreForUser computes and stores the average score for a student.
-- Takes 1 input user_id, a users.id
-- Context: Writing code in SQL is a great skill advancement!

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET
    average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END $$

DELIMITER ;
