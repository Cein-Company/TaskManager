from posixpath import split
import database as db

import plot as p
import os

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
    
    msg=input()
    
    if msg=="exit": 
        
        clear()
        break

    elif msg=="add" :
        
        clear()
        print("Name: ")
        person = input()
        print("Task: ")
        task = input()
        print("Start Time:(Standard format: Year/Month/Day) ")
        start = input()
                 
        print("Finish Time:(Standard format: Year/Month/Day) ")
        finish = input()
    
        db.insert_task(person, start, finish, task)
        
        clear()
        print("Task added successfully")
        hint()
        
    elif msg=="remove" :
        
        clear()
        print("Name: ")
        person = input()

        db_tasks= db.get_person_tasks(person)

        if len(db_tasks)==0:
            print("No task found")
        else:
            print(db.get_person_tasks(person))
            
        print("How do you want to remove?(1/2)\n1.All tasks\n2.Specific task")
        if input()=="1":
            db.remove_all_tasks(person)
            clear()
            print("All tasks removed")
        else:
            print("Enter task id: ")
            id = input()
            db.remove_task(id)
            clear()
            print("Task removed")    
        hint()
     
    elif msg=="tasks" :
        
        clear()
        print(db.get_all_tasks())
        hint()
        
    elif msg=="person task" :
        
        clear()
        print("Name: ")
        person = input()
        db_tasks= db.get_person_tasks(person)
        clear()
        if len(db_tasks)==0:
            print("No task found")
            
        else:
            print(db_tasks)
        hint()
            
    elif msg=="plot" :
        
        clear()
        print("How do you want to see plot?(1/2)\n1.All people\n2.Specific person")
        if input()=="1":
            clear()
            p.plot_show()
        else:
            clear()
            print("Name: ")
            person = input()
            p.plot_show1(person)    
        hint()
             
    else:
        clear()
        print("Invalid command")
        hint()
                