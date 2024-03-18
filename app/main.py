from fastapi import FastAPI

from app.database.db_posts_requests import create_post, get_user_posts
from app.database.db_users_requests import add_user, get_users, delete_users, get_user
from app.models import UserInput, PostCreation

app = FastAPI()


@app.post("/add_user")
async def user_creation(user: UserInput):
    print(user)
    return add_user(user.name, user.lastname)


@app.get("/")
async def greetings_message():
    return "Добро пожаловать на блогхаб!"


@app.get("/users")
async def get_all_users():
    return get_users()


@app.get("/drop_users")
async def get_all_users():
    return delete_users()


@app.get("/user/{user_id}")
async def fetch_user(user_id: int):
    return get_user(user_id)


@app.post("/post")
async def post(post_ent: PostCreation):
    return create_post(post_ent.auth_id, post_ent.header, post_ent.body)


@app.get("/user/{u_id}/posts")
async def get_posts(u_id: int):
    return get_user_posts(u_id)
