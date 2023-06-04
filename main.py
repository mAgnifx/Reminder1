import customtkinter as ctk
import tkinter
import time
from plyer import notification
from tkinter import messagebox
root = ctk.CTk()

root.geometry("450x200")
root.title('Reminder')
ctk.set_appearance_mode("dark") 


def remind_me():
    if(noti_enty.get()=='' or noti2_enty.get()==''):
        messagebox.showerror (title='Error 404', message='Enter a reminder and a time else u cant enter a reminder')

    else:
        
        time.sleep(int (noti2_enty.get()))
        notification.notify(title='REMINDER',message=noti_enty.get(), timeout=60)













noti=ctk.CTkLabel(root,text="Reminder")
noti.place(x=13,y=20)

noti_enty=ctk.CTkEntry(root,width=200)
noti_enty.place(x=20,y=50)




noti2=ctk.CTkLabel(root,text="Timpe")
noti2.place(x=290,y=20)


noti2_enty=ctk.CTkEntry(root,width=50)
noti2_enty.place(x=310,y=50)



buton=ctk.CTkButton(root,command=remind_me,text="Remind me!!")
buton.place(x=190,y=110)






note2=ctk.CTkLabel(root,text="1minute-60 sec,2minutes-120sec,3minutes-180sec")
note2.place(x=5,y=170)


root.mainloop()
