import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import S2_data as S2d
import S2_sql as S2sql
import S2_func as S2f

# region global constants
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"  # color of even row in treeview


# endregion global constants

# region hold functions
def read_hold_entries():  # Read content of entry boxes
    return entry_hold_id.get(), entry_hold_erfaring.get(), entry_hold_størrelse.get(),


def clear_hold_entries():  # Clear entry boxes
    entry_hold_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_hold_erfaring.delete(0, tk.END)
    entry_hold_størrelse.delete(0, tk.END)


def write_hold_entries(values):  # Fill entry boxes
    entry_hold_id.insert(0, values[0])
    entry_hold_erfaring.insert(0, values[1])
    entry_hold_størrelse.insert(0, values[2])


def edit_hold(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory, but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_hold_entries()  # Clear entry boxes
    write_hold_entries(values)  # Fill entry boxes


def create_hold(tree, record):  # add new tuple to database
    hold = S2d.Hold.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.create_record(hold)  # Update database
    clear_hold_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Hold)  # Refresh treeview table


def update_hold(tree, record):  # update tuple in database
    hold = S2d.Hold.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.update_hold(hold)  # Update database
    clear_hold_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Hold)  # Refresh treeview table


def delete_hold(tree, record):  # delete tuple in database
    hold = S2d.Hold.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.delete_soft_hold(hold)  # Update database
    clear_hold_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Hold)  # Refresh treeview table
# endregion hold functions

# region bane functions
def read_bane_entries():  # Read content of entry boxes
    return entry_bane_id.get(), entry_bane_kapacitet.get(), entry_bane_sværhedsgrad.get(),


def clear_bane_entries():  # Clear entry boxes
    entry_bane_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_bane_kapacitet.delete(0, tk.END)
    entry_bane_sværhedsgrad.delete(0, tk.END)


def write_bane_entries(values):  # Fill entry boxes
    entry_bane_id.insert(0, values[0])
    entry_bane_kapacitet.insert(0, values[1])
    entry_bane_sværhedsgrad.insert(0, values[2])


def edit_bane(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory, but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_bane_entries()  # Clear entry boxes
    write_bane_entries(values)  # Fill entry boxes


def create_bane(tree, record):  # add new tuple to database
    bane = S2d.Bane.convert_from_tuple(record)  # Convert tuple
    S2sql.create_record(bane)  # Update database
    clear_bane_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Bane)  # Refresh treeview table


def update_bane(tree, record):  # update tuple in database
    bane = S2d.Bane.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.update_bane(bane)  # Update database
    clear_bane_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Bane)  # Refresh treeview table


def delete_bane(tree, record):  # delete tuple in database
    bane = S2d.Bane.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.delete_soft_bane(bane)  # Update database
    clear_bane_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Bane)  # Refresh treeview table
# endregion hold functions

# region booking functions
def read_booking_entries():  # Read content of entry boxes
    return entry_booking_id.get(), entry_booking_date.get(), entry_booking_hold_id.get(), entry_booking_bane_id.get(),


def clear_booking_entries():  # Clear entry boxes
    entry_booking_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_booking_date.delete(0, tk.END)
    entry_booking_hold_id.delete(0, tk.END)
    entry_booking_bane_id.delete(0, tk.END)


def write_booking_entries(values):  # Fill entry boxes
    entry_booking_id.insert(0, values[0])
    entry_booking_date.insert(0, values[1])
    entry_booking_hold_id.insert(0, values[2])
    entry_booking_bane_id.insert(0, values[3])


