import tkinter as tk
from tkinter import ttk

#Functions
def Submit():
    print("Button was pressed")

#create window
window = tk.Tk()
window.title('Window & Widgets')
window.geometry('800x500')

#ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#tk text
text_box = tk.Text(master = window)
text_box.pack()

#ttk entry
entry_field = ttk.Entry(master = window)
entry_field.pack()

#ttk button
#submit_button = ttk.Button(master = window, text = 'Submit', command = Submit)
submit_button = ttk.Button(master = window, text = 'Submit', command = lambda: print("test")) #lambda function
submit_button.pack()

window.mainloop()