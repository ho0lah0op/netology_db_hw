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