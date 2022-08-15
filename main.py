import database as db
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hint():
    print("Available Commands: ")
    print("""
add -------------- To add task
remove ----------- To remove task
tasks ------------ To see availble task
exit ------------- To exit task manager
""")
    print("Enter your command: ")

clear()
print("Hi buddy")
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
        print("Task:")
        task = input()
        db.insert_task(person, task)
        clear()
        print("Task added successfully")
        hint()

    elif msg=="remove" :
        clear()

        print("Name:")
        person = input()

        db_tasks= db.get_person_tasks(person)

        if len(db_tasks)==0:
            print("No task found")
        else:
            print('Tasks:')
            for task in db_tasks:
                print(task[0] + ' -> ' + task[1])

            print("Do you want to remove all tasks for " + person + "? (y/n)")
            if input()=="y":
                db.remove_task(person)
                clear()
                print("All tasks removed")
        hint()

    elif msg=="tasks" :
        clear()
        db_tasks = db.get_all_tasks()[::-1]
        if len(db_tasks)==0 :
            print("There is no task")
        else:
            print("Tasks:\n")
            for task in db_tasks:
                print(task[0] + " -> " + task[1])
            print()
        hint()
    
    else:
        clear()
        print("Invalid command")
        hint()
        