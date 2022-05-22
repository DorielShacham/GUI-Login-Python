from tkinter import *
from tkinter import messagebox

def login(): # login function to check if the username and password is correct
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("Login","Please enter your username and password")

    elif (username=="Doriel" and password=="Shacham123"):
        messagebox.showinfo("","Log in successful")

    else:
        messagebox.showinfo("","Incorrect username or password")



root = Tk() # Create a window
root.title("Doriel Login") # Title of the window
root.geometry("400x400") # Size of the window

global entry1 #global variable
global entry2 #global variable

#Box of Username + Password
Label(root, text="Username").place(x=20, y=20) # x, y  Username label
Label(root, text="Password").place(x=20, y=70) # x, y   Password label

#Box of Username + Entry
entry1 = Entry(root,bd=5) # bd = border width = 5 pixels
entry1.place(x=140, y=20) # x, y = position
#Box of Password + Entry
entry2 = Entry(root,bd=5) # bd = border width = 5 pixels
entry2.place(x=140, y=70) # x, y = position

#Button Login
Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120) # x, y = position of the button


root.mainloop() # Start the window