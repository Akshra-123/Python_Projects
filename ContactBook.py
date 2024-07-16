from tkinter import *
root=Tk()
root.title("Contact Book")
root.geometry("400x500")
data=[]


# Adding Labels and Frames
Name=StringVar()
Number=StringVar()

frame=Frame()
frame.pack(pady=10)

Label(frame,text="Name",font="Arial 12 bold").pack(side=LEFT)
Entry(frame,textvariable=Name,width=50).pack()

frame1=Frame()
frame1.pack()

Label(frame1,text="Phone No.",font="Arial 12 bold").pack(side=LEFT)
Entry(frame1,textvariable=Number,width=44).pack()

frame2=Frame()
frame2.pack(pady=10)

Label(frame2,text="Address",font="Arial 12 bold").pack(side=LEFT)
address=Text(frame2,width=35,height=10)
address.pack()

# Adding Buttons
def add():
    global data
    data.append([Name.get(),Number.get(),address.get(1.0,"end-1c")])
    update_book()
Button(root,text="add",font="Arial 12 bold",command=add).place(x=100,y=270)

def delete():
    del data[int(select.curselection()[0])]
    update_book()
Button(root,text="delete",font="Arial 12 bold",command=delete).place(x=100,y=310)

def view():
    Name.set(data[int(select.curselection()[0])][0])
    Number.set(data[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0,data[int(select.curselection()[0])][2])
Button(root,text="view",font="Arial 12 bold",command=view).place(x=100,y=350)

def reset():
    Name.set(" ")
    Number.set(" ")
    address.delete(1.0,"end")
Button(root,text="reset",font="Arial 12 bold",command=reset).place(x=100,y=390)


def update_book():
    select.delete(0,"end")
    for n,p,a in data:
        select.insert(END,n)
        
# Scroll Bar
scroll_bar=Scrollbar(root,orient=VERTICAL)
select=Listbox(root,yscrollcommand=scroll_bar.set,height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=LEFT,fill=Y)
select.place(x=200,y=260)









root.mainloop()