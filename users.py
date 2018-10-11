import sqlite3
from tkinter import *
from tkinter import messagebox


class Passwords:

    def saving(self, url, username, password):
        conn = sqlite3.connect('users.db')
        query = "INSERT INTO PASSWORDS(WEBSITE, USERNAME, PASSWORD) VALUES('" + url + \
                "','" + username + "','" + password + "')"
        print(query)
        conn.execute(query)
        conn.commit()
        conn.close()

    def fillpass(self):
        passgen = Tk()
        passgen.title("Random password generator")
        passgen.geometry('300x150+500+100')
        passgen.configure(background='sky blue')

        def des():
            try:
                self.saving(urls.get(), usrs.get(), passs.get())
                passgen.destroy()
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning('Saved Successfully', 'Successfully saved your credentials')
            except:
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning('Save failed!', 'Cannot save the field')

        urls = StringVar()
        Label(passgen, text="Website url:", font=('TkFixedFont', 15, 'bold')).grid(row=0, column=0)
        url = Entry(passgen, textvariable=urls, bd=4, fg='grey')
        url.grid(row=0, column=1)

        usrs = StringVar()
        Label(passgen, text="Username:", font=('TkFixedFont', 15, 'bold')).grid(row=1, column=0)
        usrnme = Entry(passgen, textvariable=usrs, bd=4, fg='grey')
        usrnme.grid(row=1, column=1)

        passs = StringVar()
        Label(passgen, text="Password:", font=('TkFixedFont', 15, 'bold')).grid(row=2, column=0)
        passwo = Entry(passgen, textvariable=passs, bd=4, fg='grey').grid(row=2, column=1)

        Button(passgen, text="Save", background='#4faaff', command=des).grid(row=3,column=1)

        passgen.mainloop()
