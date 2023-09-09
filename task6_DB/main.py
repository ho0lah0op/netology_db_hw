import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Sale, Shop


def create_session():
    DSN = "postgresql://postgres:***@localhost:5432/book_shop"
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    return Session()


def find_publisher_by_id(session, publisher_id):
    return session.query(Publisher).filter(Publisher.id_publisher == publisher_id).first()


def find_publisher_by_name(session, publisher_name):
    query = session.query(Publisher).filter(Publisher.publisher_name.ilike(f"{publisher_name.split()[0]}%"))
    return query.all()


def find_books_by_publisher_id(session, publisher_id):
    return session.query(Book).filter(Book.id_publisher == publisher_id).all()


def find_sales_by_book_id(session, book_id):
    return session.query(Sale).join(Stock, Stock.id_stock == Sale.id_stock).filter(Stock.id_book == book_id).all()


def find_shop_by_stock_id(session, stock_id):
    return session.query(Shop).join(Stock, Stock.id_shop == Shop.id_shop).filter(Stock.id_stock == stock_id).first()


if __name__ == "__main__":
    session = create_session()

    input_value = input("Введите имя (publisher_name) или идентификатор (id_publisher) издателя: ")

    if input_value.isdigit():
        publisher = find_publisher_by_id(session, int(input_value))
        if publisher:
            books = find_books_by_publisher_id(session, publisher.id_publisher)
        else:
            print("Издатель не найден в базе данных")
            books = []
    else:
        publishers = find_publisher_by_name(session, input_value)
        if publishers:
            books = []
            for publisher in publishers:
                books.extend(find_books_by_publisher_id(session, publisher.id_publisher))
        else:
            print("Издатель не найден в базе данных")
            books = []

    for book in books:
        sales = find_sales_by_book_id(session, book.id_book)
        for sale in sales:
            shop = find_shop_by_stock_id(session, sale.id_stock)
            if shop:
                print(f"{book.book_title} | {shop.shop_name} | {sale.sale_price} | {sale.sale_date}")

    session.close()


