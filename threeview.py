from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    import sqlite3
    conn = sqlite3.connect('example.db')

    c = conn.cursor()

# Create table
    c.execute('''CREATE TABLE stocks
             (date text, trans text)''')

# Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY')")

# Save (commit) the changes
    conn.commit()

    conn.close()

def View():
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stocks")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("400x400")

tree= ttk.Treeview(root, column=("column1", "column2"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")

tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()