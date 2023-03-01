from tkinter import *
from tkinter import messagebox

# create Tk window.
root = Tk()
root.title('Login')
root.eval('tk::PlaceWindow . center')
root.geometry("200x280+800+300")
root.resizable(False, False)


# create Tk window 2.


def access():
    messagebox.showinfo("Access", "Welcome")
    button = Button(root, text='Close', cursor='hand2', font='20', command=root.destroy)
    button.pack(pady=10)


def error():
    messagebox.showerror("Error", "Username and password are incorrect.")
    button = Button(root, text='Close', cursor='hand2', font='20', command=root.destroy)
    button.pack(pady=10)


user = StringVar()
password = StringVar()


def login():
    user_name = user.get()
    user_password = password.get()
    if user_name == 'admin' and user_password == '1234':
        access()
    else:
        error()


labelLogin1 = Label(root, text='User Name', font='20')
labelLogin1.pack(pady=10)

entryLogin1 = Entry(root, textvariable=user,)
entryLogin1.pack(pady=10)

labelLogin2 = Label(root, text='Password', font='20')
labelLogin2.pack(pady=10)

entryLogin2 = Entry(root, textvariable=password, show='*')
entryLogin2.pack(pady=10)

buttonLogin = Button(root, text='Enter', cursor='hand2', font='20', command=login)
buttonLogin.pack(pady=10)

root.mainloop()
