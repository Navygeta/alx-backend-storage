-- Creates a view need_meeting that lists all students with a score under 80 (strict)
-- and who either haven't had a last meeting or had it more than 1 month ago.
-- Context: Views can simplify complex queries and provide a more structured way to access data.

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
AND (students.last_meeting IS NULL OR students.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));
