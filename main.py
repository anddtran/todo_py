#tasks app built using python and tkinter
#author: Andrew Tran

import tkinter as tk            # importing the tkinter module as tk  
from tkinter import *
from tkinter import messagebox  # importing the messagebox module from the tkinter library  
from PIL import ImageTk, Image  
import os     

tasks = []

def readtasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip())

def writetasks():
    with open('tasks.txt', 'w') as file:
        for item in tasks:
            file.write(f'{item}\n')

def add_task(event=None):
    new_task = new_task_entry.get()
    if not new_task:
        messagebox.showinfo('error', 'you didn\'t add anything!')
    else:
        tasks.append(new_task)
        update_listbox()
        new_task_entry.delete(0, 'end')
        writetasks()

def deletetask(event=None):
    index = listbox.curselection()[0]
    tasks.pop(index)
    update_listbox()
    writetasks()

def on_keypress(event):
    if event.keysym == 'BackSpace':
        try:
            deletetask()
        except IndexError:  # if no item is selected or list is empty
            messagebox.showinfo('Error', 'No task selected to delete!')
    elif event.keysym == 'Escape':
        root.destroy()

def on_keypresstask(event):
    if event.keysym == 'BackSpace':
        try:
            new_task_entry.delete(0, 'end')
        except IndexError:  # if no item is selected or list is empty
            messagebox.showinfo('Error', 'No task selected to delete!')
    elif event.keysym == 'Escape':
        root.destroy()
    elif event.keysym =='Return':
        add_task()

def next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

def update_listbox():
    listbox.delete(0, tk.END)
    for item in tasks:
        listbox.insert(tk.END, item)
    listbox.selection_set(0)
    listbox.activate(0)

if __name__ == '__main__':
    # Create the window
    root = tk.Tk()
    root.title('Todo')
    root.geometry('400x600') 
    root.resizable(False, False)

    #topframe
    topframe = Frame(root, width='400', height='125', bg='#32405b')
    topframe.pack()

    # Background image
    bgimage = Image.open('ds.png')
    bgresize = bgimage.resize((72, 72), Image.NEAREST)
    tkimage = ImageTk.PhotoImage(bgresize)
    tkbg = tk.Label(root, image=tkimage)
    tkbg.place(relx=0.5, rely=0.09, anchor='center')  

    # Title
    label = tk.Label(root, text='To-Do List', font= 'arial 20 bold', fg= 'white', bg='#32405b')
    label.place(relx=0.5, rely=0.18, anchor='center')

    #entry frame
    entryframe = Frame(root, width='350', height='20', bg='white', pady=20)
    entryframe.pack(pady=6)
    new_task_entry = tk.Entry(entryframe, width=42, fg='black', bg='white', justify='center')
    new_task_entry.place(relx=0.5, rely=0.5, anchor='center')
    new_task_entry.focus()
    new_task_entry.bind('<Key>', on_keypresstask)
    new_task_entry.bind('Tab', next_widget)

    #listbox frame
    listboxframe = Frame(root, bd=3, width='330', height='400', bg='white')
    listboxframe.pack()

    # Listbox widget
    listbox = tk.Listbox(listboxframe, width=40, height=23, bg='#32405b') 
    listbox.pack(side=LEFT, fill=BOTH) # Center of the window
    listbox.bind("<Key>", on_keypress)
    listbox.bind('Tab', next_widget)

    #scrollbar
    #scroll = Scrollbar(listboxframe)
    #scroll.pack(side=RIGHT, fill=BOTH)
    #listbox.config(yscrollcommand=scroll.set)
    #scroll.config(command=listbox.yview)

    # Add task button
    button = tk.Button(root, text='Add Task', command=add_task)
    button.place(relx=0.3, rely=0.955, anchor='center')  # Moved up slightly

    # Add delete button
    deleteitem = tk.Button(root, text='Delete', command=deletetask)
    deleteitem.place(relx=0.7, rely=0.955, anchor='center')  # Moved up slightly

    readtasks()
    update_listbox()

    root.mainloop()