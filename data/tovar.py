import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Tovar(SqlAlchemyBase):
    __tablename__ = 'tovar'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Name = sqlalchemy.Column(sqlalchemy.String)
    Price = sqlalchemy.Column(sqlalchemy.Integer)
    Info = sqlalchemy.Column(sqlalchemy.String)
    Image = sqlalchemy.Column(sqlalchemy.String)
