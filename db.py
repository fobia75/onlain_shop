import sqlalchemy
from sqlalchemy import create_engine
import databases 
import settings

from settings import settings


DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column('user_name', sqlalchemy.String(32)),
    sqlalchemy.Column('last_name', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(128)),
    sqlalchemy.Column('password', sqlalchemy.String(128))
)


goods = sqlalchemy.Table(
    'goods',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('description', sqlalchemy.String(1000)),
    sqlalchemy.Column('price', sqlalchemy.Float)
)


orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column(' goods_id', sqlalchemy.ForeignKey('goods.id')),
    sqlalchemy.Column('order_date', sqlalchemy.DateTime()),
    sqlalchemy.Column('order_status', sqlalchemy.String(32))
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)