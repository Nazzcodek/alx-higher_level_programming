-- temperature by city
SELECT state, MAX(value) as max_temp
FROM tempratures
ORDER BY state
