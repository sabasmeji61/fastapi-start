# from typing import Optional, List
# from fastapi import FastAPI  #, Response, status, HTTPException, Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor
from .database import engine  #, get_db
from . import models  #, schemas, utils
from .routers import post, user, auth, vote
from .config import settings

# print(settings.database_username)
# models.Base.metadata.create_all(bind=engine)  ## replaced by alembic system!!!

app = FastAPI()

# origins =["https://www.google.com", "https://www.youtube.com"]
origins =["*"]  # for all domains!

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": 
# "favorite foods", "content": "I like pizza", "id": 2}]
# def find_post(id):
# def find_index_post(id):
#    for i, p in enumerate(my_posts):
#        if p['id'] == id:
#            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# async def root():  *removed de keyword async from 'def root():' *request Get method url: "/"
@app.get("/")
def root():
    # return {"message": "Welcome to my api"}
    return {"message": "Hello World"}

