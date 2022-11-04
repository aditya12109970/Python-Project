from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = listb.curselection()[0]
    selected_tuple = listb.get(index)
    event.widget.delete(0,END)
    
    ent1.delete(0,END)
    ent1.insert(END ,selected_tuple[1])
    
    ent2.delete(0,END)
    ent2.insert(END ,selected_tuple[2])
    
    ent3.delete(0,END)
    ent3.insert(END ,selected_tuple[3])
    
    ent4.delete(0,END)
    ent4.insert(END ,selected_tuple[4])

    


def add_command():
    backend.insert(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    listb.insert(END, (title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))
    
    
def view_command():
    listb.delete(0,END)
    for row in backend.view():
        listb.insert(END, row)
        
        
def search_command():
    listb.delete(0,END)
    for row in backend.search(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        listb.insert(END, row)
        
        
def update_command():
    backend.update(selected_tuple[0],title_text.get(),Author_text.get(), Year_text.get(),ISBN_text.get())


def delete_command():
    backend.delete(selected_tuple[0])
    


root = Tk()
root.title("BOOK MANAGMENT")

L1 = Label(root, text='Title')
L1.grid(row=0, column=0)

L1 = Label(root, text='Author')
L1.grid(row=0, column=2)

L1 = Label(root, text='year')
L1.grid(row=1, column=0)

L1 = Label(root, text='ISBN')
L1.grid(row=1, column=2)

title_text = StringVar()
ent1 = Entry(root, textvariable = title_text)
ent1.grid(row=0,column=1)

Author_text = StringVar()
ent2 = Entry(root, textvariable = Author_text )
ent2.grid(row=0,column=3)

Year_text = StringVar()
ent3 = Entry(root, textvariable = Year_text )
ent3.grid(row=1,column=1)

ISBN_text = StringVar()
ent4 = Entry(root, textvariable = ISBN_text)
ent4.grid(row=1,column=3)

listb = Listbox(root,height=6,width=35)
listb.grid(row=2,column=0, rowspan=6,columnspan=2)

sb = Scrollbar(root)
sb.grid(row=2 ,column=2,rowspan=6)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

listb.bind("<<listboxSelect>>",get_selected_row)

b1 = Button(root,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(root,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(root,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(root,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(root,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(root,text="Close",width=12,command=root.destroy)
b6.grid(row=7,column=3)

root.mainloop()