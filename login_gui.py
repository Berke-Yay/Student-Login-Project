import imp
import tkinter as tk
from tkinter import messagebox
from student import *
s1 = student("Berke","Yay",1061,"yayber.26","LP",1234)
s2 = student("Can","Ağca",1000,"agccan.26","LP",5678)
s3 = student("Efe","Göktaş",1010,"gokefe.26","LP",9012)
s4 = student("Kaan","Bozay",1020,"bozkaa.26","LP",3456)
s5 = student("Ege","Öztürk",1030,"oztege.26","LP",7890)
students = [s1,s2,s3,s4,s5]
window = tk.Tk()
window.title("Student Portal")
window.geometry("400x400")
username_label = tk.Label(text="Enter your username: ")
username_label.pack()
username_entry = tk.Entry()
username_entry.pack()
password_label = tk.Label(text="Enter your password: ")
password_label.pack()
password_entry = tk.Entry()
password_entry.pack()
def create(chosen):
    win = tk.Toplevel(window)
    label_fullname = tk.Label(win, text=chosen.name+" "+chosen.surname)
    label_fullname.pack()
    label_id = tk.Label(win, text="Student No: "+str(chosen.id))
    label_id.pack()
    label_email = tk.Label(win, text="Email: "+chosen.email+ "@robcol.k12.tr")
    label_email.pack()
    chosen.level = chosen.level.replace("LP", "Lise Prep")
    chosen.level = chosen.level.replace("L9", "Lise 9")
    chosen.level = chosen.level.replace("L10", "Lise 10")
    chosen.level = chosen.level.replace("L11", "Lise 11")
    chosen.level = chosen.level.replace("L12", "Lise 12")
    label_level = tk.Label(win, text="Level: "+chosen.level)
    label_level.pack()
def getData():
  entered_username = username_entry.get()
  entered_password = password_entry.get()
  username_entry.delete(0,tk.END)
  password_entry.delete(0,tk.END)
  if entered_username == (s1.surname[0:3] + s1.name[0:3]).lower() and entered_password == str(s1.password):
    create(s1)
  elif entered_username == (s2.surname[0:3] + s2.name[0:3]).lower() and entered_password == str(s2.password):
    create(s2)
  elif entered_username == (s3.surname[0:3] + s3.name[0:3]).lower() and entered_password == str(s3.password):
    create(s3)
  elif entered_username == (s4.surname[0:3] + s4.name[0:3]).lower() and entered_password == str(s4.password):
    create(s4)
  elif entered_username == (s5.surname[0:3] + s5.name[0:3]).lower() and entered_password == str(s5.password):
    create(s5)
  else:
   messagebox.showwarning("Invalid Information", "You have entered either username or password incorrectly.")

login_button = tk.Button(text = "Login", command = getData)
login_button.pack()
tk.mainloop()