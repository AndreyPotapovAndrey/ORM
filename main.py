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

name = input('Введите название издательства: ')

for i in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == name).all():
    name_book, name_shop, i_price, i_data = i
    print(f'{name_book: <20} | {name_shop: >15} | {i_price: >5} | {i_data}')

session.close
