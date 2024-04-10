from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field, validator
from pydantic.generics import GenericModel
from datetime import datetime, date

T = TypeVar('T')


class BookSchema(BaseModel):
    book_name: str
    number_of_copies: int
    available_number_of_copies: int

    class Config:
        orm_mode = True


class MemberSchema(BaseModel):
    member_name: str

    class Config:
        orm_mode = True

class CirculationSchema(BaseModel):
    book_id: int
    member_id: int
    date: date

    @validator("date", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()
    

class RequestCirculation(BaseModel):
    parameter: CirculationSchema = Field(...)


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
