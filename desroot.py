from tkinter import *
import displaypassword


class Option:

    def generate(self):
        displaypassword.Display(self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.limit.get(), self.number.get()).display()

    def labels(self):
        passgen = Tk()
        passgen.title("Random password generator")
        passgen.geometry('400x450+500+100')
        passgen.configure(background='sky blue')

        def des():
            passgen.destroy()
            self.generate()

        Label(passgen, text="Choose your options:", font=('TkFixedFont', 20, 'bold')).place(x=70, y=0)

        self.var1 = IntVar(0)
        Checkbutton(passgen, text='a,b,c,...', variable= self.var1, font="TkFixedFont 15").place(x=110, y=50)

        self.var2 = IntVar(0)
        Checkbutton(passgen, text='A,B,C,...', variable= self.var2, font="TkFixedFont 15").place(x=110, y=90)

        self.var3 = IntVar(0)
        Checkbutton(passgen, text='1,2,3,...', variable= self.var3, font="TkFixedFont 15").place(x=110, y=130)

        self.var4 = IntVar(0)
        Checkbutton(passgen, text='!@#$%^&*()', variable= self.var4, font="TkFixedFont 15").place(x=110, y=170)

        Label(passgen, text="Enter the number of characters:", font=('TkFixedFont', 15, 'bold')).place(x=40, y=220)

        self.limit = StringVar()
        Entry(passgen, textvariable= self.limit, bd=4, fg='grey').place(x=110, y=250)

        self.number = IntVar()
        Label(passgen, text="Number of Passwords:", font=('TkFixedFont', 15, 'bold')).place(x=60, y=290)
        Entry(passgen, textvariable=self.number, bd=4, fg='grey').place(x=110, y=320)

        Button(passgen, text="Generate", background='#4faaff', command=des).place(x=150, y=370)

        passgen.mainloop()