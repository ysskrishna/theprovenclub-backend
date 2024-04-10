from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import Response, RequestBook, BookSchema
from dbutils import get_db

import crud

router = APIRouter()

@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)


@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.post("/create-dummy-books")
async def create_book_service(db: Session = Depends(get_db)):
    books_arr = [(1000, 'Book 1', 2, 2),
    (1001, 'Book 2', 4, 4),
    (1002, 'Book 3', 1, 1),
    (1003, 'Book 4', 3, 3),
    (1004, 'Book 5', 1, 1),
    (1005, 'Book 6', 2, 2),
    (1006, 'Book 7', 4, 4),
    (1007, 'Book 8', 4, 4),
    (1008, 'Book 9', 3, 3),
    (1009, 'Book 10', 1, 1),
    (1010, 'Book 11', 5, 5),
    (1011, 'Book 12', 5, 5),
    (1012, 'Book 13', 4, 4),
    (1013, 'Book 14', 3, 3),
    (1014, 'Book 15', 3, 3),
    (1015, 'Book 16', 5, 5),
    (1016, 'Book 17', 4, 4),
    (1017, 'Book 18', 1, 1),
    (1018, 'Book 19', 4, 4),
    (1019, 'Book 20', 5, 5)];

    for item in books_arr:
        crud.create_book(db, BookSchema(**{"book_name": item[1], "number_of_copies": item[2], "available_number_of_copies": item[3]}))
    return Response(status="Ok",
                    code="200",
                    message="Books created successfully").dict(exclude_none=True)