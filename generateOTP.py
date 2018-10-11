import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox

o = pyotp.random_base32()


class OtpGeneration:

    def verifying(self, m):

        print("ot", m, "otp", o[:5])
        if m == o[:5]:
            destroying = Tk()
            destroying.withdraw()
            messagebox.showwarning("Warning", "OTP verified successfully")

        else:
            destroying = Tk()
            destroying.withdraw()
            messagebox.showwarning("Warning", "OTP incorrect!")
            self.verify()

    def verify(self):
        passgen = Tk()
        passgen.title("OTP verification - reg")
        passgen.geometry('250x250+500+100')
        passgen.configure(background='sky blue')

        def snd():
            self.verifying(m.get())
            passgen.destroy()


        self.otp = StringVar()
        Label(passgen, text="Enter OTP: ", font=('TkFixedFont', 10, 'bold')).pack()
        m = Entry(passgen, textvariable=self.otp, bd=5, fg='grey')
        m.pack()

        Button(passgen, text="Verify", background='#4faaff', command=snd).pack()

    def sendotp(self, toadd, body):
        msg = MIMEMultipart('alternative')

        msg['Subject'] = "Random password generator - Password reg."
        msg['From'] = "susindran@engineer.com"
        msg['To'] = toadd

        text = 'sample'
        part1 = MIMEText(text, 'plain')

        html = "<em>" + body + "<br/>Your One Time Password is: <br/><strong>" + o[:5] + "</strong></em>"
        part2 = MIMEText(html, 'html')

        username = 'susindran@engineer.com'
        password = 'Susi@1308'

        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP('smtp.mail.com', 587)

        s.login(username, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())

        s.quit()

    def maildet(self):

        passgen = Tk()
        passgen.title("Random password generator")
        passgen.geometry('250x250+500+100')
        passgen.configure(background='sky blue')

        def sending():
            try:
                self.sendotp(a.get(), b.get())
                passgen.destroy()
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning("Warning", "Mail sent!")
                self.verify()

            except:
                destroying = Tk()
                destroying.withdraw()
                messagebox.showwarning("Warning", "Mail cannot be sent!")

        self.toaddr = StringVar()
        Label(passgen, text="To: ", font=('TkFixedFont', 10, 'bold')).pack()
        a = Entry(passgen, textvariable=self.toaddr, bd=5, fg='grey')
        a.pack()

        self.msgbdy = StringVar()
        Label(passgen, text="Mail body: ", font=('TkFixedFont', 10, 'bold')).pack()
        b = Entry(passgen, textvariable=self.msgbdy, bd=5, fg='grey')
        b.pack(ipady=20)

        Button(passgen, text="Send", background='#4faaff', command=sending).pack()

        passgen.mainloop()


'''
import onetimepass as otp

my_secret = 'MFRGGZDFMZTWQ2LK'
my_token = otp.get_totp(my_secret)
print(my_token)
'''