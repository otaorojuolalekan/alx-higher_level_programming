--LISTS ALL CITIES OF CALIFORNIA
SELECT 
    id, name 
FROM 
    cities
wHERE
id = (SELECT id from states where name = 'California')
