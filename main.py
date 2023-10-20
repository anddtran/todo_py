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
    elif event.keysym == 'Return':
        create_popup()
    elif event.keysym == 'Escape':
        root.destroy()

def update_listbox():
    listbox.delete(0, tk.END)
    for item in tasks:
        listbox.insert(tk.END, item)
    listbox.selection_set(0)
    listbox.activate(0)

def create_popup():
    #popup creation and title
    global popup, new_task_entry
    popup = tk.Toplevel()
    popup.title('Add Item')

    #popup task entry field with focus
    new_task_entry = tk.Entry(popup)
    new_task_entry.pack()
    new_task_entry.focus()
    new_task_entry.bind("<Return>",add_task)

    popup.bind("<Escape>", lambda event: popup.destroy())

    #add button for those who like buttons
    confirm_button = tk.Button(popup, text="Add", command=add_task)
    confirm_button.pack()

if __name__ == '__main__':
    # Create the window
    root = tk.Tk()
    root.title('Todo')
    root.geometry('400x600')  # Consider making the window a bit larger if needed
    root.resizable(False, False)

    # Background image
    bgimage = Image.open('ds.png')
    bgresize = bgimage.resize((50, 50), Image.NEAREST)
    tkimage = ImageTk.PhotoImage(bgresize)
    tkbg = tk.Label(root, image=tkimage)
    tkbg.place(relx=0.5, rely=0.1, anchor='center')  # Adjusted position

    # Title
    label = tk.Label(root, text='List', fg= 'white')
    label.place(relx=0.5, rely=0.18, anchor='center')  # Moved down slightly
    

    # Listbox widget
    listbox = tk.Listbox(root, width=30, height=20)  # Reduced height to fit buttons
    listbox.place(relx=0.5, rely=0.5, anchor='center')  # Center of the window

    listbox.focus_set()
    listbox.bind("<Key>", on_keypress)
    readtasks()
    update_listbox()

    # Add task button
    button = tk.Button(root, text='Add Task', command=create_popup)
    button.place(relx=0.3, rely=0.85, anchor='center')  # Moved up slightly

    # Add delete button
    deleteitem = tk.Button(root, text='Delete', command=deletetask)
    deleteitem.place(relx=0.7, rely=0.85, anchor='center')  # Moved up slightly

    label.lift()
    root.mainloop()