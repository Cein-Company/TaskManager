from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///tasks.db', echo=True)
Base = declarative_base()

class Task(Base):
    """"""
    __tablename__ = "tasks"
 
    id = Column(Integer, primary_key=True)
    #team name or person name
    name = Column(String)
    #task name
    task = Column(String)
    #start date
    start = Column(String)
    #end date
    finish = Column(String)
    password = Column(String)
    sections = Column(String)
    status = Column(String)
    membership = Column(String)
    
    #----------------------------------------------------------------------
    
    def __init__(self, name, task, start, finish, password, sections, status, membership):
        """"""
        self.name = name
        self.task = task
        self.start = start
        self.finish = finish
        self.password = password
        self.sections = sections
        self.status = status
        self.membership = membership

# create tables
Base.metadata.create_all(engine)

