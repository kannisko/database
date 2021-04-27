import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(True,True)
root.title('baza')

paidVar = tk.IntVar()
sentVar = tk.IntVar()


def my_action(var, indx, mode):
    print(paidVar.get(),sentVar.get())

def groupBox(var,label):
    box = ttk.LabelFrame(
        root,
        text=label)
    ttk.Radiobutton(box,
                    text="Tak",
                    variable=var,
                    value=1).grid(row=0, column=0)

    ttk.Radiobutton(box,
                    text="Nie",
                    variable=var,
                    value=2).grid(row=1, column=0)
    ttk.Radiobutton(box,
                    text="Wszystkie",
                    variable=var,
                    value=0).grid(row=2, column=0)
    return box



paidVar.trace_add('write', my_action)
sentVar.trace_add('write', my_action)

groupBox(paidVar,'zapłacono').grid(column=0, row=0, padx=10, pady=10)
groupBox(sentVar,'wysłano').grid(column=1, row=0, padx=10, pady=10)

treeView = ttk.Treeview(root, columns=(1, 2, 3), show='headings', height=8)
treeView.grid(row=1,column=0,columnspan=7, padx=10, pady=10,sticky="nsew")
treeView.heading(1, text='name')
treeView.heading(2, text="eid")
treeView.heading(3, text="Salary")

sb = ttk.Scrollbar(root, orient=tk.VERTICAL).grid(row=1,column=8,sticky="nse")
# treeView.config(yscrollcommand=sb.set)
# sb.config(command=treeView.yview)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

root.mainloop()

# def update_item():
#     selected = tv.focus()
#     temp = tv.item(selected, 'values')
#     sal_up = float(temp[2]) + float(temp[2]) * 0.05
#     tv.item(selected, values=(temp[0], temp[1], sal_up))
#
# tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
# tv.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
# tv.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
# tv.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))
# tv.insert(parent='', index=4, iid=4, values=("vineet", "e11", 1000000.00))
# tv.insert(parent='', index=5, iid=5, values=("anil", "e12", 120000.00))
# tv.insert(parent='', index=6, iid=6, values=("ankit", "e13", 41000.00))
# tv.insert(parent='', index=7, iid=7, values=("Shanti", "e14", 22000.00))
# tv.insert(parent='', index=8, iid=8, values=("vineet", "e11", 1000000.00))
# tv.insert(parent='', index=9, iid=9, values=("anil", "e12", 120000.00))
# tv.insert(parent='', index=10, iid=10, values=("ankit", "e13", 41000.00))
# tv.insert(parent='', index=11, iid=11, values=("Shanti", "e14", 22000.00))
#
# # Button(
# #     ws,
# #     text='Increment Salary',
# #     command=update_item,
# #     padx=20,
# #     pady=10,
# #     bg='#081947',
# #     fg='#fff',
# #     font=('Times BOLD', 12)
# #     ).pack(pady=10)




