from tkinter import *

class loginpage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1680x1050")
        self.root.title("Admin LOGIN")
        Frame_bg = Frame(self.root, bg="yellow")
        Frame_bg.place(width=1680, height=1050)
        heading=Label(text="Welcome To Student Management System", bg="yellow", font="timesnewroman 15 bold")
        heading.pack(side="top",fill=X)

        # Frame for log in
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=600,y=100,width=450,height=400)

        # Log In here TEXT
        title = Label(Frame_login,text="Login Here",font="Impact 35 bold",fg="#d77337",bg="white").place(x=120,y=20)

        # Admin Login
        Admin_login = Label(Frame_login, text="Admin Login", font="Goudyoldstyle 15 bold", fg="#d77337", bg="white").place(x=170, y=100)

        # user name as text
        user = Label(Frame_login, text="Username",font="Goudyoldstyle 15 bold", fg="Gray",bg="white").place(x=120,y=130)

        # user name Entry
        user_entry=Entry(Frame_login,font="timesnewroman 15", bg="lightgray").place(x=125, y=160)

        # user name as text
        user_password = Label(Frame_login, text="Password", font="Goudyoldstyle 15 bold", fg="Gray", bg="white").place(x=120, y=190)

        # user name Entry
        user_password = Entry(Frame_login, font="timesnewroman 15", bg="lightgray").place(x=125, y=220)

        # Button Login
        log_button = Button(Frame_login, text="LOGIN",width=15,height=2).place(x=170, y=270)


root=Tk()
obj = loginpage(root)
root.mainloop()