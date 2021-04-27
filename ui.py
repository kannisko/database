from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("baza")

paidVar = IntVar()
sentVar = IntVar()


def my_action(var, indx, mode):
    print(paidVar.get(),sentVar.get())

def groupBox(root,var,label):
    box = ttk.LabelFrame(
        root,
        text=label)
    ttk.Radiobutton(box,
                    text="Tak",
                    variable=var,
                    value=1).pack()

    ttk.Radiobutton(box,
                    text="Nie",
                    variable=var,
                    value=2).pack()
    ttk.Radiobutton(box,
                    text="Wszystkie",
                    variable=var,
                    value=0).pack()
    return box



paidVar.trace_add('write', my_action)
sentVar.trace_add('write', my_action)





topPanel = ttk.Frame(ws).pack(side=TOP)
groupBox(topPanel,paidVar,'zapłacono').pack(side=LEFT)
groupBox(topPanel,sentVar,'wysłano').pack(side=LEFT)



frame = Frame(ws)
frame.pack(pady=10, side=BOTTOM)

tv = ttk.Treeview(frame, columns=(1, 2, 3), show='headings', height=8)
tv.pack(side=LEFT)

tv.heading(1, text="name")
tv.heading(2, text="eid")
tv.heading(3, text="Salary")

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)

def update_item():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    sal_up = float(temp[2]) + float(temp[2]) * 0.05
    tv.item(selected, values=(temp[0], temp[1], sal_up))

tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))
tv.insert(parent='', index=4, iid=4, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=5, iid=5, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=6, iid=6, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=7, iid=7, values=("Shanti", "e14", 22000.00))
tv.insert(parent='', index=8, iid=8, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=9, iid=9, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=10, iid=10, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=11, iid=11, values=("Shanti", "e14", 22000.00))

Button(
    ws,
    text='Increment Salary',
    command=update_item,
    padx=20,
    pady=10,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    ).pack(pady=10)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()
