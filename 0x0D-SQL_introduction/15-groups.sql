-- list number of records with the same score in table
SELECT score, count(score) GROUP BY 1;
