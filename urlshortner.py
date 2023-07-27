

from tkinter import *
import pyshorteners
from PIL import ImageTk

root=Tk()
root.title("Shrinker")
root.iconbitmap(r"favicon.ico")
root.geometry("500x500")
root.configure(bg="white")
img= PhotoImage(file='bckgrnd.png', master= root)
img_label= Label(root,image=img)

#define the position of the image
img_label.place(x=0, y=0)

#function to shorten the link

def shortenlink():
    longURL=my_entry.get()

    #shorten URL
    shortURL=pyshorteners.Shortener().tinyurl.short(longURL)

    #output it to the screen
    short_link_label.insert(END,shortURL)

#creating the GUI

label_1=Label(root,text="🔗 Insert the link 🔗",font=("Times New Roman",20),bg="lightyellow")
label_1.pack(pady=30)

my_entry=Entry(root,font=("times new roman",15,"bold"),bg="white",fg="#262626")
my_entry.pack(pady=30)

my_button=Button(root,text="Get Started",font=("Times New Roman",12),command=shortenlink,bg='#00a4e4',fg='white')
my_button.pack(pady=20)

label_2=Label(root,text="Your shorten Link\n👇👇👇",font=("Times New Roman",20))
label_2.pack(pady=10)

short_link_label=Entry(root,font=("Times New Roman",20),bd=0,bg="lightblue",justify=CENTER,width=30)
short_link_label.pack(pady=30)

root.mainloop()
