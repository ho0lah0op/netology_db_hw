SELECT track_name, duration
FROM track
ORDER BY duration DESC
LIMIT 1;

SELECT track_name, duration
FROM track
WHERE duration >= 3.5 * 60;

SELECT track_name, duration
FROM track
WHERE duration >= 210;

SELECT collection_name
FROM collection
WHERE year_of_release BETWEEN 2018 and 2020;

SELECT artist_name
FROM artist
WHERE artist_name NOT LIKE '% %' AND artist_name NOT LIKE '%-%';

SELECT track_name
FROM track
WHERE LOWER(track_name) LIKE '%my%' OR LOWER(track_name) LIKE '%мой%';

SELECT g.genre_name, count(ga.artist_id)
FROM genre g
JOIN genre_artist ga ON g.id = ga.genre_id
GROUP BY g.genre_name;

SELECT a.album_name, a.year_of_release, count(t.id)
FROM album a
JOIN track t ON a.id = t.album_id
WHERE a.year_of_release BETWEEN 2019 and 2020
GROUP BY a.album_name, a.year_of_release;

SELECT a.album_name, AVG(ROUND(t.duration/60, 2))
FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY a.album_name;

SELECT a.album_name, AVG(t.duration)
FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY a.album_name;

SELECT ar.artist_name
FROM artist ar
JOIN album_artist aa ON ar.id = aa.artist_id
   JOIN album a ON a.id = aa.album_id
   WHERE a.year_of_release != 2020;

SELECT distinct c.collection_name
FROM collection c
JOIN track_collection tc ON c.id = tc.collection_id
JOIN track t ON t.id = tc.track_id
JOIN album a ON a.id = t.album_id
JOIN album_artist aa ON a.id = aa.album_id
JOIN artist ar ON ar.id = aa.artist_id
WHERE ar.artist_name LIKE '%%Lady Gaga%%';