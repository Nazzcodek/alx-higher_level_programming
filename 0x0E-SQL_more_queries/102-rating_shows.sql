-- sum rating
SELECT ts.title, SUM(tr.rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings tr
ON ts.id = tr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
