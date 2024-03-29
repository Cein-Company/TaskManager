from datetime import datetime as dt
import os
from tabulate import tabulate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *
import pandas as pd

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def plot_show1(person):
    dic = {}
    for task in session.query(Task).filter(Task.name == person):
        list = []
        dic[task.id] = []
        format = '%Y/%m/%d'
        time1 = task.start
        time11 = dt.strptime(time1, format).date()
        list.append(time11)
        time2 = task.finish
        time22 = dt.strptime(time2, format).date()
        list.append(time22)
        list.append(task.task)
        list.append(task.sections)
        list.append(task.status)
        dic.update({task.id:list})
    
    sort_orders = sorted(dic.items(),key = lambda item: item[1][1])
    
    
    start_list = []
    finish_list = []
    duration_list = []
    task_list = []
    sections_list = []
    status_list = []
    id_list = []
    for i in range(len(sort_orders)):
        id = sort_orders[i][0]
        start = sort_orders[i][1][0]
        finish = sort_orders[i][1][1]
        task = sort_orders[i][1][2]
        sections = sort_orders[i][1][3]
        status = sort_orders[i][1][4]
        
        id_list.append(id)
        start_list.append(start)
        finish_list.append(finish)
        time_interval = str(finish-start)
        d = time_interval.split(" ")
        duration_list.append(int(d[0]))
        task_list.append(task)
        sections_list.append(sections)
        status_list.append(status)
    
        
    dict={'Task id':id_list,
          'Task':task_list,
          'Start':start_list,
          'Finish':finish_list,
          'Duration':duration_list,
          'Sections':sections_list,
          'Status':status_list}
    df = pd.DataFrame(dict,columns = ['Task id','Task','Start','Finish','Duration','Sections','Status'])
    
    clear()
    print(tabulate(df,headers= 'keys',tablefmt = 'fancy_grid'))
    
def plot_show():
    dict1 = {}
    for task in session.query(Task).order_by(Task.id):
        list = []
        dict1[task.id] = []
        format = '%Y/%m/%d'
        time1 = task.start
        time11 = dt.strptime(time1, format).date()
        list.append(time11)
        time2 = task.finish
        time22 = dt.strptime(time2, format).date()
        list.append(time22)
        list.append(task.task)
        list.append(task.name)
        list.append(task.sections)
        list.append(task.status)
        list.append(task.membership)
        dict1.update({task.id:list})
    
    sort_orders = sorted(dict1.items(),key=lambda item: item[1][1])

    start_list = []
    finish_list = []
    duration_list = []
    task_list = []
    id_list = []
    name_list = []
    sections_list = []
    status_list = []
    membership_list = []
    for i in range(len(sort_orders)):
        id = sort_orders[i][0]
        start = sort_orders[i][1][0]
        finish = sort_orders[i][1][1]
        task = sort_orders[i][1][2]
        name = sort_orders[i][1][3]
        sections = sort_orders[i][1][4]
        status = sort_orders[i][1][5]
        membership = sort_orders[i][1][6]
    
        id_list.append(id)
        name_list.append(name)
        start_list.append(start)
        finish_list.append(finish)
        time_interval = str(finish-start)
        d = time_interval.split(" ")
        duration_list.append(int(d[0]))
        task_list.append(task)
        sections_list.append(sections)
        status_list.append(status)
        membership_list.append(membership)
    
        
    dict={'Task id':id_list,
          'Name':name_list,
          'Task':task_list,
          'Start':start_list,
          'Finish':finish_list,
          'Duration':duration_list,
          'Sections':sections_list,
          'Status':status_list,
          'Membership':membership_list}
    df = pd.DataFrame(dict,columns = ['Task id','Name','Task','Start','Finish','Duration','Sections','Status','Membership'])
    
    clear()
    print(tabulate(df,headers = 'keys',tablefmt = 'fancy_grid'))    
