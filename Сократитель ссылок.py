from tkinter import *
from tkinter import ttk,messagebox
import pyshorteners

def short():
    s = pyshorteners.Shortener()
    shor = bedforelink.get()
    afterLink.delete(0,END)
    afterLink.insert(0,s.tinyurl.short(shor))

root = Tk()
root.title('Сокращатель ссылок')
root.geometry('500x150')
root.resizable(False,False)

beforelinkLabel = Label(root,text='Вставтье ссылку')
beforelinkLabel.place(x=10,y=10)

bedforelink = ttk.Entry(root,width=40,font='Arial 13 bold')
bedforelink.place(x=10,y=30)

btn = ttk.Button(root,text='Сократить',command=short)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

afterLinkLabel = Label(root,text='Результат')
afterLinkLabel.place(x=10,y=80)

afterLink = ttk.Entry(root,width=40,font='Arial 13 bold')
afterLink.place(x=10,y=105)

root.mainloop()