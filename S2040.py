"""
Exercise "GUI step 4":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2040.png

Reuse your code from "GUI step 3".

Fill the treeview with test data.
Play with the color values. Find a color combination that you like.

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes.
    clicking on a data row in the treeview copies the data of this row into the entry fields.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


import tkinter as tk
from tkinter import ttk


def empty_entry():
    print("All entry boxes cleared")
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)

def read_table(tree):  # fill tree with test data
        count = 0
        for record in test_data_list:
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
            else:  # odd
                tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
            count += 1

def edit_record(event, tree):  # Copy data from selected row into entry box. Parameter event is mandatory but we don't use it. (1)
        index_selected = tree.focus()  # Index of selected tuple
        values = tree.item(index_selected, 'values')  # Values of selected tuple
        entry_1.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
        entry_1.insert(0, values[0])  # write data into entry box
        entry_2.delete(0, tk.END)
        entry_2.insert(0, values[1])
        entry_3.delete(0, tk.END)
        entry_3.insert(0, values[2])


padx = 10
pady = 5
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ff95da"
evenrow = "#ffbde9"


test_data_list = []
test_data_list.append(("1", 1000, "Oslo"))
test_data_list.append(("2", 2000, "Chicago"))
test_data_list.append(("3", 3000, "Milano"))
test_data_list.append(("4", 4000, "Asterdam"))


main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("900x500")


frame_main = tk.LabelFrame(main_window, text="Container")
frame_main.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(frame_main)
frame_1.grid(row=0, column=1, padx=padx, pady=pady)

frame_2 = tk.Frame(frame_main)
frame_2.grid(row=1, column=1, padx=padx, pady=pady)

frame_3 = tk.Frame(frame_main)
frame_3.grid(row=2, column=1, padx=padx, pady=pady)


style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])


tree_1_scrollbar = tk.Scrollbar(frame_1)
tree_1_scrollbar.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(frame_1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

tree_1.tag_configure('oddrow', background=oddrow)  # Create tags
tree_1.tag_configure('evenrow', background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))


empty_entry_button = tk.Button(frame_3, text="clear entry boxes", command=empty_entry)
empty_entry_button.grid(row=0, column=4, padx=padx, pady=pady)

button_1 = tk.Button(frame_3, text="Create")
button_1.grid(row=0, column=1, padx=padx, pady=pady)

button_2 = tk.Button(frame_3, text="Update")
button_2.grid(row=0, column=2, padx=padx, pady=pady)

button_3 = tk.Button(frame_3, text="Delete")
button_3.grid(row=0, column=3, padx=padx, pady=pady)


label_1 = tk.Label(frame_2, text="Id")
label_1.grid(row=0, column=1, padx=padx, pady=pady)

label_2 = tk.Label(frame_2, text="Weight")
label_2.grid(row=0, column=2, padx=padx, pady=pady)

label_3 = tk.Label(frame_2, text="Destination")
label_3.grid(row=0, column=3, padx=padx, pady=pady)

label_4 = tk.Label(frame_2, text="Weather")
label_4.grid(row=0, column=4, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_2, width=4, justify="left")
entry_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1.insert(0, "fhgfhj")

entry_2 = tk.Entry(frame_2, width=6, justify="left")
entry_2.grid(row=1, column=2, padx=padx, pady=pady)
entry_2.insert(0, "jbh")

entry_3 = tk.Entry(frame_2, width=8, justify="left")
entry_3.grid(row=1, column=3, padx=padx, pady=pady)
entry_3.insert(0, "vjhjbk")

entry_4 = tk.Entry(frame_2, width=6, justify="left")
entry_4.grid(row=1, column=4, padx=padx, pady=pady)
entry_4.insert(0, "hey")

read_table(tree_1)

if __name__ == "__main__":
    main_window.mainloop()
