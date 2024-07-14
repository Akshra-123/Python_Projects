from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("400x650+400+100")
root.title("To Do App")
root.resizable(False,False)
Task_List=[]

# Image Icon
Image_Icon=PhotoImage(file="C:\\Users\\akshr\\OneDrive\\Desktop\\TaskIcon(1).png")
root.iconphoto(False,Image_Icon)

# Top Icon
Top_Icon=Image.open("C:\\Users\\akshr\\OneDrive\\Desktop\\rect.jpeg")
resizedImage=Top_Icon.resize((650,100),Image.LANCZOS)
TopImage=ImageTk.PhotoImage(resizedImage)
TopLabel=Label(root,image=TopImage,width=650,height=100)
TopLabel.place(x=0,y=0)

#Three Dots
Dock_Icon=Image.open("C:\\Users\\akshr\\OneDrive\\Desktop\\Dots.png")
resizedDock=Dock_Icon.resize((50,20),Image.LANCZOS)
DockImage=ImageTk.PhotoImage(resizedDock)
Label(root,image=DockImage,bg="#32405b").place(x=350,y=5)

# Note Image
Note_Icon=Image.open("C:\\Users\\akshr\\OneDrive\\Desktop\\TaskIcon(1).png")
ResizedNote=Note_Icon.resize((50,50),Image.LANCZOS)
NoteImage=ImageTk.PhotoImage(ResizedNote)
Label(image=NoteImage).place(x=20,y=21)

#heading
heading=Label(root,text="All Tasks",font="Comicsansms 25 bold",bg="#171B26",fg="White")
heading.place(x=130,y=25)


# Task Frame
Task=Frame(root,width=400,height=50,bg="white")
Task.place(x=0,y=180)
Task_Var=StringVar
TaskEntry=Entry(Task,width=18,font="arial 20",bd=0,textvariable=StringVar())
TaskEntry.place(x=10,y=4)
TaskEntry.focus()
tasks_label = Label(TaskEntry, text="", font="Comicsansms 15")
tasks_label.place(x=10, y=7)


def add_tasks():
    taskcontent=TaskEntry.get()
    if taskcontent:
        Task_List.append(taskcontent)
        ListBoxFrame.insert("end",taskcontent)
        TaskEntry.delete(0,END)
    with open("Python-Projects-/taskcontent.txt",'a') as file:
        file.write(taskcontent +"\n")
        file.flush()
        
        
        
AddButton=Button(Task,text="Add",font="arial 15 bold",width=8,bg="#BAE0F3",command=add_tasks)
AddButton.place(x=290,y=2)


# List Box 
ListFrame=Frame(root,width=400,height=90,bg="#171B26")
ListFrame.place(x=3,y=275)

ListBoxFrame=Listbox(ListFrame,width=400,height=17,bg="#171B26",fg="white",cursor="hand2",selectbackground="#60709D")
ListBoxFrame.pack(side=LEFT)

scrollbar=Scrollbar(ListFrame)
scrollbar.pack(side=RIGHT,fill=BOTH)

ListBoxFrame.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=ListBoxFrame.yview)

def deleteTask():
    task=str(ListBoxFrame.get(ANCHOR))
    if task in Task_List:
        Task_List.remove(task)
        with open("taskcontent.txt",'w') as taskfile:
            for taskitem in Task_List:
                taskfile.write(taskitem+"\n")
    ListBoxFrame.delete(ANCHOR)

# Delete 
delete_Icon=Image.open("C:\\Users\\akshr\\OneDrive\\Desktop\\delete.jpeg")
resized_delete=delete_Icon.resize((50,50),Image.LANCZOS)
delete_Image=ImageTk.PhotoImage(resized_delete)
Button(root,image=delete_Image,bd=0,command=deleteTask).place(x=175,y=575)




    













































root.mainloop() 
print(Task_List)