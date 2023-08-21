"""
Exercise "GUI step 2":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2020.png

Reuse your code from "GUI step 1".

The GUI structure should be this:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import tkinter as tk

def empty_entry():
    print("All entry boxes cleared")
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)

padx = 10
pady = 5

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")


frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


frame_2 = tk.Frame(frame_1)
frame_2.grid(row=0, column=1, padx=padx, pady=pady)


frame_3 = tk.Frame(frame_1)
frame_3.grid(row=1, column=1, padx=padx, pady=pady)


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


if __name__ == "__main__":
    main_window.mainloop()