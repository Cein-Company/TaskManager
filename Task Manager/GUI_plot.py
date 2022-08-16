from datetime import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *

engine = create_engine('sqlite:///tasks.db', echo = True)

Session = sessionmaker(bind = engine)
session = Session()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def plot1_show(person):
    dic = {}
    for task in session.query(Task).filter(Task.name == person):
        list = []
        dic[task.id] = []
        format = '%Y/%m/%d'
        time1 = task.start
        time11 = datetime.strptime(time1, format).date()
        list.append(time11)
        time2 = task.finish
        time22 = datetime.strptime(time2, format).date()
        list.append(time22)
        list.append(task.task)
        dic.update({task.id:list})
    
    sort_orders=sorted(dic.items(),key = lambda item: item[1][1])
    
    start_list = []
    finish_list = []
    duration_list = []
    task_list = []
    id_list = []
    for i in range(len(sort_orders)):
        id = sort_orders[i][0]
        start = sort_orders[i][1][0]
        finish = sort_orders[i][1][1]
        task = sort_orders[i][1][2]
    
        id_list.append(id)
        start_list.append(start)
        finish_list.append(finish)
        time_interval = str(finish - start)
        d = time_interval.split(" ")
        duration_list.append(int(d[0]))
        task_list.append(task)
        
    return id_list , task_list , start_list , finish_list , duration_list
    
def plot_show():
    dic = {}
    for task in session.query(Task).order_by(Task.id):
        list = []
        dic[task.id] = []
        format = '%Y/%m/%d'
        time1 = task.start
        time11 = datetime.strptime(time1, format).date()
        list.append(time11)
        time2 = task.finish
        time22 = datetime.strptime(time2, format).date()
        list.append(time22)
        list.append(task.task)
        list.append(task.name)
        dic.update({task.id:list})
    
    
    sort_orders = sorted(dic.items(),key = lambda item: item[1][1])
    start_list = []
    finish_list = []
    duration_list = []
    task_list = []
    id_list = []
    name_list = []
    for i in range(len(sort_orders)):
        id = sort_orders[i][0]
        start = sort_orders[i][1][0]
        finish = sort_orders[i][1][1]
        task = sort_orders[i][1][2]
        name = sort_orders[i][1][3]
        
        id_list.append(id)
        name_list.append(name)
        start_list.append(start)
        finish_list.append(finish)
        time_interval = str(finish - start)
        d = time_interval.split(" ")
        duration_list.append(int(d[0]))
        task_list.append(task)
        
    return id_list , name_list , task_list , start_list , finish_list , duration_list
    
