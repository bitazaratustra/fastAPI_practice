from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Blog(Base):
    __tablename__= 'blogs'
    id = Column(Integer, primary_key=True, index = True)
    title = Column (String)
    body = Column (String)
