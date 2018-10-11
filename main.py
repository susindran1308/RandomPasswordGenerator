from tkinter import *
import desroot
import generateOTP
import users

class Main:

    def mainfunc(self):
        try:
            root.destroy()
        finally:
            desroot.Option().labels()

    def otp(self):
        try:
            root.destroy()
        finally:
            generateOTP.OtpGeneration().maildet()

    def userpass(self):
        root.destroy()
        users.Passwords().fillpass()

    def view(self):
        root.destroy()
        import displaydetails


if __name__ == '__main__':

    root = Tk()
    root.title("Random password generator")
    root.geometry('300x350+600+200')
    root.configure(background='sky blue')

    mainob = Main()
    Button(root, text='Generate Password', font=20, command=mainob.mainfunc, background='#4faaff').place(x=70, y=45)

    Button(root, text='Generate OTP', font=20, command=mainob.otp, background='#4faaff').place(x=90, y=90)

    Button(root, text='Save Passwords', font=20, command=mainob.userpass, background='#4faaff').place(x=80, y=135)

    Button(root, text='View Passwords', font=20, command=mainob.view, background='#4faaff').place(x=80, y=185)

    root.mainloop()
