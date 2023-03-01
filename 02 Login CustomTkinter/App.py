from customtkinter import *

set_appearance_mode('System')  # Modes: system (default), light, dark.
set_default_color_theme('blue')  # Themes: blue (default), dark-blue, green.

# create CTk window.
root = CTk()
root.title('Login')
root.eval('tk::PlaceWindow . center')
root.geometry("200x180+800+300")
root.resizable(False, False)


# create CTk window 2.
def access():
    root.withdraw()
    window = CTkToplevel()
    window.title('Access')
    window.geometry('300x510+800+200')
    window.resizable(False, False)

    # ----------------------------#
    frame = CTkFrame(master=window)
    frame.pack(pady=10, padx=10, fill='both', expand=True)

    # Add label for the window 2.
    label = CTkLabel(master=frame, text='CTkProgressBar')
    label.pack(pady=10)

    # Add progress bar for the window 2.
    progressbar = CTkProgressBar(master=frame)
    progressbar.pack(pady=10)

    # Add switch for the window 2.
    switch = CTkSwitch(master=frame)
    switch.pack(pady=10)

    # Add combo box for the window 2.
    combobox = CTkComboBox(master=frame, values=['Option 1","Option 2","Option 42 long long long...'])
    combobox.pack(pady=10)
    combobox.set('CTkComboBox')

    # Add option menu for the window.
    option_menu = CTkOptionMenu(master=frame, values=['Option 1","Option 2","Option 42 long long long...'])
    option_menu.pack(pady=10)
    option_menu.set('CTkOptionMenu')

    # Add radio button for the window 2.
    radiobutton_var = IntVar(value=1)

    radiobutton_1 = CTkRadioButton(master=frame, variable=radiobutton_var, value=1)
    radiobutton_1.pack(pady=10)

    radiobutton_2 = CTkRadioButton(master=frame, variable=radiobutton_var, value=2)
    radiobutton_2.pack(pady=10)

    # Add check box for the window 2.
    checkbox = CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=10)

    # Add textbox for the window 2.
    text = CTkTextbox(master=frame, width=200, height=70)
    text.pack(pady=10)
    text.insert("0.0", "CTkTextbox\n\n\n\n")

    # Add button to close the window 2.
    button = CTkButton(master=frame, text='Close', cursor='hand2', command=root.destroy)
    button.pack(pady=10)


def error():
    root.withdraw()
    window = CTkToplevel()
    window.title('Error')
    window.geometry('370x120+800+300')
    window.resizable(False, False)

    # Add frame for the window error.
    frame = CTkFrame(master=window)
    frame.pack(pady=10, padx=10, fill='both', expand=True)

    # Add labels for message to the window.
    label = CTkLabel(master=frame, text='Username and password are incorrect.')
    label.pack()

    # Add button to submit login information.
    button = CTkButton(master=frame, text='Close', cursor='hand2', command=root.destroy)
    button.pack(pady=10)


# Add frame for the login window.
frame_login = CTkFrame(master=root)
frame_login.pack(pady=10, padx=10, fill='both', expand=True)

# Add labels for username to the window.
label_username = CTkLabel(master=frame_login, text='Username')
label_username.pack()

# Add username entry boxes to the window.
entry_username = CTkEntry(master=frame_login)
entry_username.pack()

# Add labels for password to the window.
label_pass = CTkLabel(master=frame_login, text='Password')
label_pass.pack()

# Add password entry boxes to the window.
entry_password = CTkEntry(master=frame_login, show='*')
entry_password.pack()


def login():
    user_name = entry_username.get()
    user_password = entry_password.get()
    if user_name == 'admin' and user_password == '1234':
        access()
    else:
        error()


# Add button to submit login information.
button_login = CTkButton(master=frame_login, text='Enter', cursor='hand2', command=login)
button_login.pack(pady=10)

# Display the window.
root.mainloop()