def edit_booking(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory, but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_booking_entries()  # Clear entry boxes
    write_booking_entries(values)  # Fill entry boxes


def create_booking(tree, record):  # add new tuple to database
    booking = S2d.Booking.convert_from_tuple(record)  # Convert tuple
    plads_ok = S2f.plads(S2sql.get_record(S2d.Bane, booking.bane_id), S2sql.get_record(S2d.Hold, booking.hold_id))
    skill_ok = S2f.skill(S2sql.get_record(S2d.Bane, booking.bane_id), S2sql.get_record(S2d.Hold, booking.hold_id))
    max_one = S2f.max_one(S2sql.get_record(S2d.Bane, booking.bane_id), booking.date)
    if max_one:
        if plads_ok:
            if skill_ok:
                S2sql.create_record(booking)  # Update database
                clear_booking_entries()  # Clear entry boxes
                refresh_treeview(tree, S2d.Booking)  # Refresh treeview table
            else:
                messagebox.showwarning("", "Banen er for svær for dette hold!")
        else:
            messagebox.showwarning("", "Holdet er for stort til denne bane!")
    else:
        messagebox.showwarning("", "Banen er allerede booked den dag!")


def update_booking(tree, record):  # add new tuple to database
    booking = S2d.Booking.convert_from_tuple(record)  # Convert tuple to Booking
    plads_ok = S2f.plads(S2sql.get_record(S2d.Bane, booking.bane_id), S2sql.get_record(S2d.Hold, booking.hold_id))
    skill_ok = S2f.skill(S2sql.get_record(S2d.Bane, booking.bane_id), S2sql.get_record(S2d.Hold, booking.hold_id))
    max_one = S2f.max_one(S2sql.get_record(S2d.Bane, booking.bane_id), booking.date)
    if max_one:
        if plads_ok:
            if skill_ok:
                S2sql.update_booking(booking)  # Update database
                clear_booking_entries()  # Clear entry boxes
                refresh_treeview(tree, S2d.Booking)  # Refresh treeview table
            else:
                messagebox.showwarning("", "Banen er for svær for dette hold!")
        else:
            messagebox.showwarning("", "Holdet er for stort til denne bane!")
    else:
        messagebox.showwarning("", "Banen er allerede booked den dag!")


def delete_booking(tree, record):  # delete tuple in database
    booking = S2d.Booking.convert_from_tuple(record)  # Convert tuple to Hold
    S2sql.delete_hard_booking(booking)  # Update database
    clear_booking_entries()  # Clear entry boxes
    refresh_treeview(tree, S2d.Booking)  # Refresh treeview table


# endregion booking functions

# region common functions
def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = S2sql.select_all(class_)  # Read all from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())


def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)  # Fill treeview from database


# endregion common functions

# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('AspIT S2: BoulderParadis')  # Text shown in the top window bar
main_window.geometry("1200x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme

# Configure treeview colors and formatting. A treeview is an object that can contain a data table.
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview
# endregion common widgets

# region hold widgets
# Define Labelframe which contains all hold related GUI objects (data table, labels, buttons, ...)
frame_hold = tk.LabelFrame(main_window, text="Hold")
frame_hold.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_hold = tk.Frame(frame_hold)
tree_frame_hold.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_hold = tk.Scrollbar(tree_frame_hold)
tree_scroll_hold.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_hold = ttk.Treeview(tree_frame_hold, yscrollcommand=tree_scroll_hold.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_hold.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_hold.config(command=tree_hold.yview)

# Define the data table's formatting and content
tree_hold['columns'] = ("id", "erfaring", "størrelse")  # Define columns
tree_hold.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_hold.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_hold.column("erfaring", anchor=tk.E, width=80)
tree_hold.column("størrelse", anchor=tk.W, width=200)
tree_hold.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_hold.heading("id", text="Id", anchor=tk.CENTER)
tree_hold.heading("erfaring", text="Erfaring", anchor=tk.CENTER)
tree_hold.heading("størrelse", text="Størrelse", anchor=tk.CENTER)
tree_hold.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_hold.tag_configure('evenrow', background=evenrow)
tree_hold.bind("<ButtonRelease-1>", lambda event: edit_hold(event, tree_hold))  # Define function to be called, when an item is selected.

# Define Frame which contains labels, entries and buttons
controls_frame_hold = tk.Frame(frame_hold)
controls_frame_hold.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_hold = tk.Frame(controls_frame_hold)  # Add tuple entry boxes
edit_frame_hold.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for hold id
label_hold_id = tk.Label(edit_frame_hold, text="Id")
label_hold_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_hold_id = tk.Entry(edit_frame_hold, width=4, justify="right")
entry_hold_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for hold erfaring
label_hold_erfaring = tk.Label(edit_frame_hold, text="Erfaring")
label_hold_erfaring.grid(row=0, column=1, padx=padx, pady=pady)
entry_hold_erfaring = tk.Entry(edit_frame_hold, width=8, justify="right")
entry_hold_erfaring.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for hold størrelse
label_hold_størrelse = tk.Label(edit_frame_hold, text="Størrelse")
label_hold_størrelse.grid(row=0, column=2, padx=padx, pady=pady)
entry_hold_størrelse = tk.Entry(edit_frame_hold, width=12, justify="right")
entry_hold_størrelse.grid(row=1, column=2, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_hold = tk.Frame(controls_frame_hold)
button_frame_hold.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_hold = tk.Button(button_frame_hold, text="Create", command=lambda: create_hold(tree_hold, read_hold_entries()))
button_create_hold.grid(row=0, column=1, padx=padx, pady=pady)
button_update_hold = tk.Button(button_frame_hold, text="Update", command=lambda: update_hold(tree_hold, read_hold_entries()))
button_update_hold.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_hold = tk.Button(button_frame_hold, text="Delete", command=lambda: delete_hold(tree_hold, read_hold_entries()))
button_delete_hold.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_hold, text="Clear Entry Boxes", command=clear_hold_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion hold widgets

# region bane widgets
# Define Labelframe which contains all bane related GUI objects (data table, labels, buttons, ...)
frame_bane = tk.LabelFrame(main_window, text="Bane")
frame_bane.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_bane = tk.Frame(frame_bane)
tree_frame_bane.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_bane = tk.Scrollbar(tree_frame_bane)
tree_scroll_bane.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_bane = ttk.Treeview(tree_frame_bane, yscrollcommand=tree_scroll_bane.set, selectmode="browse")
tree_bane.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_bane.config(command=tree_bane.yview)

# Define the data table's formatting and content
tree_bane['columns'] = ("id", "kapacitet", "sværhedsgrad")  # Define columns
tree_bane.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_bane.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_bane.column("kapacitet", anchor=tk.E, width=80)
tree_bane.column("sværhedsgrad", anchor=tk.W, width=200)
tree_bane.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_bane.heading("id", text="Id", anchor=tk.CENTER)
tree_bane.heading("kapacitet", text="Kapacitet", anchor=tk.CENTER)
tree_bane.heading("sværhedsgrad", text="Sværhedsgrad", anchor=tk.CENTER)
tree_bane.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_bane.tag_configure('evenrow', background=evenrow)
tree_bane.bind("<ButtonRelease-1>", lambda event: edit_bane(event, tree_bane))  # Define function to be called, when an item is selected.

# Define Frame which contains labels, entries and buttons
controls_frame_bane = tk.Frame(frame_bane)
controls_frame_bane.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_bane = tk.Frame(controls_frame_bane)  # Add tuple entry boxes
edit_frame_bane.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for bane id
label_bane_id = tk.Label(edit_frame_bane, text="Id")
label_bane_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_bane_id = tk.Entry(edit_frame_bane, width=4, justify="right")
entry_bane_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for bane weight
label_bane_kapacitet = tk.Label(edit_frame_bane, text="Kapacitet")
label_bane_kapacitet.grid(row=0, column=1, padx=padx, pady=pady)
entry_bane_kapacitet = tk.Entry(edit_frame_bane, width=8, justify="right")
entry_bane_kapacitet.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for bane sværhedsgrad
label_bane_sværhedsgrad = tk.Label(edit_frame_bane, text="Sværhedsgrad")
label_bane_sværhedsgrad.grid(row=0, column=2, padx=padx, pady=pady)
entry_bane_sværhedsgrad = tk.Entry(edit_frame_bane, width=8, justify="right")
entry_bane_sværhedsgrad.grid(row=1, column=2, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_bane = tk.Frame(controls_frame_bane)
button_frame_bane.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_bane = tk.Button(button_frame_bane, text="Create", command=lambda: create_bane(tree_bane, read_bane_entries()))
button_create_bane.grid(row=0, column=1, padx=padx, pady=pady)
button_update_bane = tk.Button(button_frame_bane, text="Update", command=lambda: update_bane(tree_bane, read_bane_entries()))
button_update_bane.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_bane = tk.Button(button_frame_bane, text="Delete", command=lambda: delete_bane(tree_bane, read_bane_entries()))
button_delete_bane.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_bane, text="Clear Entry Boxes", command=clear_bane_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion bane widgets

# region booking widgets
# Define Labelframe which contains all booking related GUI objects (data table, labels, buttons, ...)
frame_booking = tk.LabelFrame(main_window, text="Booking")
frame_booking.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_booking = tk.Frame(frame_booking)
tree_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_booking = tk.Scrollbar(tree_frame_booking)
tree_scroll_booking.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_booking = ttk.Treeview(tree_frame_booking, yscrollcommand=tree_scroll_booking.set, selectmode="browse")
tree_booking.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_booking.config(command=tree_booking.yview)

# Define the data table's formatting and content
tree_booking['columns'] = ("id", "date", "hold_id", "bane_id")  # Define columns
tree_booking.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_booking.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_booking.column("date", anchor=tk.E, width=100)
tree_booking.column("hold_id", anchor=tk.W, width=80)
tree_booking.column("bane_id", anchor=tk.W, width=80)
tree_booking.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_booking.heading("id", text="Id", anchor=tk.CENTER)
tree_booking.heading("date", text="Date", anchor=tk.CENTER)
tree_booking.heading("hold_id", text="Hold_id", anchor=tk.CENTER)
tree_booking.heading("bane_id", text="Bane_id", anchor=tk.CENTER)
tree_booking.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_booking.tag_configure('evenrow', background=evenrow)
tree_booking.bind("<ButtonRelease-1>", lambda event: edit_booking(event, tree_booking))  # Define function to be called, when an item is selected.

# Define Frame which contains labels, entries and buttons
controls_frame_booking = tk.Frame(frame_booking)
controls_frame_booking.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_booking = tk.Frame(controls_frame_booking)  # Add tuple entry boxes
edit_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for booking id
label_booking_id = tk.Label(edit_frame_booking, text="Id")
label_booking_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_booking_id = tk.Entry(edit_frame_booking, width=4, justify="right")
entry_booking_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for booking weight
label_booking_date = tk.Label(edit_frame_booking, text="Date")
label_booking_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_booking_date = tk.Entry(edit_frame_booking, width=12, justify="right")
entry_booking_date.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for booking destination
label_booking_hold_id = tk.Label(edit_frame_booking, text="Hold ID")
label_booking_hold_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_booking_hold_id = tk.Entry(edit_frame_booking, width=4, justify="right")
entry_booking_hold_id.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for booking destination
label_booking_bane_id = tk.Label(edit_frame_booking, text="Bane ID")
label_booking_bane_id.grid(row=0, column=3, padx=padx, pady=pady)
entry_booking_bane_id = tk.Entry(edit_frame_booking, width=4, justify="right")
entry_booking_bane_id.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_booking = tk.Frame(controls_frame_booking)
button_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_booking = tk.Button(button_frame_booking, text="Create", command=lambda: create_booking(tree_booking, read_booking_entries()))
button_create_booking.grid(row=0, column=1, padx=padx, pady=pady)
button_update_booking = tk.Button(button_frame_booking, text="Update", command=lambda: update_booking(tree_booking, read_booking_entries()))
button_update_booking.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_booking = tk.Button(button_frame_booking, text="Delete", command=lambda: delete_booking(tree_booking, read_booking_entries()))
button_delete_booking.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_booking, text="Clear Entry Boxes", command=clear_booking_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion booking widgets

# region main program
# if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
#     main_window.mainloop()  # Wait for button clicks and act upon them
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_hold, S2d.Hold)  # Load data from database
    refresh_treeview(tree_bane, S2d.Bane)
    refresh_treeview(tree_booking, S2d.Booking)
    main_window.mainloop()  # Wait for button clicks and act upon them
# endregion main program