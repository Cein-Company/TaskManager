import sqlite3

conn = sqlite3.connect("tasks.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks (person TEXT, task TEXT)''')

def insert_task(person, task):
    c.execute("INSERT INTO tasks VALUES (?,?)", (person, task))
    conn.commit()

def get_person_tasks(person):
    c.execute("SELECT * FROM tasks WHERE person=?", (person,))
    return c.fetchall()

def get_all_tasks():
    c.execute("SELECT * FROM tasks")
    return c.fetchall()

def remove_task(person):
    c.execute("DELETE FROM tasks WHERE person=?", (person,))
    conn.commit()
