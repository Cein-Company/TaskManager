from cProfile import label
from cgitb import text
from os import remove
from tracemalloc import start
from turtle import color, right, title
import PySimpleGUI as sg
from tkinter import *
import database as db
from tkinter import ttk
import GUI_plot as gp

"""
def login():
    
    def check():            
            login_text=login_pass.get()
            login_pass.delete(0, END)
            if login_text != "1234":               
                label = Label(login_page, text="Wrong Password", bg='light blue', fg='red', font='Any 10')
                label.pack()
            else:
                pass   
    login_page = Tk()
    login_page.geometry("600x300")
    login_page.title("Login")
    login_page.configure(bg='light blue')
    
    label1 = Label(login_page,
        text ="Password:",
        foreground="blue",
        bg='light blue',
        font='Any 10')
    label1.pack()
    login_pass=Entry(login_page)
    login_pass.pack()
    
    bt = Button(login_page,
                    text ="Submit", command=check, bg='sky blue')
    bt.pack()
    
login()    
""" 

layout = [[sg.Text('Hello there, welcome to our app!', text_color='blue', font=('Any 15'))],
          [sg.Text('Please select the option you want:', text_color='lightgreen', font=('Any 12'))],
          [[sg.Button('Add', button_color='green')], [sg.Button('Remove', button_color='red')], [sg.Button('Person Task', button_color='blue')], [sg.Button('Tasks', button_color='teal')], [sg.Button('Plot', button_color='purple')], [sg.Button('Exit', button_color='dark red')]]]

