-- This SQL script ranks the country origins of bands by the number of non-unique fans.
-- It selects the origin and the total number of fans from the metal_bands table, grouping them by origin.
-- The results are ordered by the total number of fans in descending order.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
