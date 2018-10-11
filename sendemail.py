import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox


class SendEmail:

    def __init__(self, passwd):
        self.password = passwd.replace('\n', '<br/>')

    def send(self, toadd, body):
        msg = MIMEMultipart('alternative')

        msg['Subject'] = "Random password generator - Password reg."
        msg['From'] = "susindran@engineer.com"
        msg['To'] = toadd

        text = 'sample'
        part1 = MIMEText(text, 'plain')

        html = "<em>" + body + "<br/>Password is: <br/><strong>" + self.password + "</strong></em>"
        part2 = MIMEText(html, 'html')

        username = 'susindran@engineer.com'
        password = 'Susi@1308'

        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP('smtp.mail.com', 587)

        s.login(username, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())

        s.quit()

    def maildetails(self):

        passgen = Tk()
        passgen.title("Random password generator")
        passgen.geometry('250x250+500+100')
        passgen.configure(background='sky blue')

        def sending():
            # print(a.get())
            self.send(a.get(), b.get())
            passgen.destroy()
            destroying = Tk()
            destroying.withdraw()
            messagebox.showwarning("Warning", "Mail sent!")

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
