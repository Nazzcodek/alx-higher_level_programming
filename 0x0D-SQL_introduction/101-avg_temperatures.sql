-- Average temperature order by city
SELECT city, AVG(value) as avg_temp
FROM temperatures
ORDER BY avg_temp DESC
