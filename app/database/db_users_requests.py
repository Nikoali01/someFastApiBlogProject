from sqlalchemy.exc import SQLAlchemyError

from app.database.db_creation import engine, users


def exec_db(req):
    with engine.connect() as conn:
        result = conn.execute(req)
        conn.commit()
        return result


def add_user(name: str, lastname: str):
    query = users.insert().values(name=name, lastname=lastname)
    try:
        exec_db(query)
        return {"message": "User added successfully"}
    except SQLAlchemyError as e:
        return {"error": str(e)}


def get_users():
    query = users.select()
    try:
        result = exec_db(query)
        return {"users": [{"id": user[0], "name": user[1], "lastname": user[2]} for user in result.fetchall()]}
    except SQLAlchemyError as e:
        return {"error": str(e)}


def delete_users():
    query = users.delete()
    try:
        exec_db(query)
        return {"message": "Все пользователи удалены"}
    except SQLAlchemyError as e:
        return {"error": str(e)}


def get_user(u_id: int):
    query = users.select().where(users.c.id == u_id)
    try:
        result = exec_db(query).fetchone()
        if result:
            return {"id": result[0], "name": result[1], "lastname": result[2]}
        else:
            return {"error": "User not found"}
    except SQLAlchemyError as e:
        return {"error": str(e)}



