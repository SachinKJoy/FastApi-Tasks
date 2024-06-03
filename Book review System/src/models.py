from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(Integer)

    reviews = relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text_review = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.book_id'))

    book = relationship("Book", back_populates="reviews")