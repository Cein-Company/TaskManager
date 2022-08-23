import database as db
import plot as p
import os
from datetime import datetime
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
           
def hint():
    
    print("Available Commands: ")
    print("""
add -------------- To add task
remove ----------- To remove task
person task ------ To see person's task
tasks ------------ To see availble tasks
plot ------------- To show plot
exit ------------- To exit task manager
""")
    print("Enter your command: ")

clear()
print("Hiiiii")
hint()

while True:
    
    msg = input()
    
    if msg == "exit": 
        
        clear()
        break

    elif msg == "add" :

        situation = True
        while situation:
            time.sleep(2)
            clear()
            print("Enter person name: ")
            person = input()
            print("Enter task: ")
            task = input()
            print("Enter start date:(Standard format: Year/Month/Day) ")
            start = input()
            print("Enter finish date:(Standard format: Year/Month/Day) ")
            finish = input()

            if person == "":
                print("Please enter name!")
            elif task == "":
                print("Please enter task!")
            elif start == "":
                print("Please enter start time!")
            elif finish == "":
                print("Please enter finish time")
            elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                print("Start time can't be greater than finish time!")
            else:
                db.insert_task(person, start, finish, task)
                situation = False
                clear()
                print("Task added successfully.")
                hint()  
       
    elif msg == "remove" :
        
        clear()
        print("Name: ")
        person = input()

        db_tasks = db.get_person_tasks(person)

        if len(db_tasks) == 0:
            print("No task found!")
        else:
            print(db.get_person_tasks(person))
            
        print("How do you want to remove?(1/2)\n1.All tasks\n2.Specific task")
        if input() == "1":
            db.remove_all_tasks(person)
            clear()
            print("All tasks removed.")
        else:
            print("Enter task id: ")
            id = input()
            db.remove_task(id)
            clear()
            print("Task removed.")    
        hint()
     
    elif msg == "tasks" :
        
        clear()
        if len(db.get_all_tasks()) == 0:
            print("No task found!")
        else:
            print(db.get_all_tasks())
        hint()
        
    elif msg == "person task" :

        clear()
        print("Enter person name: ")
        person = input()
        if person == "":
            clear()
            print("Please enter name!")
        elif db.search_name(person) == "false":
            clear()
            print("Nobody found!")
        elif len(db.get_person_tasks(person)) == 0:
            clear()
            print("No task found!")    
        else:
            clear()
            print(db.get_person_tasks(person))
        hint()
            
    elif msg == "plot" :
        
        clear()
        print("How do you want to see plot?(1/2)\n1.All people\n2.Specific person")
        if input() == "1":
            clear()
            if len(db.get_all_tasks()) == 0:
                print("No task found!")
            else:
                p.plot_show()
        else:
            clear()
            print("Name: ")
            person = input()
            if person == "":
                clear()
                print("Please enter name!")
            elif db.search_name(person) == "false":
                clear()
                print("Nobody found!")
            else:
                clear()
                p.plot_show1(person)          
        hint()
             
    else:
        clear()
        print("Invalid command!")
        hint()
                