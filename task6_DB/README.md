# Домашнее задание к лекции «Python и БД. ORM»
## Задание 1
**Дано**

Составить модели классов SQLAlchemy по схеме:

![Схема](files/book_publishers_scheme.png)

Легенда: система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только что за книга была продана, но и в каком магазине это было сделано, а также когда.

Интуитивно необходимо выбрать подходящие типы и связи полей.

**Решение**

Модели реализованы в файле [models.py](/task6_DB/models.py)

Схема созданной БД (book_shop) выглядит следующим образом:
![Схема_готовой_БД](files/схема_БД_решение.JPG)

## Задание 2
**Дано**

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python-скрипт, который:

- подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
- импортирует необходимые модели данных;
- принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг этого издателя:

~~~
название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки
~~~

**Решение**

Реализация задачи осуществлена в файле [main.py](/task6_DB/main.py)
Примеры запуска кода:

1. _Пользователь вводит_
~~~
Чехов #Поиск по publisher_name
~~~
_Результат_
~~~
Введите имя (publisher_name) или идентификатор (id_publisher) издателя: Чехов
Дама с собачкой | ЧитайГород | 300 | 2023-07-01 00:00:00
Дама с собачкой | Подписные Издания | 310 | 2023-07-28 00:00:00
Вишневый сад | Литрес | 530 | 2023-07-14 00:00:00

Process finished with exit code 0
~~~
2. _Пользователь вводит_
~~~
3 #Поиск по id_publisher
~~~
_Результат_
~~~
Введите имя (publisher_name) или идентификатор (id_publisher) издателя: 3
Дама с собачкой | ЧитайГород | 300 | 2023-07-01 00:00:00
Дама с собачкой | Подписные Издания | 310 | 2023-07-28 00:00:00
Вишневый сад | Литрес | 530 | 2023-07-14 00:00:00

Process finished with exit code 0
~~~
3. _Пользователь вводит_
~~~
Акунин #Поиск по несуществующему publisher_name в БД
~~~
_Результат_
~~~
Введите имя (publisher_name) или идентификатор (id_publisher) издателя: Акунин
Издатель не найден в базе данных

Process finished with exit code 0
~~~
4. _Пользователь вводит_
~~~
12 #Поиск по несуществующему id_publisher в БД
~~~
_Результат_
~~~
Введите имя (publisher_name) или идентификатор (id_publisher) издателя: 12
Издатель не найден в базе данных

Process finished with exit code 0
~~~
Обратите внимание, что поиск может быть осуществлен либо просто по фамилии, либо по фамилии, имени и отчеству.
Помимо, успешный результат поиска можно получить, введя id_publisher (если такой ID существует в базе)
