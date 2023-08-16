-- get california cities
SELECT id, name
FROM cities
WHERE ( SELECT id FROM states WHERE name = 'california')
ORDER BY cities.id
