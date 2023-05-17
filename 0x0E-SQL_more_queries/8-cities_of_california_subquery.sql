--LISTS ALL CITIES OF CALIFORNIA
SELECT
    id, name
FROM cities
wHERE state_id IN
    (SELECT id from states WHERE name = 'California')
ORDER BY 1 ASC;
