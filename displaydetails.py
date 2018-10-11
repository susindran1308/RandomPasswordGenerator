import tkinter as tk
import sqlite3

top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)

con = sqlite3.connect('users.db')

query = 'SELECT * FROM PASSWORDS'
row = con.execute(query)

con.commit()

for column in row:
    tex.insert(tk.END, "ID: " + str(column[0]) + '\n')
    tex.insert(tk.END, "Website URL: " + str(column[1]) + '\n')
    tex.insert(tk.END, "Username: " + column[2] + '\n')
    tex.insert(tk.END, "Password: " + column[3] + '\n')


tex.see(tk.END)             # Scroll if necessary

top.mainloop()
