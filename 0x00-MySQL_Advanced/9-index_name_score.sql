-- Creates an index idx_name_first_score on table names to index only the first letter of each name and the score.
-- Context: Optimizing indexing can significantly improve query performance.

CREATE INDEX idx_name_first_score
ON names(name(1), score);
