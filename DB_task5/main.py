import psycopg2
from pprint import pprint


def create_db(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        lastname VARCHAR(30),
        email VARCHAR(254) UNIQUE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phone(
        number VARCHAR(11) PRIMARY KEY UNIQUE,
        client_id INTEGER REFERENCES client(id)
    );
    """)
    return


def delete_db(cur):
    cur.execute("""
        DROP TABLE client, phone CASCADE;
        """)


def add_phone(cur, client_id, tel):
    cur.execute("""
        INSERT INTO phone(number, client_id)
        VALUES (%s, %s)
        """, (tel, client_id))
    return client_id


def add_client(cur, name=None, surname=None, email=None, tel=None):
    cur.execute("""
        INSERT INTO client(name, lastname, email)
        VALUES (%s, %s, %s)
        """, (name, surname, email))
    cur.execute("""
        SELECT id from client
        ORDER BY id DESC
        LIMIT 1
        """)
    id = cur.fetchone()[0]
    if tel is None:
        return id
    else:
        add_phone(cur, id, tel)
        return id


def change_client(cur, id, name=None, surname=None, email=None):
    cur.execute("""
        SELECT * from client
        WHERE id = %s
        """, (id, ))
    info = cur.fetchone()
    if name is None:
        name = info[1]
    if surname is None:
        surname = info[2]
    if email is None:
        email = info[3]
    cur.execute("""
        UPDATE client
        SET name = %s, lastname = %s, email =%s 
        where id = %s
        """, (name, surname, email, id))
    return id


def delete_phone(cur, number):
    cur.execute("""
        DELETE FROM phone
        WHERE number = %s
        """, (number, ))
    return number


def delete_client(cur, id):
    cur.execute("""
        DELETE FROM phone
        WHERE client_id = %s
        """, (id, ))
    cur.execute("""
        DELETE FROM client 
        WHERE id = %s
       """, (id,))
    return id


def find_client(cur, name=None, surname=None, email=None, phone=None):
    where_conditions = []
    params = []

    if name:
        where_conditions.append("c.name LIKE %s")
        params.append('%' + name + '%')
    if surname:
        where_conditions.append("c.lastname LIKE %s")
        params.append('%' + surname + '%')
    if email:
        where_conditions.append("c.email LIKE %s")
        params.append('%' + email + '%')
    if phone:
        where_conditions.append("p.number LIKE %s")
        params.append('%' + phone + '%')

    where_clause = " AND ".join(where_conditions)

    if where_clause:
        sql = f"""
            SELECT c.id, c.name, c.lastname, c.email, p.number 
            FROM client c
            LEFT JOIN phone p ON c.id = p.client_id
            WHERE {where_clause}
        """
        cur.execute(sql, params)
    else:
        # Если фильтры не заданы, вернуть все записи
        cur.execute("""
            SELECT c.id, c.name, c.lastname, c.email, p.number 
            FROM client c
            LEFT JOIN phone p ON c.id = p.client_id
        """)
    return cur.fetchall()


if __name__ == '__main__':
    with psycopg2.connect(database="test12", user="postgres",
                          password="%%") as conn:
        with conn.cursor() as curs:
            delete_db(curs)  # - Удаление таблиц перед запуском, закомментируйте это строку после запуска.

            # # 1. Cоздание таблиц
            # create_db(curs)
            # print("Таблицы к БД созданы")

            # # 2. Добавление 5 клиентов
            # print("Добавлен клиент id:",
            #       add_client(curs, "Игорь", "Бабушкин", "ibabush@hotmail.com"))
            # print("Добавлен клиент id:",
            #       add_client(curs, "Кирилл", "Бледный",
            #                     "bledkir0t@ya.ru", 79680990031))
            # print("Добавлен клиент id:",
            #       add_client(curs, "Анна", "Лисашвили",
            #                     "anlis@mail.ru", 79161234567))
            # print("Добавлен клиент id:",
            #       add_client(curs, "Анастасия", "Жамалетдинова",
            #                     "zhama@ya.ru", 79370822819))
            # print("Добавлен клиент id:",
            #       add_client(curs, "Наталья", "Перова",
            #                     "nata@ibox.com"))
            # print("Данные в таблицах:")
            # curs.execute("""
            #     SELECT c.id, c.name, c.lastname, c.email, p.number FROM client c
            #     LEFT JOIN phone p ON c.id = p.client_id
            #     ORDER by c.id
            #     """)
            # pprint(curs.fetchall())

            # # 3. Добавление клиенту номер телефона
            # print("Телефон добавлен клиенту id: ",
            #       add_phone(curs, 2, 79192280288))
            # print("Телефон добавлен клиенту id: ",
            #       add_phone(curs, 1, 79179875432))
            #
            # print("Данные в таблицах")
            # curs.execute("""
            #     SELECT c.id, c.name, c.lastname, c.email, p.number FROM client c
            #     LEFT JOIN phone p ON c.id = p.client_id
            #     ORDER by c.id
            #     """)
            # pprint(curs.fetchall())

            # # 4. Изменение данных клиента
            # print("Изменены данные клиента id:",
            #       change_client(curs, 4, "Елизавета", None, 'lilip@gmail.com'))
            #
            # # 5. Удаляем клиенту номер телефона
            # print("Телефон удалён c номером: ",
            #       delete_phone(curs, '79179875432'))
            # print("Данные в таблицах")
            # curs.execute("""
            #     SELECT c.id, c.name, c.lastname, c.email, p.number FROM client c
            #     LEFT JOIN phone p ON c.id = p.client_id
            #     ORDER by c.id
            #     """)
            # pprint(curs.fetchall())

            # # 6. Удаление клиента (например, id 2)
            # print("Клиент удалён с id: ",
            #       delete_client(curs, 2))
            # curs.execute("""
            #                 SELECT c.id, c.name, c.lastname, c.email, p.number FROM client c
            #                 LEFT JOIN phone p ON c.id = p.client_id
            #                 ORDER by c.id
            #                 """)
            # pprint(curs.fetchall())

            # # 7. Поиск клиента
            # # 7.1 По email:
            # email_to_find = 'ibabush@hotmail.com'
            # found_clients = find_client(curs, email=email_to_find)
            #
            # if found_clients:
            #     print(f'Найденные клиенты с email {email_to_find}:')
            #     pprint(found_clients)
            # # 7.2 По имени, фамилии, телефон:
            # name_to_find = 'Елизавета'
            # surname_to_find = 'Жамалетдинова'
            # tel_to_find = '79370822819'
            # found_clients = find_client(curs, name=name_to_find, surname=surname_to_find, phone=tel_to_find)
            #
            # if found_clients:
            #     print(f'Найденные клиенты по параметрам:')
            #     pprint(found_clients)
            # else:
            #     print(f'Клиенты по заданным параметрам не найдены.')
