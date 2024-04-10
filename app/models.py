from sqlalchemy import  Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from config import Base
from datetime import datetime
from sqlalchemy.orm import declarative_mixin

@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)


class Book(Timestamp, Base):
    __tablename__ ="books"

    book_id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)
    number_of_copies = Column(Integer, nullable=False)
    available_number_of_copies = Column(Integer, nullable=False)


class Member(Timestamp, Base):
    __tablename__ ="members"

    member_id = Column(Integer, primary_key=True, index=True)
    member_name = Column(String, nullable=False)


class Circulation(Timestamp, Base):
    __tablename__ ="circulations"

    circulation_id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.book_id"), nullable=False)
    member_id = Column(Integer, ForeignKey("members.member_id"), nullable=False)
    event_type = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    book = relationship(Book)
    member = relationship(Member)