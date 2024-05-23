from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session, joinedload
from typing import Optional, List

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to return all the Books
@app.get("/books/", response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    
    db_books = db.query(models.Book).options(joinedload(models.Book.reviews)).all()
    return db_books


# Endpoint to return all the Reviews
@app.get("/reviews/")
def get_reviews(db: Session = Depends(get_db)):
    
    db_reviews = db.query(models.Review).all()
    return db_reviews


# Endpoint to delete a book
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    """
    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="book not found")
    db.delete(db_book)
    db.commit()
    return db_book


# Endpoint to delete a review by its id
@app.delete("/reviews/{review_id}")
def delete_book(review_id: int, db: Session = Depends(get_db)):
    """
    Delete a review by its ID.
    """
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return db_review



# Endpoint to add a book
@app.post("/books/", response_model=schemas.Book)
def add_book(book: schemas.BookBase, db: Session = Depends(get_db)):
    """ 
    Adds a new book if not already present
    """
    db_book = models.Book(**book.dict())

    if db.query(models.Book).filter(models.Book.title == db_book.title, models.Book.author == db_book.author).first():
        raise HTTPException(status_code=400, detail="Book Already Exists with the given title for the author")
     
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Endpoint to add a review to a book
@app.post("/books/{book_id}/add_review", response_model=schemas.Review)
def add_review(book_id: int, review: schemas.ReviewBase, db: Session = Depends(get_db)):
    """ Adds a review to a book based on the book id """

    if db.query(models.Book).filter(models.Book.book_id == book_id).first():
        
        db_review = models.Review(**review.dict(), book_id= book_id)
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review
    
    raise HTTPException(status_code=404, detail="Book not found")



@app.get("/books/filter", response_model=List[schemas.Book])
def get_books_by_author_or_year(author: Optional[str] = None, publication_year: Optional[int] = None, db: Session = Depends(get_db)):
    """ Returns Books list based on author or publication year"""
    
    query = db.query(models.Book)
    
    if author:
        query = query.filter(models.Book.author == author)
    if publication_year != None:
        query = query.filter(models.Book.publication_year == publication_year)
    
    db_books = query.options(joinedload(models.Book.reviews)).all()
    
    if not db_books:
        raise HTTPException(status_code=404, detail="Books not found")
    
    return db_books



@app.get("/books/{book_id}/reviews", response_model=List[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    """ Returns all the reviews for a particular book"""

    db_review = db.query(models.Review).filter(models.Review.book_id == book_id).all()

    if db_review:
        return db_review
    
    raise HTTPException(status_code=404, detail="No reviews found for this book")



# # Simulated email sending function
# def send_confirmation_email(email: str, review_text: str):
#     # Simulate sending email (e.g., using an SMTP library)
#     time.sleep(2)  # Simulate delay for sending email
#     print(f"Sent confirmation email to {email} about review: {review_text}")

# # Endpoint to post a review with background task for sending email
# @app.post("/reviews/", response_model=schemas.Review)
# def create_review(
#     review: schemas.ReviewCreate,
#     background_tasks: BackgroundTasks,
#     db: Session = Depends(get_db)
# ):
#     # Create the review in the database
#     db_review = models.Review(review_text=review.text_review, book_id=review.book_id)
    
#     # Add background task to send confirmation email
#     background_tasks.add_task(send_confirmation_email, review.email, review.review_text)
    
#     return db_review