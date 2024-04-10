from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import Response, RequestCirculation
from dbutils import get_db

import crud

router = APIRouter()

@router.post("/checkout")
async def create_checkout(request: RequestCirculation, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, request.parameter.book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    member = crud.get_member_by_id(db, request.parameter.member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    
    if book.available_number_of_copies > 0:
        crud.update_book_checkout(db, book)
        crud.create_circulation_event(db, request.parameter, "CHECKOUT")
    else:
        raise HTTPException(status_code=400, detail="Book copies not available")
    
    return Response(status="Ok", code="200", message="Created Book Checkout Successfully")


@router.post("/return")
async def create_return(request: RequestCirculation, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, request.parameter.book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    member = crud.get_member_by_id(db, request.parameter.member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")


    if book.available_number_of_copies < book.number_of_copies:
        crud.update_book_return(db, book)
        crud.create_circulation_event(db, request.parameter, "RETURN")
    else:
        raise HTTPException(status_code=400, detail="Returned book copies are more than total")
    
    return Response(status="Ok", code="200", message="Created Book Return Successfully")