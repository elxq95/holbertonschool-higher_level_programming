-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- 	Links tv_shows with tv_show_genres by matching tv_shows.id with tv_show_genres.show_id.
-- 	This LEFT JOIN ensures that all shows are listed, even if there is no matching entry in tv_show_genres.
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
