-- list number of records with the same score in table
SELECT score,  COUNT(score) FROM second_table GROUP BY 1;
