import tkinter as tk
from tkinter import messagebox, PhotoImage, Image

USER_DATA_FILE = "username_and_password.txt"


window = tk.Tk()
window.title('Login and Registration System')
window.geometry("925x500+300+200")
window.config(bg='#fff')
window.resizable(False,False)

img = PhotoImage(file="D:\DownloadFromMicrosoftBrowser\login.png")
tk.Label(window, image=img, bg='white').place(x=50,y=50)

login_frame = tk.Frame(window, width=350, height=350, bg='white')
login_frame.place(x=480, y=70)

login_heading=tk.Label(login_frame, text='Sign in', fg='#57a1f8', bg='white', font=('Arial', 20, 'bold'))
login_heading.place(x=100, y=5)
username_entry = tk.Entry(login_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))


# Load eye images (Make sure you have eye_open.png and eye_closed.png)
eye_open_img = PhotoImage(file='eye-open.png').subsample(25)
eye_closed_img = PhotoImage(file='eye-closed.png').subsample(8)

# Functions
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        eye_button.config(image=eye_open_img)
    else:
        password_entry.config(show='*')
        eye_button.config(image=eye_closed_img)

def toggle_create_password():
    if create_password_entry.cget('show') == '*':
        create_password_entry.config(show='')
        eye_button_create.config(image=eye_open_img)
    else:
        create_password_entry.config(show='*')
        eye_button_create.config(image=eye_closed_img)

def toggle_confirm_password():
    if confirm_password_entry.cget('show') == '*':
        confirm_password_entry.config(show='')
        eye_button_confirm.config(image=eye_open_img)
    else:
        confirm_password_entry.config(show='*')
        eye_button_confirm.config(image=eye_closed_img)

def on_enter(e):
    if username_entry.get() == 'Username':
        username_entry.delete(0, 'end')

def on_leave(e):
    if username_entry.get() == '':
        username_entry.insert(0, "Username")

def p_on_enter(e):
    if password_entry.get() == 'Password':
        password_entry.delete(0, 'end')
        password_entry.config(show='*')

def p_on_leave(e):
    if password_entry.get() == '':
        password_entry.config(show="")
        password_entry.insert(0, "Password")

def on_enter_password(e):
    if create_password_entry.get() == 'Create Password':
        create_password_entry.delete(0, 'end')
        create_password_entry.config(show="*")  # Hide password when typing

def on_leave_password(e):
    if create_password_entry.get() == '':
        create_password_entry.config(show="")  # Show text again
        create_password_entry.insert(0, 'Create Password')

def on_enter_confirm_password(e):
    if confirm_password_entry.get() == 'Confirm Password':
        confirm_password_entry.delete(0, 'end')
        confirm_password_entry.config(show="*")  # Hide password when typing

def on_leave_confirm_password(e):
    if confirm_password_entry.get() == '':
        confirm_password_entry.config(show="")  # Show text again
        confirm_password_entry.insert(0, 'Confirm Password')

def on_enter_username(e):
    if create_name_entry.get() == 'Create Username':
        create_name_entry.delete(0, 'end')

def on_leave_username(e):
    if create_name_entry.get() == '':
        create_name_entry.insert(0, 'Create Username')

def login():
    #####----------------------------------------------------------
    username = username_entry.get()
    password = password_entry.get()

    with open(USER_DATA_FILE, 'r') as file:
        data = file.readlines()
        for line in data:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", "Successfully Logged In!")
                return

    retry = messagebox.showerror("Error", "Incorrect username or password.")
    return

def register_user():
    create_username = create_name_entry.get()
    create_password = create_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if create_username == 'Create Username' or create_password == 'Create Password' or confirm_password == 'Confirm Password':
        messagebox.showerror("Error", "All fields are required.")
        return

    if create_password != confirm_password:
        messagebox.showerror("Error", "Write same passwords")
        return
    

    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{create_username} {create_password}\n")

    messagebox.showinfo("Success", "Successfully Registered!")
    show_login_screen()  # Redirect to login screen after registration

