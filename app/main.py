from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from book_routes import router as book_router
from member_routes import router as member_router
from circulation_routes import router as circulation_router
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/book", tags=["book"])
app.include_router(member_router, prefix="/member", tags=["member"])
app.include_router(circulation_router, prefix="/circulation", tags=["circulation"])