"""
Exercise "GUI step 1":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2010.png

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import tkinter as tk

padx = 25
pady = 8

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")


frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=2, column=1, padx=padx, pady=pady)


label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=0, column=1, padx=padx, pady=pady)


entry_1 = tk.Entry(frame_1, width=3, justify="center")
entry_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1.insert(0, "")


if __name__ == "__main__":
    main_window.mainloop()