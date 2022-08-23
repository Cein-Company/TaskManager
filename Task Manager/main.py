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
person task ------ To see person's task
tasks ------------ To see availble tasks
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

        situation = True
        while situation:
            time.sleep(2)
            clear()
            print("How do you want to add task?(1/2)\n1. Add task for a person\n2. Add task for a team")
            in1 = input()
            if in1 == "1":
                clear()
                print("Enter person name: ")
                person = input()
                if person == "":
                    print("Please enter name!")
                    hint()
                clear()
                print("Enter task: ")
                task = input()
                if task == "":
                    print("Please enter task!")
                    hint()
                clear()
                print("Enter password: ")
                password = input()
                if password == "":
                    print("Please enter password!")
                    hint()
                clear()
                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                if start == "":
                    print("Please enter start time!")
                    hint()
                s = start.split('/')
                if (len(s[0]) != 4) or (len(s[1]) != 2) or (len(s[2]) != 2):
                    print("Please enter correct date format") 
                    hint()
                clear()
                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                if finish == "":
                    print("Please enter finish time")
                    hint()
                f = finish.split('/')  
                if (len(f[0]) != 4) or (len(f[1]) != 2) or (len(f[2]) != 2):
                    print("Please enter correct date format")   
                    hint()   
                elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                    print("Start time can't be greater than finish time!")
                    hint()
                clear()
                print("Enter number of sections: ")
                n = int(input())
                if n == "" :
                    print("Please enter number of sections")
                    hint()
                section_list = []
                status_list = []
                membership_list = []
                for i in range(n):
                    clear()
                    print(f"Enter section {i+1}: ")
                    sections = input()
                    if sections == "":
                        print("Please enter finish time")
                        hint()
                    section_list.append(sections)
                    membership_list.append(person)
                    status_list.append("Undone")
                    
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
                if person == "":
                    print("Please enter team name!")
                    hint()
                clear()
                print("Enter task: ")
                task = input()
                if task == "":
                    print("Please enter task!")
                    hint()
                clear()
                print("Enter password: ")
                password = input()
                if password == "":
                    print("Please enter password!")
                    hint()
                clear()
                print("Enter start date:(Standard format: Year/Month/Day) ")
                start = input()
                if start == "":
                    print("Please enter start time!")
                    hint()
                s = start.split('/')
                if (len(s[0]) != 4) or (len(s[1]) != 2) or (len(s[2]) != 2):
                    print("Please enter correct date format") 
                    hint()    
                clear()
                print("Enter finish date:(Standard format: Year/Month/Day) ")
                finish = input()
                if finish == "":
                    print("Please enter finish time")
                    hint()
                f = finish.split('/')  
                if (len(f[0]) != 4) or (len(f[1]) != 2) or (len(f[2]) != 2):
                    print("Please enter correct date format")   
                    hint()   
                elif datetime.strptime(start, '%Y/%m/%d').date() > datetime.strptime(finish, '%Y/%m/%d').date():
                    print("Start time can't be greater than finish time!")
                    hint()
                clear()
                print("Enter number of sections: ")
                n = int(input())
                if n == "" :
                    print("Please enter number of sections")
                    hint()
                section_list = []
                status_list = []
                membership_list = []
                for i in range(n):
                    clear()
                    print(f"Enter section {i+1}: ")
                    sections = input()
                    if sections == "":
                        print("Please enter section")
                        hint()
                    section_list.append(sections)
                    print("Enter person name: ")
                    membership = input()
                    if membership == "":
                        print("Please enter membership")
                        hint()
                    membership_list.append(membership)
                    status_list.append("Undone")

                sections = '-'.join(map(str, section_list))
                status = '-'.join(map(str, status_list))
                membership = '-'.join(map(str, membership_list))
                db.insert_task(team, start, finish, task, password, sections, status, membership)
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
            print("Enter new start time:(Standard format: Year/Month/Day) ")
            new_start = input()
            if new_start == "":
                    print("Please enter start time!")
                    hint()
            s = new_start.split('/')
            if (len(s[0]) != 4) or (len(s[1]) != 2) or (len(s[2]) != 2):
                print("Please enter correct date format") 
                hint()
            db.edit_start(person, new_start)
            clear()
            print("Start time changed successfully.")
        elif in2 == "4":
            clear()
            print("Enter new finish time:(Standard format: Year/Month/Day) ")
            new_finish = input()
            if new_finish == "":
                    print("Please enter finish time")
                    hint()
            f = new_finish.split('/')  
            if (len(f[0]) != 4) or (len(f[1]) != 2) or (len(f[2]) != 2):
                    print("Please enter correct date format")   
                    hint()   
            elif datetime.strptime(new_start, '%Y/%m/%d').date() > datetime.strptime(new_finish, '%Y/%m/%d').date():
                    print("Start time can't be greater than finish time!")
                    hint()
            db.edit_finish(person, new_finish)
            clear()
            print("Finish time changed successfully.")
        elif in2 == "5":
            clear()
            print("Enter new number of sections: ")
            n = int(input())
            if n == "" :
                print("Please enter number of sections")
                hint()
            section_list = []
            for i in range(n):
                clear()
                print(f"Enter section {i+1}: ")
                sections = input()
                if sections == "":
                    print("Please enter finish time")
                    hint()
                section_list.append(sections)
            new_sections = '-'.join(map(str, section_list))    
            db.edit_sections(person, new_sections)
            clear()
            print("Sections changed successfully.")
        elif in2 == "6":
            clear()
            print("Enter new number of status: ")
            n = int(input())
            if n == "" :
                    print("Please enter number of status")
                    hint()
            status_list = []
            for i in range(n):
                clear()
                print(f"Enter status {i+1}:(done/undone)")
                status = input()
                if status == "":
                    print("Please enter status")
                    hint()
                status_list.append(status)
            new_status = '-'.join(map(str, status_list))    
            db.edit_status(person, new_status)
            clear()
            print("Status changed successfully.")
        elif in2 == "7":
            clear()
            print("Enter new number of membership: ")
            n = int(input())
            membership_list = []
            for i in range(n):
                clear()
                print(f"Enter person name {i+1}: ")
                membership = input()
                if membership == "":
                    print("Please enter membership")
                    hint()
                membership_list.append(membership)
            new_membership = '-'.join(map(str, membership_list))    
            db.edit_membership(person, new_membership)
            clear()
            print("Membership changed successfully.")        
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
            hint()
        elif len(db.get_person_tasks(person)) == 0:
            clear()
            print("No task found!")    
        elif db.check_password(person, password) == False:
            clear()
            print("Invalid password!")
            hint()
        else:
            clear()
            print(db.get_person_tasks(person))
        hint()
            
    elif msg == "plot" :
        
        clear()
        print("How do you want to see plot?(1/2)\n1.All people\n2.Specific person")
        in3 = input()
        if in3 == "1":
            clear()
            if len(db.get_all_tasks()) == 0:
                print("No task found!")
            else:
                p.plot_show()
        elif in3 == "2":
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
        else:
                print("Invalid command!")                    
        hint()
        
    elif msg == "pie" :
        
        clear()
        print("How do you want to see pie chart?(1/2)\n1.All people\n2.Specific person")
        in4 = input()
        if in4 == "1":
            clear()
            if len(db.get_all_tasks()) == 0:
                print("No task found!")
            else:
                pie.pie_show()
        elif in4 == "2":
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
                pie.pie_show1(person)          
        else:
                print("Invalid command!")   
        hint()    
             
    else:
        clear()
        print("Invalid command!")
        hint()
                