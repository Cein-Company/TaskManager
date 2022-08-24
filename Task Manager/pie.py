from random import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *
import random
import os 
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pie_show(person):
    for task in session.query(Task).order_by(Task.id):
        sections = task.sections
        section_list = sections.split('-')
        membership = task.membership
        membership_list = membership.split('-')
        n = len(section_list)
        labels = []
        for i in range(n):
            labels.append(section_list[i]+ '(' + membership_list[i] + ')') 
        sizes = []
        for j in range(n):
            sizes.append(1)
        status = task.status
        info = status.split('-')
    color_list = ['gold', 'yellowgreen', 'darkviolet', 'lightcoral', 'lightskyblue', 'hotpink', 'aqua', 'g', 'blue', 'maroon', 'orange']
    colors = []
    for j in range(len(info)):
        if info[j] == 'undone':
            colors.append('gray')  
        else:
            colors.append(random.choice(color_list))            
    plt.pie(sizes, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    clear()
    plt.show()             
    
def pie_show1():
    for task in session.query(Task).filter(Task.name == person):
        sections = task.sections
        labels = sections.split('-')
        n = len(labels)
        sizes = []
        for i in range(n):
            sizes.append(1)
        status = task.status
        info = status.split('-')
    color_list = ['gold', 'yellowgreen', 'darkviolet', 'lightcoral', 'lightskyblue', 'hotpink', 'aqua', 'g', 'blue', 'maroon', 'orange']
    colors = []
    for j in range(len(info)):
        if info[j] == 'undone':
            colors.append('gray')  
        else:
            colors.append(random.choice(color_list))            
    plt.pie(sizes, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    clear()
    plt.show()        