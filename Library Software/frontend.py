from tkinter import *
import backend

def get_selected_rows(event):
    try:
        global selected_tuple
        index=list1.curselection()
        selected_tuple = list1.get(index)

        b1.delete(0,END)
        b1.insert(END,selected_tuple[1])
        b2.delete(0,END)
        b2.insert(END,selected_tuple[2])
        b3.delete(0,END)
        b3.insert(END,selected_tuple[3])
        b4.delete(0,END)
        b4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)

    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = isbn_text.get()

    for row in backend.search(title,author,year,isbn):
        list1.insert(END,row)

def add_command():
    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = isbn_text.get()

    backend.insert(title,author,year,isbn)
    list1.delete(0,END)
    list1.insert(END,(title,author,year,isbn))

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

window = Tk()

window.wm_title("BookStore")

e1 = Label(window, text="Title")
e1.grid(row=0,column=0)

e2 = Label(window, text="Author")
e2.grid(row=0,column=2)

e3 = Label(window, text="Year")
e3.grid(row=1,column=0)

e4 = Label(window, text="ISBN")
e4.grid(row=1,column=2)

title_text = StringVar()
b1 = Entry(window,textvariable=title_text)
b1.grid(row=0,column=1)

author_text = StringVar()
b2 = Entry(window,textvariable=author_text)
b2.grid(row=0,column=3)

year_text = StringVar()
b3 = Entry(window,textvariable=year_text)
b3.grid(row=1,column=1)

isbn_text = StringVar()
b4 = Entry(window,textvariable=isbn_text)
b4.grid(row=1,column=3)



list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_rows)


btn1 = Button(window, text="View All", width=12, command=view_command)
btn1.grid(row=2,column=3)

btn2 = Button(window, text="Search Entry", width=12, command=search_command)
btn2.grid(row=3,column=3)

btn3 = Button(window, text="Add Entry", width=12, command=add_command)
btn3.grid(row=4,column=3)

btn4 = Button(window, text="Update Selected", width=12,command=update_command)
btn4.grid(row=5,column=3)

btn5 = Button(window, text="Delete Selected", width=12, command=delete_command)
btn5.grid(row=6,column=3)

btn6 = Button(window, text="Close", width=12,command=window.destroy)
btn6.grid(row=7,column=3)

window.mainloop()
