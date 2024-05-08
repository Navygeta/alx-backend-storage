-- Create function SafeDiv that divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0
-- Function SafeDiv takes 2 arguments: a, INT, b, INT
-- Returns a / b or 0 if b == 0
-- Context: Utilizing functions can enhance SQL code modularity and reusability.

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
