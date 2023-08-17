-- rating genres
SELECT tg.name, SUM(tr.rate) AS rating
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
JOIN tv_show_ratings tr
ON tsg.show_id = tr.show_id
GROUP BY tg.name
ORDER BY rating DESC;
