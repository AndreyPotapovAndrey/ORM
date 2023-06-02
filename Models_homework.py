import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    book = relationship("Book", back_populates="pub")

    def __str__(self):
        return f'{self.id} | {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    pub = relationship("Publisher", back_populates="book")
    stock = relationship("Stock", back_populates="book_stock")

    def __str__(self):
        return f'{self.id} | {self.title} | {self.publisher_id}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book_stock = relationship("Book", back_populates="stock")

    stock_shop = relationship("Shop", back_populates="shop")

    stock_sale = relationship("Sale", back_populates="sale")

    def __str__(self):
        return f'{self.id} | {self.title} | {self.shop_id} | {self.count}'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    shop = relationship("Stock", back_populates="stock_shop")

    def __str__(self):
        return f'{self.id} | {self.name}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    sale = relationship("Stock", back_populates="stock_sale")

    def __str__(self):
        return f'{self.id} | {self.price} | {self.date_sale} | {self.stock_id} | {self.count}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
