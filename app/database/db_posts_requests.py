from sqlalchemy.exc import SQLAlchemyError

from app.database.db_creation import posts, engine


def exec_db(req):
    with engine.connect() as conn:
        result = conn.execute(req)
        conn.commit()
        return result


def create_post(a_id: int, header: str, body: str):
    query = posts.insert().values(author_id=a_id, header=header, body=body)
    try:
        exec_db(query)
        return {"message": f"Information was posted to {a_id} blog"}
    except SQLAlchemyError as e:
        return {"error": str(e)}


def get_user_posts(u_id: int):
    query = posts.select().where(posts.c.author_id == u_id)
    try:
        result = exec_db(query).fetchall()
        return {"posts": [{"id": post[0], "author_id": post[1], "header": post[2], "body": post[3]} for post in
                          result]}
    except SQLAlchemyError as e:
        return {"error": str(e)}
