from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def logout():
    os.system("shutdown -l")

    
def shutdown():
    os.system("shutdown /s /t /1")

st = Tk()
st.title("Power Options")
st.geometry("500x500")
st.config(bg = "Black")

label1 = Label(st, text="All Power Options : ", font=("Helvetica", 18),fg = "white",bg = "Black")
label1.place(x = 140,y = 10)

restartButton = Button(st,text = "Restart",font=("Helvetica",16,"bold"),relief=GROOVE,fg="White",bg = "Black",command=restart)
restartButton.place(x = 170 , y=50 ,height=50 , width=150)

ShutDownButton = Button(st, text="Shutdown", font=("Helvetica", 16, "bold"), relief=GROOVE, fg="White", bg="Black",command=shutdown)
ShutDownButton.place(x=169, y=130, height=50, width=150)

LogOutButton = Button(st, text="Log Out", font=("Helvetica", 16, "bold"), relief=GROOVE, fg="White", bg="Black",command = logout)
LogOutButton.place(x=169, y=210, height=50, width=150)

st.mainloop()
