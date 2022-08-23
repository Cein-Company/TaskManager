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
edit ------------- To edit task
person task ------ To see person's task
tasks ------------ To see availble tasks
plot ------------- To show plot
exit ------------- To exit task manager
""")
    print("Enter your command: ")

clear()
print("Hi three, welcome to Task Manager")
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
            print("How do you want to add task?(1/2)\n1. Add task for a person\n2. Add task for a team")
            if input() == "1":
                clear()
                print("Enter person name: ")
                person = input()
                clear()
                print("Enter task: ")
                task = input()
                clear()
                print("Enter password: ")
                password = input()
                clear()
                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                clear()
                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                clear()
                print("Enter number of sections: ")
                n = int(input())
                for i in range(n):
                    clear()
                    print("Enter section: ")
                    sections[i][0] = input()
                    sections[i][1] = person
                    sections[i][2] = "Undone"

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
                    db.insert_task(person, start, finish, task, password, sections)
                    situation = False
                    clear()
                    print("Task added successfully.")
                    hint()
            elif input() == "2":
                clear()
                print("Enter team name: ")
                team = input()
                clear()
                print("Enter task: ")
                task = input()
                clear()
                print("Enter password: ")
                password = input()
                clear()
                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                clear()
                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                clear()
                print("Enter number of sections: ")
                n = int(input())
                for i in range(n):
                    clear()
                    print("Enter section: ")
                    sections[i][0] = input()
                    print("Enter person name: ")
                    sections[i][1] = input()
                    sections[i][2] = "undone"

                if team == "":
                    print("Please enter team name!")
                elif task == "":
                    print("Please enter task!")
                elif start == "":
                    print("Please enter start time!")
                elif finish == "":
                    print("Please enter finish time")
                elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                    print("Start time can't be greater than finish time!")
                else:
                    db.insert_task(team, start, finish, task, password, sections)
                    situation = False
                    clear()
                    print("Task added successfully.")
                    hint()    
            else:
                print("Invalid input")      
       
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

    elif msg == "edit" :

        clear()
        print("Name: ")
        person = input()
        print("Password: ")
        password = input()
        if person == "":
            clear()
            print("Please enter name!")
        elif len(db.get_person_tasks(person)) == 0:
            clear()
            print("No task found!")    
        elif password == "":
            clear()
            print("Please enter password!")
        elif db.check_password(person, password) == False:
            clear()
            print("Invalid password!")    
        else:
            clear()
            print("What do you want to edit?(1/2/3/4/5)\n1.Name\n2.Task\n3.Start time\n4.Finish time\n5.Sections")
            if input() == "1":
                clear()
                print("Enter new name: ")
                new_name = input()
                db.edit_name(person, new_name)
                clear()
                print("Name changed successfully.")
            elif input() == "2":
                clear()
                print("Enter new task: ")
                new_task = input()
                db.edit_task(person, new_task)
                clear()
                print("Task changed successfully.")    
            elif input() == "3":
                clear()
                print("Enter new start time:(Standard format: Year/Month/Day) ")
                new_start = input()
                db.edit_start(person, new_start)
                clear()
                print("Start time changed successfully.")
            elif input() == "4":
                clear()
                print("Enter new finish time:(Standard format: Year/Month/Day) ")
                new_finish = input()
                db.edit_finish(person, new_finish)
                clear()
                print("Finish time changed successfully.")
            elif input() == "5":
                clear()
                print("Enter new number of sections: ")
                n = int(input())
                for i in range(n):
                    clear()
                    print("Enter section: ")
                    sections[i][0] = input()
                    print("Enter person name: ")
                    sections[i][1] = input()
                    print("Enter status:(Done/Undone)")
                    sections[i][2] = input()
                db.edit_sections(person, sections)
                clear()
                print("Sections changed successfully.")
            else:
                print("Invalid command!")   
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
        print("Enter password: ")
        password = input()
        if person == "":
            clear()
            print("Please enter name!")
        elif db.search_name(person) == "false":
            clear()
            print("Nobody found!")
        elif len(db.get_person_tasks(person)) == 0:
            clear()
            print("No task found!")    
        elif db.check_password(person, password) == False:
            clear()
            print("Invalid password!")
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
                