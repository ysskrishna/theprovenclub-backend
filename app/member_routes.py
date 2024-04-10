from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import Response, MemberSchema
from dbutils import get_db

import crud

router = APIRouter()

@router.get("/")
async def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _members = crud.get_member(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_members)



@router.post("/create-dummy-members")
async def create_members_service(db: Session = Depends(get_db)):
    members_arr = [(2000, 'Member 1'),
    (2001, 'Member 2'),
    (2002, 'Member 3'),
    (2003, 'Member 4'),
    (2004, 'Member 5'),
    (2005, 'Member 6'),
    (2006, 'Member 7'),
    (2007, 'Member 8'),
    (2008, 'Member 9'),
    (2009, 'Member 10'),
    (2010, 'Member 11'),
    (2011, 'Member 12'),
    (2012, 'Member 13'),
    (2013, 'Member 14'),
    (2014, 'Member 15'),
    (2015, 'Member 16'),
    (2016, 'Member 17'),
    (2017, 'Member 18'),
    (2018, 'Member 19'),
    (2019, 'Member 20')];

    for item in members_arr:
        crud.create_member(db, MemberSchema(**{"member_name": item[1]}))
    return Response(status="Ok",
                    code="200",
                    message="Books created successfully").dict(exclude_none=True)