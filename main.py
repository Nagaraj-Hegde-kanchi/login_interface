from customtkinter import *
import csv
from tkinter import messagebox
from PIL import Image

def login():
    messagebox.showinfo("Success", "Logged In")
    win.destroy()

def check_userdata(email, password):
    with open("user_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email and row[1] == password:
                return True

def create_account(email, password):
    file = open("user_data.csv", "a")
    print(f"\n{email},{password}")
    messagebox.showinfo("acount_creation", "new account created succesfuly")
    

def verify_email(email):
    return "@" in email and "." in email

def LogIn():
    email_data = email.get()
    passaward_data=passward.get()
    while email.get()!="":
        email.delete(0)
    while passward.get()!="":
        passward.delete(0)
    if not (verify_email(email_data)):
        messagebox.showerror("Error", "Invalid Email")
        return
    else:
        x = check_userdata(email_data, passaward_data)
        if x:
            login()
        else:
            create_account(email_data, passaward_data)
            login()
win = CTk()
win.geometry("600x480")

app = CTkFrame(master=win, height=600, width=480)
app.pack()

side_img_data = Image.open("C:\\coding folder\\customtkinter\\login_interface\\side-img.png")
email_icon_data = Image.open("C:\\coding folder\\customtkinter\\login_interface\\email-icon.png")
password_icon_data = Image.open("C:\\coding folder\\customtkinter\\login_interface\\password-icon.png")
google_icon_data = Image.open("C:\\coding folder\\customtkinter\\login_interface\\google-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
email = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
email.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
passward = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
passward.pack(anchor="w", padx=(25, 0))

log_in = CTkButton(master=frame, text="Login", 
                   fg_color="#601E88", hover_color="#E44982", 
                   font=("Arial Bold", 12), text_color="#ffffff",
                   width=225, command=LogIn)
log_in.pack(anchor="w", pady=(21, 0), padx=(25, 0))

google_login = CTkButton(master=frame, text="Continue With Google", 
                        fg_color="#EEEEEE",
                        hover_color="#EEEEEE",
                        font=("Arial Bold", 9), 
                        text_color="#601E88", 
                        width=225, 
                        image=google_icon,

                         )
google_login.pack(anchor="w", pady=(21, 0), padx=(25, 0))
win.mainloop()
