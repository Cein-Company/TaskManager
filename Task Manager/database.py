from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *
import os

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_name(person):
    s = ""
    for task in session.query(Task).order_by(Task.id).filter(Task.name == person):
        s += task.name
    if s == "" :
        return "false"   
  
def search_id(id):
    s = ""
    for task in session.query(Task).order_by(Task.id).filter(Task.id == id):
        s += str(task.id)
    if s == "" :
        return "false"  
            
def insert_task(person, start, finish, task, password, sections):
    task1 = Task(person, task, start, finish, password, sections)
    session.add(task1)
    session.commit()
    
   
def get_all_tasks():
    s = ""
    for task in session.query(Task).order_by(Task.id):
        s += (str(task.id) + " " + task.name + " " + task.task + " " + task.start + " " + task.finish + task.sections + "\n")    
    clear()
    return s

def get_person_tasks(person):
    s = ""
    for task in session.query(Task).filter(Task.name == person):
        s += (str(task.id) + " " + task.name + " " + task.task + " " + task.start + " " + task.finish + task.sections + "\n")
    clear()
    return s

def remove_task(id):
    session.query(Task).filter(Task.id == id).delete()
    session.commit()

def remove_all_tasks(person):
    session.query(Task).filter(Task.name == person).delete()
    session.commit()

def check_password(person, password):
    s = ""
    for task in session.query(Task).filter(Task.name == person):
        s += task.password
    if s == password:
        return True
    else:
        return False        

def edit_name(person, new_name):
    session.query(Task).filter(Task.name == person).update({"name": new_name})
    session.commit()

def edit_task(person, new_task):
    session.query(Task).filter(Task.name == person).update({"task": new_task})
    session.commit()

def edit_start(person, new_start):
    session.query(Task).filter(Task.name == person).update({"start": new_start})
    session.commit()

def edit_finish(person, new_finish):
    session.query(Task).filter(Task.name == person).update({"finish": new_finish})
    session.commit()

def edit_password(person, new_password):
    session.query(Task).filter(Task.name == person).update({"password": new_password})
    session.commit()

def edit_sections(person, new_sections):
    session.query(Task).filter(Task.name == person).update({"sections": new_sections})
    session.commit()
