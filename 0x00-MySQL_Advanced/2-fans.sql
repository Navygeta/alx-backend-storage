-- Create a temporary table to store the counts of fans per band origin
CREATE TEMPORARY TABLE temp_band_fans_counts AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the country origins of bands based on the number of fans
SELECT origin, nb_fans
FROM temp_band_fans_counts
ORDER BY nb_fans DESC;
