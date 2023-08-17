-- lists all genres of the show not Dexter.
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
	SELECT tv_show_genres.genre_id
	FROM tv_show_genres
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
	) AS dexter_genres
ON tv_genres.id = dexter_genres.genre_id
WHERE dexter_genres.genre_id IS NULL
ORDER BY tv_genres.name;
