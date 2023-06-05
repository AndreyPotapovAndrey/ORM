import sqlalchemy
from sqlalchemy.orm import sessionmaker
from decouple import config
from Models_homework import create_tables, Publisher, Book, Stock, Shop, Sale


DSN = config('DSN', default='')

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

# pub1 = Publisher(name='Буквоед')
# pub2 = Publisher(name='Лабиринт')
# pub3 = Publisher(name='Книжный дом')
#
# book1 = Book(title='Капитанская дочка', pub=pub1)
# book2 = Book(title='Руслан и Людмила', pub=pub1)
# book3 = Book(title='Капитанская дочка', pub=pub2)
# book4 = Book(title='Евгений Онегин', pub=pub3)
# book5 = Book(title='Капитанская дочка', pub=pub1)
#
# shop1 = Shop(name='Молодая гвардия')
# shop2 = Shop(name='Московский дом книги')
# shop3 = Shop(name='Республика')
#
# session.add_all([pub1, pub2, pub3, \
#                  book1, book2, book3, book4, book5, \
#                  shop1, shop2, shop3])
# session.commit()

# Как заполнить через скрипт ORM таблицы "stock" и "sale" я так и не понял. Если есть возможность пояснить, был бы очень признателен.

def get_shops(id_or_name):  # Функция принимает обязательный параметр
    request = session.query(  # Создаем общее тело запроса на выборку данных и сохраняем в переменную
        Book.title, Shop.name, Sale.price, Sale.date_sale,
        # Название книги, имя магазина, стоимость продажи и дату продажи
    ).select_from(Shop). \
        join(Stock, Stock.shop_id == Shop.id). \
        join(Book, Book.id == Stock.book_id). \
        join(Publisher, Publisher.id == Book.publisher_id). \
        join(Sale, Sale.stock_id == Stock.id)

    print(f'{"Book": ^40} | {"Shop": ^10} | {"Price": ^8} | {"Date": ^10}')
    if id_or_name.isdigit():
        request = request.filter(Publisher.id == id_or_name).all()
        for book_title, shop_name, price, date_sale in request:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')
    else:
        request = request.filter(Publisher.name == id_or_name).all()
        for book_title, shop_name, price, date_sale in request:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')

if __name__ == '__main__':
        create_tables(engine)
    id_or_name = input(
        "Введите id или название издательства: ")  # Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    print(get_shops(
        id_or_name))  # Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше
        
session.close
