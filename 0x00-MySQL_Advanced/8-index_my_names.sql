-- Creates an index idx_name_first on table names to index only the first letter of each name.
-- Context: Optimizing indexing can significantly improve query performance.

CREATE INDEX idx_name_first
ON names(name(1));