window = sg.Window('Task Manager', layout,margins=(300, 150), element_justification='center')

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Add": 
         
        def save_info():            
            name_text=entry_n.get()
            task_text=entry_t.get()
            start_text=entry_s.get()
            finish_text=entry_f.get()
            # l = Label(add,text=name_text+"-"+task_text+"-"+start_text+"-"+finish_text )
            # l.pack()
            entry_n.delete(0, END)
            entry_t.delete(0, END)
            entry_s.delete(0, END)
            entry_f.delete(0, END)
            db.insert_task(name_text,start_text,finish_text,task_text)
            label = Label(add, text="Task saved sucessfully!", bg='light blue', fg='green', font='Any 10')
            label.pack()
            
        add = Tk()
        add.geometry("600x300")
        add.title("Adding")
        add.configure(bg='light blue')
        
        label1 = Label(add,
            text ="Name:",
            foreground="blue",
            bg='light blue',
            font='Any 10')
        label1.pack()
        entry_n=Entry(add)
        entry_n.pack()
        
        label2 = Label(add,
            text ="Task:",
            foreground="red",
            bg='light blue',
            font='Any 10')
        label2.pack()
        entry_t=Entry(add)
        entry_t.pack()
        
        label3 = Label(add,
            text ="Start Time:",
            foreground="green",
            bg='light blue',
            font='Any 10')
        label3.pack()
        entry_s=Entry(add)
        entry_s.pack()
        
        label4 = Label(add,
            text ="Finish Time:",
            foreground="purple",
            bg='light blue',
            font='Any 10')
        label4.pack()
        entry_f=Entry(add)
        entry_f.pack()
        """
        label3 = Label(add,
            text ="Start Time:",
            foreground="green")
        label3.pack()
        
        start = Scrollbar(add)

        year_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for year in range(2000,2051):
            year_list.insert(END, 'Year ' + str(year))
        year_list.pack()
        
        month_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for month in range(1,13):
            month_list.insert(END, 'Month ' + str(month))
        month_list.pack()
        
        day_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for day in range(1,32):
            day_list.insert(END, 'Day ' + str(day))
        day_list.pack()
        
        start.config(command = year_list.yview and month_list.yview and day_list.yview)

        label4 = Label(add,
            text ="Finish Time:",
            foreground="purple")
        label4.pack()
        
        finish = Scrollbar(add)

        year_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        for year in range(2000,2051):
            year_list.insert(END, 'Year ' + str(year))
        year_list.pack()
        
        #month_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        #for month in range(1,13):
        #    month_list.insert(END, 'Month ' + str(month))
        #month_list.pack()
        
        #day_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        #for day in range(1,32):
        #    day_list.insert(END, 'Day ' + str(day))
        #day_list.pack()
        
        finish.config(command = year_list.yview)
        """ 
        
        bt = Button(add,
                    text ="Submit", command=save_info, bg='sky blue')
        bt.pack()

    elif event == "Remove":
        def remove_info():
            person=entry.get()
            db.remove_task(person)
            entry.delete(0, END)
            label = Label(eliminate, text="Task removed sucessfully!", fg='green', bg='gold2', font='Any 10')
            label.pack()
            
        eliminate = Tk()
        eliminate.geometry("600x300")
        eliminate.title("Removing")
        eliminate.configure(bg='gold2')
        
        label1 = Label(eliminate,
            text = db.get_all_tasks(), bg='gold2')
        label1.pack() 
        label2 = Label(eliminate,
            text ="Task ID:",
            foreground="blue",
            bg='gold2',
            font='Any 10')
        label2.pack()
        entry = Entry(eliminate)
        entry.pack() 
        bt = Button(eliminate,
                    text ="Submit", command=remove_info, bg='sky blue')
        bt.pack()
    
    elif event == "Tasks": 
        def destroy():
            show_tasks.destroy()

        show_tasks = Tk()
        show_tasks.geometry("600x300")
        show_tasks.title("Tasks")
        show_tasks.configure(bg='SpringGreen2')
        
        label1 = Label(show_tasks,
            text = db.get_all_tasks(),
            bg='SpringGreen2')
        label1.pack() 
        bt = Button(show_tasks,
                    text ="OK", command=destroy, bg='sky blue')
        bt.pack()
        
    elif event == "Person Task":
        def show_person_tasks():
            name=name_e.get()
            label2 = Label(show_task,
                text = db.get_person_tasks(name),
                bg='PaleGreen3')
            name_e.delete(0, END)
            label2.pack() 
            
        show_task = Tk()
        show_task.geometry("600x300")
        show_task.title("Person Tasks")
        show_task.configure(bg='PaleGreen3')
  
        label1 = Label(show_task,
            text ="Name:",
            foreground="blue", bg='PaleGreen3', font='Any 10')
        label1.pack()
        name_e = Entry(show_task)
        name_e.pack()
        
        bt = Button(show_task,
                    text ="Submit", command=show_person_tasks, bg='sky blue')
        bt.pack()
    
    elif event == "Plot":
        
        def all_people():
            
            show_table = Tk()
            show_table.geometry("600x300")
            show_table.title("table")
            table_frame = Frame(show_table)
            table_frame.pack()
            my_table = ttk.Treeview(table_frame)
            my_table['columns'] = ('id', 'name', 'task', 'start', 'finish' , 'duration')
        
            my_table.column("#0", width=0,  stretch=NO)
            my_table.column("id",anchor=CENTER, width=80)
            my_table.column("name",anchor=CENTER,width=80)
            my_table.column("task",anchor=CENTER,width=80)
            my_table.column("start",anchor=CENTER,width=80)
            my_table.column("finish",anchor=CENTER,width=80)
            my_table.column("duration",anchor=CENTER,width=80)
        
            my_table.heading("#0",text="",anchor=CENTER)
            my_table.heading("id",text="Id",anchor=CENTER)
            my_table.heading("name",text="Name",anchor=CENTER)
            my_table.heading("task",text="Task",anchor=CENTER)
            my_table.heading("start",text="Start",anchor=CENTER)
            my_table.heading("finish",text="Finish",anchor=CENTER)
            my_table.heading("duration",text="Duration",anchor=CENTER)
        
            id_list,name_list,task_list,start_list,finish_list,duration_list=gp.plot_show()
            for i in range(len(id_list)):
                my_table.insert(parent='',index='end',iid=i,text='',
                values=(str(id_list[i]),str(name_list[i]),str(task_list[i]),str(start_list[i]),str(finish_list[i]),str(duration_list[i])))
            
            my_table.pack()
                
        
        def one_person():
            
            def person_info():
                table1_frame = Frame(show_table1)
                table1_frame.pack()
                my_table1 = ttk.Treeview(table1_frame)
                my_table1['columns'] = ('id', 'task', 'start', 'finish' , 'duration')
        
                my_table1.column("#0", width=0,  stretch=NO)
                my_table1.column("id",anchor=CENTER, width=80)
                my_table1.column("task",anchor=CENTER,width=80)
                my_table1.column("start",anchor=CENTER,width=80)
                my_table1.column("finish",anchor=CENTER,width=80)
                my_table1.column("duration",anchor=CENTER,width=80)
        
                my_table1.heading("#0",text="",anchor=CENTER)
                my_table1.heading("id",text="Id",anchor=CENTER)
                my_table1.heading("task",text="Task",anchor=CENTER)
                my_table1.heading("start",text="Start",anchor=CENTER)
                my_table1.heading("finish",text="Finish",anchor=CENTER)
                my_table1.heading("duration",text="Duration",anchor=CENTER)
                # text=Text(show_table1, width=80, height=15)
                # text.pack()
                person=table_e.get()
                id_list,task_list,start_list,finish_list,duration_list=gp.plot1_show(person)
                for i in range(len(id_list)):
                    # text.insert(END,str(id_list)+" "+str(task_list)+" "+str(start_list)+" "+str(finish_list)+" "+str(duration_list))
                    my_table1.insert(parent='',index='end',iid=i,text='',
                    values=(str(id_list[i]),str(task_list[i]),str(start_list[i]),str(finish_list[i]),str(duration_list[i])))
                my_table1.pack()
                table_e.delete(0, END)
            
            show_table1 = Tk()
            show_table1.geometry("600x300")
            show_table1.title("Table")
            label1 = Label(show_table1,
                text ="Name:",
                foreground="blue", font='Any 10')
            label1.pack()
            table_e = ttk.Entry(show_table1)
            table_e.pack() 
            bt = Button(show_table1,
                        text ="Submit", command=person_info, bg='sky blue')
            bt.pack()
        
        plot = Tk()
        plot.geometry("600x300")
        plot.title("Plot")
        plot.configure(bg='light blue')
        
        label1 = Label(plot,
            text ="Select the option you want:",
            foreground="green",bg='light blue', font='Any 10')
        label1.pack()
        
        bt = Button(plot,
                    text ="All People", command=all_people, bg='gold')
        bt.pack()
        
        bt2 = Button(plot,
                     text="One Person", command=one_person, bg='cyan2')
        bt2.pack()
         
    mainloop()
                     
window.close()
