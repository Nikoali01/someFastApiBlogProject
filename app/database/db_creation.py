from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Double

engine = create_engine('sqlite:///blogs.db', echo=False)

meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

posts = Table(
    'posts', meta,
    Column('id', Integer, primary_key=True),
    Column('author_id', Integer, ForeignKey('users.id')),
    Column('header', String),
    Column('body', String),
)

comments = Table(
    'comments', meta,
    Column('id', Integer, primary_key=True),
    Column('commentator_id', Integer, ForeignKey('users.id')),
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('text', String),
)

meta.create_all(engine)
