import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key = True, unique=True, nullable=False)
    nick = Column(String(250), nullable = False, unique = True)
    firstname = Column(String(250), nullable = False, unique = False)
    lastname = Column(String(250), nullable = False, unique = False)
    email = Column(String(250), nullable = False, unique = True)
    password = Column(String(250), nullable = False, unique = False)
    


class Comment(Base):
    __tablename__='comment'
    id = Column(Integer(), nullable= False, unique= True, primary_key = True)
    comment_text = Column(String(250), nullable = True, unique = False)
    author_id = Column(Integer(), nullable = False, unique = True)
    post_id = Column(Integer(), nullable = False, unique = True)



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), unique=False, nullable=False)



class Media(Base):
    __tablename__='media'
    id= Column(Integer(), nullable = False, unique = True, primary_key = True)
    type = Column(String(250), nullable = False, unique = False)
    url = Column(String(250), nullable = False, unique = True)
    post_id = Column(Integer(), nullable=False, unique=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e