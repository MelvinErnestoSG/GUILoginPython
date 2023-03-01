from customtkinter import *

set_appearance_mode('System')  # Modes: system (default), light, dark.
set_default_color_theme('blue')  # Themes: blue (default), dark-blue, green.

# create CTk window.
root = CTk()
root.title('Login')
root.eval('tk::PlaceWindow . center')
root.geometry("200x270+800+300")
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
    # --------------------------------------------------#
    label = CTkLabel(master=frame, text='CTkProgressBar')
    label.pack(pady=10)
    # ---------------------------------------#
    progressbar = CTkProgressBar(master=frame)
    progressbar.pack(pady=10)
    # -----------------------------#
    switch = CTkSwitch(master=frame)
    switch.pack(pady=10)
    # -----------------------------------------------------------------------------------------------#
    combobox = CTkComboBox(master=frame, values=['Option 1","Option 2","Option 42 long long long...'])
    combobox.pack(pady=10)
    combobox.set('CTkComboBox')
    # ----------------------------------------------------------------------------------------------------#
    option_menu = CTkOptionMenu(master=frame, values=['Option 1","Option 2","Option 42 long long long...'])
    option_menu.pack(pady=10)
    option_menu.set('CTkOptionMenu')
    # -----------------------------#
    radiobutton_var = IntVar(value=1)

    radiobutton_1 = CTkRadioButton(master=frame, variable=radiobutton_var, value=1)
    radiobutton_1.pack(pady=10)

    radiobutton_2 = CTkRadioButton(master=frame, variable=radiobutton_var, value=2)
    radiobutton_2.pack(pady=10)
    # -----------------------------------------------------#
    checkbox = CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=10)
    # --------------------------------------------------#
    text = CTkTextbox(master=frame, width=200, height=70)
    text.pack(pady=10)
    text.insert("0.0", "CTkTextbox\n\n\n\n")
    # ---------------------------------------------------------------------------------#
    button = CTkButton(master=frame, text='Close', cursor='hand2', command=root.destroy)
    button.pack(pady=10)


def error():
    root.withdraw()
    window = CTkToplevel()
    window.title('Error')
    window.geometry('370x120+800+300')
    window.resizable(False, False)
    # ---------------------------#
    frame = CTkFrame(master=window)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    # -----------------------------------------------------------------------#
    label = CTkLabel(master=frame, text='Username and password are incorrect.')
    label.pack(pady=10)
    # ---------------------------------------------------------------------------------#
    button = CTkButton(master=frame, text='Close', cursor='hand2', command=root.destroy)
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


frameLogin = CTkFrame(master=root)
frameLogin.pack(pady=10, padx=10, fill='both', expand=True)

labelLogin1 = CTkLabel(master=frameLogin, text='User Name')
labelLogin1.pack(pady=10)

entryLogin1 = CTkEntry(master=frameLogin, textvariable=user)
entryLogin1.pack(pady=10)

labelLogin2 = CTkLabel(master=frameLogin, text='Password')
labelLogin2.pack(pady=10)

entryLogin2 = CTkEntry(master=frameLogin, textvariable=password, show='*')
entryLogin2.pack(pady=10)

buttonLogin = CTkButton(master=frameLogin, text='Enter', cursor='hand2', command=login)
buttonLogin.pack(pady=10)

root.mainloop()
