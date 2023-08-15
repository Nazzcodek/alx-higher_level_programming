-- group all
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY Score
ORDER BY number DESC
