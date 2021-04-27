from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("baza")
ws.columnconfigure(0, weight=1)
ws.rowconfigure(1, weight=2)

paidVar = IntVar()
sentVar = IntVar()


def my_action(var, indx, mode):
    print(paidVar.get(),sentVar.get())


def groupBox(visibleParent, var, label):
    box = ttk.LabelFrame(
        visibleParent,
        text=label)
    ttk.Radiobutton(box,
                    text="Tak",
                    variable=var,
                    value=1).grid(row=0,column=0)

    ttk.Radiobutton(box,
                    text="Nie",
                    variable=var,
                    value=2).grid(row=1,column=0)
    ttk.Radiobutton(box,
                    text="Wszystkie",
                    variable=var,
                    value=0).grid(row=2,column=0)
    return box



paidVar.trace_add('write', my_action)
sentVar.trace_add('write', my_action)





topPanel = Frame(ws,borderwidth=5, relief='raised')
groupBox(topPanel,paidVar,'zapłacono').grid(row=0,column=0,sticky="wn")
groupBox(topPanel,sentVar,'wysłano').grid(row=0,column=1,sticky="wn")
topPanel.grid(row=0,column=0,sticky="we")





frame = Frame(ws,borderwidth=5, relief='raised')

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

tv = ttk.Treeview(frame, columns=(1, 2, 3), show='headings', height=8)
tv.grid(row=0,column=0,sticky="nwes")

tv.heading(1, text="name")
tv.heading(2, text="eid")
tv.heading(3, text="Salary")

sb = Scrollbar(frame, orient=VERTICAL)
sb.grid(row=0,column=1,sticky="ns")

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)
frame.grid(row=1,column=0,sticky="wens")
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

# Button(
#     ws,
#     text='Increment Salary',
#     command=update_item,
#     padx=20,
#     pady=10,
#     bg='#081947',
#     fg='#fff',
#     font=('Times BOLD', 12)
#     ).grid(row=2,column=0)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()
