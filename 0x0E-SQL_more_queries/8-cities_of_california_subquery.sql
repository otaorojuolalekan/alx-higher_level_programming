--LISTS ALL CITIES OF CALIFORNIA
SELECT 
    c.id, c.name 
FROM 
    cities c
wHERE
state_id IN (SELECT s.id from states WHERE s.name = 'California')
ORDER BY 1 ASC;
