from sqlalchemy.orm import Session

import random
from datetime import datetime


from . import models, schemas


def get_book_by_title(db: Session, book_title: str):
    return db.query(models.Book).filter(models.Book.title == book_title).first()


def create_new_book_entry(db: Session, db_book):
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def create_review(db: Session, review: schemas.Review, book_id: int):
    db_review = models.Review(**review.dict(),id = random.seed(datetime.now().timestamp()), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review 


def get_books(db: Session, author: str, publication_year: int):
    return db.query(models.Book).filter(
        models.Book.author == author,
        models.Book.publication_year == publication_year
    ).all()


def get_books_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author).all()


def get_books_by_year(db: Session, publication_year: int):
    return db.query(models.Book).filter(models.Book.publication_year == publication_year).all()


def get_reviews_by_id(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

