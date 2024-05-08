-- Procedure AddBonus takes 3 inputs (in this order):
-- user_id: a users.id value (assumed to be linked to an existing user)
-- project_name: a new or existing project name; if the project name is not found in the table, it is created
-- score: the score value for the correction
-- Creates a stored procedure AddBonus that adds a new correction for a student.
-- Context: Writing code in SQL is a great skill advancement!

DELIMITER $$;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT )
BEGIN
    IF NOT EXISTS(SELECT name FROM projects WHERE name=project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name=project_name), score);
END;$$
DELIMITER ;
