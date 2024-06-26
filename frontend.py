#!/usr/bin/env python
from tkinter import ttk
from tkinter import *
from backend import Backend

global backend
backend = Backend(False)
global window
window = Tk()
global addinputboxarr
addinputboxarr = {}
global searchbox
global filterselect
global deletebox
global filtered
filtered = False

def create_window():
    window.title("Books Manager")
    window.geometry('1050x900')

def draw_book_list(datframe):
    separator = ttk.Separator(window, orient='horizontal')
    separator.grid(row=7, column=0, pady=40, sticky="ew", columnspan=10)
    Label(window, padx= 20, text="Book List: ").grid(row=8, column=0)
    Label(window, padx= 10, pady= 15, text="ID").grid(row=8, column=1)
    colcount = 2
    for column in datframe.columns.tolist():
        Label(window, padx= 10, pady= 15, text=column).grid(row=8, column=colcount)
        colcount += 1
        rowcount = 9
        for index, row in datframe.iterrows():
            humanindex = index+1
            Label(window, padx= 10, pady= 15, text=humanindex).grid(row=rowcount, column=1)
            Label(window, padx= 10, pady= 15, text=row[column]).grid(row=rowcount, column=colcount-1)
            rowcount += 1


def reset():
    global filtered
    filtered = False
    for widgets in window.winfo_children():
        widgets.destroy()
    draw_filter_section()
    draw_sort_section()
    draw_book_input()
    draw_delete()
    draw_book_list(backend.get_dataframe())

def delete():
    global deletebox
    global filtered
    input = int(deletebox.get())
    if not False:
        backend.remove_book(input-1)
        backend.write_dataframe_to_disk()
        reset()


def filter_reload():
    global searchbox
    global filterselect
    global filtered
    filtered = True
    filter = filterselect.get()
    input = searchbox.get()
    for widgets in window.winfo_children():
      widgets.destroy()
    draw_filter_section()
    draw_sort_section()
    draw_book_input()
    draw_delete()
    draw_book_list(backend.filter_for(filter, input))

def sort_reload():
    global sortmode
    global sortselect
    global filtered
    filtered = True
    sortsel = sortselect.get()
    if(sortmode.get() == 0):
        sortmd = 'asc'
    elif(sortmode.get() == 1):
        sortmd = 'desc'
    else:
        sortmd = 'asc'
    for widgets in window.winfo_children():
      widgets.destroy()
    draw_filter_section()
    draw_sort_section()
    draw_book_input()
    draw_delete()
    draw_book_list(backend.sort_by(sortsel, sortmd))

def add_book():
    atributes = []
    for key in addinputboxarr:
        atributes.append(addinputboxarr[key].get())
    if not all('' == s or s.isspace() for s in atributes):
        backend.add_book(atributes)
    backend.write_dataframe_to_disk()
    draw_book_list(backend.get_dataframe())

def validate_integer_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

def draw_filter_section():
    global searchbox
    global filterselect
    Label(window, pady=30, padx= 20, text="Filter for: ").grid(row=0, column=0)
    searchbox = Entry(window)
    searchbox.grid(row=0, column=1)
    Label(window, text=" in:   ").grid(row=0, column=2)
    filterselect = ttk.Combobox(
        state="readonly",
        values=backend.get_columns()
    )
    filterselect.grid(row=0, column=3)
    filterbtn = Button(window, text = "Go!" , command=filter_reload)
    filterbtn.grid(row=0, column=5)
    resetfilterbtn = Button(window, text = "Reset" , command=reset)
    resetfilterbtn.grid(row=0, column=6)
    blank1 = Label(window, text="")
    blank1.grid(row=1, column=0)

def draw_sort_section():
    global sortmode
    global sortselect
    sortmode = IntVar()
    sortmode.set(0)
    Label(window, text="Sort by:   ").grid(row=2, column=0)
    sortselect = ttk.Combobox(
        state="readonly",
        values=backend.get_columns()
    )
    sortselect.grid(row=2, column=1)
    Radiobutton(window,text="Ascending", padx = 20, variable=sortmode, value=0).grid(row=2, column=3)
    Radiobutton(window,text="Descending", padx = 20, variable=sortmode, value=1).grid(row=2, column=4)
    sortbtn = Button(window, text = "Go!" , command=sort_reload)
    sortbtn.grid(row=2, column=5)
    resetsortbtn = Button(window, text = "Reset" , command=reset)
    resetsortbtn.grid(row=2, column=6)
    blank2 = Label(window, text="")
    blank2.grid(row=3, column=0)

def draw_book_input():
    global addinputboxarr
    Label(window, padx=20, pady=30, text="Add Book:").grid(row=4, column=0)
    count = 1
    for column in backend.get_columns():
        Label(window, padx=10, text=column).grid(row=4, column=count)
        validate_func = window.register(validate_integer_input) if column == "Pages" else None
        addinputboxarr[column] = Entry(window, validate="key", validatecommand=(validate_func, '%P')) if validate_func else Entry(window)
        addinputboxarr[column].grid(row=5, column=count)
        count += 1
    blank3 = Label(window, padx=50, text="")
    blank3.grid(row=4, column=count)
    addbtn = Button(window, text="Add", command=add_book)
    addbtn.grid(row=5, column=count)

def draw_delete():
    global deletebox
    deletebtn = Button(window, text = "Remove Book" , command=delete)
    deletebtn.grid(row=6, column=0, padx = 20, pady = 20)
    Label(window, padx=20, pady=30, text="by ID:").grid(row=6, column=1)
    deletebox = Entry(window)
    deletebox.grid(row=6, column=2)


def main():
    create_window()
    draw_filter_section()
    draw_sort_section()
    draw_book_input()
    draw_delete()
    draw_book_list(backend.get_dataframe())
    window.mainloop()

main()
