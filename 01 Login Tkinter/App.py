from tkinter import*
from tkinter import messagebox

# Create a new tkinter window for the login screen.
root = Tk()
root.title('Window Login')
root.eval('tk::PlaceWindow . center')
root.geometry("250x107+640+370")
root.resizable(False, False)

# Add labels for username to the window.
label_user = Label(root, text='Username')
label_user.pack()

# Add username entry boxes to the window.
entry_username = Entry(root)
entry_username.pack()

# Add labels for password to the window.
label_pass = Label(root, text='Password')
label_pass.pack()

# Add password entry boxes to the window.
entry_password = Entry(root, show='*')
entry_password.pack()


def login():
    # Function to verify login credentials.
    user_name = entry_username.get()
    user_password = entry_password.get()

    # Clear the entry fields after login verification.
    entry_username.delete(0, END)
    entry_password.delete(0, END)

    # Check if the entered username and password match a valid pair.
    if user_name == 'admin' and user_password == '1234':
        # If the login is successful, display a message and close the login window.
        messagebox.showinfo('Login successful', 'Your username and password are correct.')
        root.destroy()
    else:
        # If the login fails, display an error message
        messagebox.showerror('Login failed', 'Incorrect username or password')


# Add button to submit login information.
button_login = Button(root, text='Enter', cursor='hand2', command=login)
button_login.pack()

# Display the window.
root.mainloop()
