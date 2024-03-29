import database as db
import plot as p
import pie
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
one task --------- To see a single task
all tasks -------- To see all tasks
plot ------------- To show table plot
pie -------------- To show pie chart
exit ------------- To exit task manager
""")
    print("Enter your command: ")

clear()
print("Hi there, welcome to Task Manager")
hint()

while True:
    
    msg = input()
    
    if msg == "exit": 
        
        clear()
        break

    elif msg == "add" :

        #check date format 
        def validate(date_text):
            res = True
            try:
                res = bool(datetime.strptime(date_text, '%Y/%m/%d'))
            except ValueError:
                res = False
            return res    
                
        situation = True
        while situation:
            time.sleep(2)
            clear()
            print("How do you want to add task?(1/2)\n1. Add task for a person\n2. Add task for a team")
            in1 = input()
            if in1 == "1":
                clear()
                print("Enter name: ")
                person = input()
                if person == "":
                    clear()
                    print("Please enter name!")
                    hint()
                    break
                
                print("Enter task: ")
                task = input()
                if task == "":
                    clear()
                    print("Please enter task!")
                    hint()
                    break

                print("Enter password: ")
                password = input()
                if password == "":
                    clear()
                    print("Please enter password!")
                    hint()
                    break

                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                if start == "":
                    clear()
                    print("Please enter start time!")
                    hint()
                    break
                if validate(start) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break

                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                if finish == "":
                    clear()
                    print("Please enter finish time")
                    hint()
                    break
                if validate(finish) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break

                elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                    clear()
                    print("Start time can't be greater than finish time!")
                    hint()
                    break

                else:
                    print("Enter number of sections: ")
                    n = input()
                    if n == "":
                        clear()
                        print("Please enter number of sections!")
                        hint()
                        break
                    section_list = []
                    status_list = []
                    membership_list = []
                    for i in range(int(n)):
                        clear()
                        print(f"Enter section {i+1}: ")
                        sections = input()
                        section_list.append(sections)
                        membership_list.append(person)
                        status_list.append("undone")

                    sections = '-'.join(map(str, section_list))
                    status = '-'.join(map(str, status_list))
                    membership = '-'.join(map(str, membership_list))
                    db.insert_task(person, start, finish, task, password, sections, status, membership)
                    situation = False
                    clear()
                    print("Task added successfully.")
                hint()
                
            elif in1 == "2":
                clear()
                print("Enter team name: ")
                team = input()
                if team == "":
                    clear()
                    print("Please enter team name!")
                    hint()
                    break

                print("Enter task: ")
                task = input()
                if task == "":
                    clear()
                    print("Please enter task!")
                    hint()
                    break

                print("Enter password: ")
                password = input()
                if password == "":
                    clear()
                    print("Please enter password!")
                    hint()
                    break

                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                if start == "":
                    clear()
                    print("Please enter start time!")
                    hint()
                    break
                if validate(start) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break

                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                if finish == "":
                    clear()
                    print("Please enter finish time")
                    hint()
                    break
                if validate(finish) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break
 
                elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                    clear()
                    print("Start time can't be greater than finish time!")
                    hint()
                    break

                else:
                    print("Enter number of sections: ")
                    n = input()
                    if n == "":
                        clear()
                        print("Please enter number of sections!")
                        hint()
                        break
                    section_list = []
                    status_list = []
                    membership_list = []
                    for i in range(int(n)):
                        clear()
                        print(f"Enter section {i+1}: ")
                        sections = input()
                        section_list.append(sections)
                        print("Enter person name: ")
                        membership_list.append(input())
                        status_list.append("undone")

                    sections = '-'.join(map(str, section_list))
                    status = '-'.join(map(str, status_list))
                    membership = '-'.join(map(str, membership_list))
                    db.insert_task(team, start, finish, task, password, sections, status, membership)
                    situation = False
                    clear()
                    print("Task added successfully.")
                hint()    

            else:
                clear()
                print("Invalid input")      
                hint()

    elif msg == "remove" :
        
        clear()
        print("Enter name: ")
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
        print("Enter name: ")
        person = input()
        if person == "":
            print("Please enter name!")
            hint()
        if len(db.get_person_tasks(person)) == 0:
            clear()
            print("No task found!") 
            hint()    
        print("Password: ")
        password = input()
        if password == "":
            clear()
            print("Please enter password!")
            hint()
        if db.check_password(person, password) == False:
            clear()
            print("Invalid password!") 
            hint()   
        clear()
        print("What do you want to edit?(1/2/3/4/5/6/7)\n1.Name\n2.Task\n3.Start time\n4.Finish time\n5.Sections\n6.status\n7.membership")
        in2 = input()
        if in2 == "1":
            clear()
            print(db.get_person_tasks(person))
            print("Enter new name: ")
            new_name = input()
            if new_name == "":
                    print("Please enter name!")
                    hint()
            db.edit_name(person, new_name)
            clear()
            print("Name changed successfully.")
        elif in2 == "2":
            clear()
            print(db.get_person_tasks(person))
            print("Enter new task: ")
            new_task = input()
            if new_task == "":
                    print("Please enter task!")
                    hint()
            db.edit_task(person, new_task)
            clear()
            print("Task changed successfully.")    
        elif in2 == "3":
            clear()
            print(db.get_person_tasks(person))
            print("Enter new start time:(Standard format: Year/Month/Day) ")
            new_start = input()
            if new_start == "":
                    print("Please enter start time!")
                    hint()
            if validate(new_start) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break        
            db.edit_start(person, new_start)
            clear()
            print("Start time changed successfully.")
        elif in2 == "4":
            clear()
            print(db.get_person_tasks(person))
            print("Enter new finish time:(Standard format: Year/Month/Day) ")
            new_finish = input()
            if new_finish == "":
                    print("Please enter finish time")
                    hint()
            if validate(new_finish) == False:
                    clear()
                    print("Incorrect data format, should be YYYY/MM/DD")
                    hint()
                    break        
            elif datetime.strptime(new_start, '%Y/%m/%d').date() > datetime.strptime(new_finish, '%Y/%m/%d').date():
                    print("Start time can't be greater than finish time!")
                    hint()
            db.edit_finish(person, new_finish)
            clear()
            print("Finish time changed successfully.")
        elif in2 == "5":
                clear()
                len_sections = len(db.get_sections(person).split('-'))
                section_list = []
                clear()
                print(db.get_person_tasks(person))
                for i in range(len_sections):
                    print(f"Enter section {i+1}: ")
                    section_list.append(input())
                new_sections = '-'.join(map(str, section_list))    
                db.edit_sections(person, new_sections)
                clear()
                print("Sections changed successfully.")
        elif in2 == "6":
            clear()
            len_status = len(db.get_status(person).split('-'))
            status_list = []
            clear()
            print(db.get_person_tasks(person))
            for i in range(len_status):
                print(f"Enter status {i+1}:(done/undone)")
                status_list.append(input())
            new_status = '-'.join(map(str, status_list))    
            db.edit_status(person, new_status)
            clear()
            print("Status changed successfully.")
        elif in2 == "7":
            clear()
            len_membership = len(db.get_membership(person).split('-'))
            membership_list = []
            clear()
            print(db.get_person_tasks(person))
            for i in range(len_membership):
                print(f"Enter person name {i+1}: ")
                membership_list.append(input())
            new_membership = '-'.join(map(str, membership_list))    
            db.edit_membership(person, new_membership)
            clear()
            print("Membership changed successfully.")        
        else:
            clear()
            print("Invalid command!")           
        hint()        

    elif msg == "all tasks" :
        
        clear()
        if len(db.get_all_tasks()) == 0:
            print("No task found!")
        else:
            print(db.get_all_tasks())
        hint()
        
    elif msg == "one task" :

        clear()
        print("Enter name: ")
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
        print("How do you want to see plot?(1/2)\n1.All tasks\n2.One task")
        in3 = input()
        if in3 == "1":
            clear()
            if len(db.get_all_tasks()) == 0:
                print("No task found!")
            else:
                p.plot_show()
        elif in3 == "2":
            clear()
            print("Enter name: ")
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
        else:
            print("Invalid command!")                    
        hint()
        
    elif msg == "pie" :

        clear()
        print("Enter name: ")
        person = input()
        if person == "":
            clear()
            print("Please enter name!")
        elif db.search_name(person) == "false":
            clear()
            print("Nobody found!")
        else:
            pie.pie_show(person)            
        hint()    
             
    else:
        clear()
        print("Invalid command!")
        hint()
                