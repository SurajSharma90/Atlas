import tkinter as tk
from tkinter import ttk

#Functions
def button_func():
    print(string_var.get())
    string_var.set('Button Pressed')

#window creation
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('800x600')

#tkinter variable
string_var = tk.StringVar(value = 'start value')
#int_var = tk.IntVar()
#bool_var = tk.BooleanVar()

#widgets
label = ttk.Label(master = window, text = "default", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

button = ttk.Button(master = window, text = 'Submit', command = button_func)
button.pack()

#Run app
window.mainloop()