# 使用SQLAlchemy 
# ORM， 把关系数据库的表结构映射到对象上
import pymysql

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = 'person'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    # 一对多:
    # books = relationship('Book')

# class Book(base):
#     __tablename__ = 'book'
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     user_id = Column(String(20), ForeignKey('user.id'))
#     外键

engine = create_engine('mysql+pymysql://root:Zjf9437879228.@localhost:3306/test_py')
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
DBSession = sessionmaker(bind=engine)

# 查询
session = DBSession()
user = session.query(User).filter(User.id == '3').one()
print(user)
print('type:',type(user))
print('name:',user.name)
# session.close()

# 插入
new_user = User(id='4', name='Bob')

session.add(new_user)
session.commit()
session.close()