from tkinter import *
from tkinter import messagebox
import sqlite3


class Display:

    def display(self):

        conn = sqlite3.connect('users.db')
        passw = conn.execute("SELECT * FROM PASSWORDS")
        details = ''
        for det in passw:
            details = details + 'URL:\t' + det[0] + '\nUsername:\t' + det[1] + '\nPassword:\t' + det[2] + '\n\n'

        passgen = Tk()
        passgen.title("Random password generator")
        passgen.geometry('500x500+500+100')

        e = Entry(passgen, textvariable=details, bd=4)
        e.pack(ipady=20)
        e.insert(0, details)
        passgen.mainloop()

ob = Display()
ob.display()