def register():
    for widget in window.winfo_children():
        widget.destroy()

    global Img
    Img = PhotoImage(file="D:\DownloadFromMicrosoftBrowser\sign_up.png")
    tk.Label(window, image=Img, bg='white').place(x=50, y=55)

    global reg_frame, reg_heading
    reg_frame = tk.Frame(window, width=350, height=350, bg='white')
    reg_frame.place(x=480, y=70)

    reg_heading = tk.Label(reg_frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Arial', 20, 'bold'))
    reg_heading.place(x=100, y=5)

    global create_name_entry, create_password_entry, confirm_password_entry

    # Create Username Entry
    create_name_entry = tk.Entry(reg_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))
    create_name_entry.place(x=30, y=80)
    create_name_entry.insert(0, 'Create Username')
    create_name_entry.bind('<FocusIn>', on_enter_username)
    create_name_entry.bind('<FocusOut>', on_leave_username)

    tk.Frame(reg_frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Create Password Entry
    create_password_entry = tk.Entry(reg_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))
    create_password_entry.place(x=30, y=150)
    create_password_entry.insert(0, 'Create Password')
    create_password_entry.bind('<FocusIn>', on_enter_password)
    create_password_entry.bind('<FocusOut>', on_leave_password)

    tk.Frame(reg_frame, width=295, height=2, bg='black').place(x=25, y=177)

    global eye_button_create
    eye_button_create = tk.Button(reg_frame, image=eye_closed_img, command=toggle_create_password, borderwidth=0, bg='white')
    eye_button_create.place(x=290, y=150)

    # Confirm Password Entry
    confirm_password_entry = tk.Entry(reg_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))
    confirm_password_entry.place(x=30, y=220)
    confirm_password_entry.insert(0, 'Confirm Password')
    confirm_password_entry.bind('<FocusIn>', on_enter_confirm_password)
    confirm_password_entry.bind('<FocusOut>', on_leave_confirm_password)

    tk.Frame(reg_frame, width=295, height=2, bg='black').place(x=25, y=247)

    global eye_button_confirm
    eye_button_confirm = tk.Button(reg_frame, image=eye_closed_img, command=toggle_confirm_password, borderwidth=0, bg='white')
    eye_button_confirm.place(x=290, y=220)  # Adjust position

    tk.Button(reg_frame, pady=5, width=39, text="Sign up", bg='#57a1f8', fg='white', border=0, command=register_user).place(x=35, y=270)

    tk.Button(reg_frame, text="Back to Login", bg='white', fg='blue', border=0, font=('Arial', 8, 'bold'),
              cursor='hand2', command=show_login_screen).place(x=135, y=310)

def show_login_screen():
    for widget in window.winfo_children():  # Destroy all existing widgets
        widget.destroy()

    global img
    img = PhotoImage(file="D:\DownloadFromMicrosoftBrowser\login.png")
    tk.Label(window, image=img, bg='white').place(x=50, y=50)

    global login_frame
    login_frame = tk.Frame(window, width=350, height=350, bg='white')
    login_frame.place(x=480, y=70)

    global login_heading
    login_heading = tk.Label(login_frame, text='Sign in', fg='#57a1f8', bg='white', font=('Arial', 20, 'bold'))
    login_heading.place(x=100, y=5)

    global username_entry

    username_entry = tk.Entry(login_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))
    username_entry.place(x=30, y=80)
    username_entry.insert(0, 'Username')
    username_entry.bind('<FocusIn>', on_enter)
    username_entry.bind('<FocusOut>', on_leave)

    tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=107)

    global password_entry
    password_entry = tk.Entry(login_frame, width=25, fg='black', border=0, bg='white', font=('Arial', 10, 'bold'))
    password_entry.place(x=30, y=150)
    password_entry.insert(0, 'Password')
    password_entry.bind('<FocusIn>', p_on_enter)
    password_entry.bind('<FocusOut>', p_on_leave)

    tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=177)

    global eye_button


    eye_button = tk.Button(login_frame, image=eye_closed_img, command=toggle_password, borderwidth=0, bg='white')
    eye_button.place(x=290, y=150)

    tk.Button(login_frame, pady=5, width=39, text="Sign in", bg='#57a1f8', fg='white', border=0, command=login).place(x=35, y=204)

    label = tk.Label(login_frame, text="Don't have an account?", fg='black', bg='white', font=('Arial', 8))
    label.place(x=92, y=270)

    sign_up = tk.Button(login_frame, width=6, text='Sign up', border=0, bg='white', fg='blue', cursor='hand2',
                        font=('Arial', 8), command=register)
    sign_up.place(x=215, y=270)


show_login_screen()  # Start with the login screen

window.mainloop()