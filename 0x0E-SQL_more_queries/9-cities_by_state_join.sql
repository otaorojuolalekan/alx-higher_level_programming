-- cities by states using join
SELECT
    c.id, c.name, s.name
FROM
    cities c JOIN states s
ON
    c.state_id = s.id
ORDER BY 1;
