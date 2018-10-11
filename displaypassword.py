from tkinter import *
from tkinter import messagebox
from random import *
import main
import string
import sendemail
import pyperclip


class Display:

    def __init__(self, var1, var2, var3, var4, limit, number):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.limit = limit
        self.number = number
        self.passw = ''

    def sendmail(self):
        sendemail.SendEmail(self.passw).maildetails()

    def generatepassword(self):
        characters = ''
        if self.var1 == 1:
            characters = characters + string.ascii_lowercase
        if self.var2 == 1:
            characters = characters + string.ascii_uppercase
        if self.var3 == 1:
            characters = characters + string.digits
        if self.var4 == 1:
            characters = characters + '!@#$%^&*()_'

        l = list(characters)
        shuffle(l)
        for i in range(0, int(self.limit)):
            self.passw = self.passw + choice(l)
        self.passw = self.passw + '\n'

    def display(self):
        if self.var1 == 0 and self.var2 == 0 and self.var3 == 0 and self.var4 == 0:
            destroying = Tk()
            destroying.withdraw()
            messagebox.showwarning("Warning", "Choose any field")
            main.Main().mainfunc()
        else:
            if self.limit == '' or 1 > self.number > 9:
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning("Warning", "Length cannot be empty")
                main.Main().mainfunc()

            elif not str(self.limit).isdigit() and not str(self.number).isdigit():
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning("Warning", "Length is not a number")
                main.Main().mainfunc()

            elif int(self.limit) > 10:
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning("Warning", "Limit exceeded")
                main.Main().mainfunc()

            else:
                passdis = Tk()
                passdis.geometry('500x500+200+100')
                passdis.title("Random Password Generator")
                passdis.configure(background='sky blue')

                def regenerat():
                    passdis.destroy()
                    main.Main().mainfunc()

                def sndmail():
                    passdis.destroy()
                    self.sendmail()

                def copy():
                    pyperclip.copy(self.passw)
                    destroying = Tk()
                    destroying.withdraw()
                    messagebox.showwarning("Warning", "Password copied!")

                for i in range(self.number):
                    self.generatepassword()

                Label(passdis, text= self.passw, font=('TkFixedFont', 20, 'bold')).pack()
                Button(passdis, text="Send as email", background='#4faaff', command=sndmail).pack()

                Button(passdis, text="Regenerate", background='#4faaff', command=regenerat).pack()

                Button(passdis, text="Copy to clipboard", background='#4faaff', command=copy).pack()
                passdis.mainloop()