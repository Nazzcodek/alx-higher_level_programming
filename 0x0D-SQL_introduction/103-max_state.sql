-- temperature by city
SELECT state, MAX(value) as max_temp
FROM temperatures
ORDER BY state
