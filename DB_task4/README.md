# Домашнее задание к лекции «Продвинутая выборка данных»
## Задание 1
### Дано
Продолжаем работать со своей базой данных. В этом задании заполните базу данных из домашнего задания к занятию "Работа с SQL. Создание БД". В ней должно быть:

- не менее 4 исполнителей,
- не менее 3 жанров,
- не менее 3 альбомов,
- не менее 6 треков,
- не менее 4 сборников.

Внимание: должны быть заполнены все поля каждой таблицы, в том числе таблицы связей исполнителей с жанрами, исполнителей с альбомами, сборников с треками.

### Решение
```sql
INSERT INTO artist(artist_name) 
VALUES('Blink-182'), ('кис-кис'), ('Sum-41'),
	('Sebastian'), ('Moullinex'), ('DJ Snake'),
	('Дора'), ('Lady Gaga'),
	('Lil Peep'), ('Jay-Z'), ('Noize MC');

INSERT INTO genre(genre_name) 
VALUES('Панк'), ('Электро'), ('Поп'), ('Рэп');

INSERT INTO genre_artist(genre_id, artist_id) 
VALUES(1,1), (1,2), (1,3),
	(2,4), (2,5), (2,6),
	(3,7), (3,8),
	(4,9), (4,10), (4,11);
	
INSERT INTO album(album_name, year_of_release) 
VALUES('Feeling This',2003), ('как перестать беспокоиться и начать жить',2022), ('Does This Look Infected?',2002),
		('Notre Jour Viendra',2010), ('Nervous Brooklyn Sessions',2020), ('Encore', 2016),
		('Младшая сестра',2019), ('The Fame Monster',2009),
		('Come Over When You are Sober, Pt. 1',2017), ('Watch The Throne',2011), ('Выход в город',2021);

INSERT INTO album_artist(album_id, artist_id) 
VALUES(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11);

INSERT INTO track(track_name, duration, album_id) 
VALUES('Violance', 227, 1), ('Feeling This', 173, 1),
		('мой отчим', 170, 2), ('ты уже не ребенок', 191, 2),
		('Over My Head - Better Off Dead', 149, 3), ('Still Waiting', 159, 3),
		('L''enfance d''un chien', 256, 4),
		('Brooklyn (Back In Time)', 348, 5), ('Ergo', 410, 5),
		('Middle', 220, 6), ('Oh Me Oh My', 236, 6),
		('Дорадура', 132, 7), ('Жулик', 231, 7),
		('Bad Romance', 294, 8), ('Alejandro', 274, 8),
		('Benz Truck (гелик)', 159, 9), ('The Brightside', 206, 9),
		('Why I Love You', 201, 10), ('No Church In The Wild', 272, 10),
		('Миокард', 181, 11), ('Вояджер-1', 279, 11);

INSERT INTO collection(collection_name, year_of_release) 
VALUES('Хиты Молодежных Комедий', 2003), ('Летнее Настроение', 2018),
		('Микс', 2020), ('Современная Российская Музыка', 2022);

INSERT INTO track_collection(track_id, collection_id) 
VALUES(1,1), (2,1), (5,1), (6,1), 
	  (16,2), (11,2), (7,2), (8,2), (10,2), (14,2), (15,2),
	  (4,3), (8,3), (9,3), (12,3), (14,3), (17,3), (18,3), (19,3), 
	  (20,4), (21,4), (12,4), (13,4), (3,4), (4,4);
```

## Задание 2
### Дано
Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.

Внимание: результаты запросов не должны быть пустыми, учтите это при заполнении таблиц.

- Название и продолжительность самого длительного трека.
- Название треков, продолжительность которых не менее 3,5 минут.
- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
- Исполнители, чьё имя состоит из одного слова.
- Название треков, которые содержат слово «мой» или «my».

### Решение
Название и продолжительность самого длительного трека:
```sql
SELECT track_name, duration 
FROM track    
ORDER BY duration DESC
LIMIT 1;
```
Название треков, продолжительность которых не менее 3,5 минут:
```sql
SELECT track_name
FROM track
WHERE duration >= 3.5 * 60;
```
_ИЛИ_ 
```sql
SELECT track_name  
FROM track 
WHERE duration >= 210; -- 210 секунд - эквивалент 3.5 минутам
```
Названия сборников, вышедших в период с 2018 по 2020 год включительно:
```sql
SELECT collection_name 
FROM collection 
WHERE year_of_release BETWEEN 2018 and 2020;
```
Исполнители, чьё имя состоит из одного слова:
```sql
SELECT artist_name
FROM artist
WHERE artist_name NOT LIKE '% %' AND artist_name NOT LIKE '%-%';
```
Название треков, которые содержат слово «мой» или «my»:
```sql
SELECT track_name
FROM track
WHERE LOWER(track_name) LIKE '%my%' OR LOWER(track_name) LIKE '%мой%';
```
## Задание 3
### Дано
Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.

Внимание: результаты запросов не должны быть пустыми, при необходимости добавьте данные в таблицы.

- Количество исполнителей в каждом жанре.
- Количество треков, вошедших в альбомы 2019–2020 годов.
- Средняя продолжительность треков по каждому альбому.
- Все исполнители, которые не выпустили альбомы в 2020 году.
- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).

### Решение
Количество исполнителей в каждом жанре:
```sql
SELECT g.genre_name, count(ga.artist_id) 
FROM genre g
JOIN genre_artist ga ON g.id = ga.genre_id
GROUP BY g.genre_name;
```
Количество треков, вошедших в альбомы 2019–2020 годов:
```sql
SELECT a.album_name, a.year_of_release, count(t.id) 
FROM album a
JOIN track t ON a.id = t.album_id
WHERE a.year_of_release BETWEEN 2019 and 2020
GROUP BY a.album_name, a.year_of_release;
```
Средняя продолжительность треков по каждому альбому:
```sql
SELECT a.album_name, AVG(t.duration) 
FROM album a
JOIN track t ON a.id = t.album_id
GROUP BY a.album_name;
```
Все исполнители, которые не выпустили альбомы в 2020 году:
```sql
SELECT ar.artist_name 
FROM artist ar
JOIN album_artist aa ON ar.id = aa.artist_id
JOIN album a ON a.id = aa.album_id
WHERE a.year_of_release != 2020; 
```
Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами):
```sql
SELECT distinct c.collection_name 
FROM collection c
JOIN track_collection tc ON c.id = tc.collection_id
JOIN track t ON t.id = tc.track_id
JOIN album a ON a.id = t.album_id
JOIN album_artist aa ON a.id = aa.album_id
JOIN artist ar ON ar.id = aa.artist_id
WHERE ar.artist_name LIKE '%%Lady Gaga%%';
```