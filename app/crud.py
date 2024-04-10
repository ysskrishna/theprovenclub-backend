from sqlalchemy.orm import Session
from models import Book, Member, Circulation
from schemas import BookSchema, CirculationSchema, MemberSchema


def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_member(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.book_id == book_id).first()


def get_member_by_id(db: Session, member_id: int):
    return db.query(Member).filter(Member.member_id == member_id).first()


def create_book(db: Session, book: BookSchema):
    _book = Book(
        book_name=book.book_name, 
        number_of_copies=book.number_of_copies,
        available_number_of_copies=book.available_number_of_copies,
    )
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

def create_member(db: Session, member: MemberSchema):
    _member = Member(
        member_name=member.member_name, 
    )
    db.add(_member)
    db.commit()
    db.refresh(_member)
    return _member

def update_book_checkout(db: Session, _book: Book):
    _book.available_number_of_copies -= 1

    db.commit()
    db.refresh(_book)
    return _book

def update_book_return(db: Session, _book: Book):
    _book.available_number_of_copies += 1

    db.commit()
    db.refresh(_book)
    return _book


def create_circulation_event(db: Session, circulation: CirculationSchema, event_type=str):
    _circulation = Circulation(
        book_id = circulation.book_id,
        member_id = circulation.member_id,
        event_type = event_type,
        date = circulation.date
    )
    db.add(_circulation)
    db.commit()
    db.refresh(_circulation)
    return _circulation