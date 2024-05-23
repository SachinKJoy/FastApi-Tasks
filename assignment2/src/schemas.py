from pydantic import BaseModel
from typing import List



class ReviewBase(BaseModel):
    text_review: str
    rating: float


class BookBase(BaseModel):

    title: str
    author: str
    publication_year: int


class Review(ReviewBase):

    id: int
    book_id: int
    class Config:
        orm_mode = True


class Book(BookBase):

    book_id: int
    reviews: List[ReviewBase] = [] 

    class Config:
        orm_mode = True
