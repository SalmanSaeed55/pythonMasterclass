SELECT a.name AS Artist, al.name AS ALBUM, s.track AS Track, s.title AS Title
FROM artists a, albums al, songs s
WHERE a._id = al.artist AND s.album = al._id
ORDER BY a.name, al.name, s.track;

SELECT a.name, al.name
FROM artists a, albums al
WHERE a._id = al.artist
ORDER BY a.name;

SELECT s.track, s.title, a.name
FROM songs s, albums a
WHERE s.album = a._id;
