import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

association = sqlalchemy.Table(
    'news_to_category',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('news_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('news.id')),
    sqlalchemy.Column('category_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('category.id'))
)

class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
