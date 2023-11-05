import tkinter as tk
from tkinter import ttk

#functions
def button_func():
    print('Submit')
    print(radio_var.get())

#create window
window = tk.Tk()
window.title('Buttons')
window.geometry('800x600')

#variables
button_string = tk.StringVar(value = "Default Value")
check_var = tk.BooleanVar()
radio_var = tk.StringVar()

#buttons
button = ttk.Button(window, text = 'Submit', command = button_func, textvariable = button_string)
#button = ttk.Button(window, text = 'Submit', command = lambda: print('Submit'))
button.pack()

#check button

check = ttk.Checkbutton(
    window, 
    text = 'Checkbox 1', 
    command = lambda: print(check_var.get()), 
    variable = check_var,
    onvalue = True,
    offvalue = False
    )
check.pack()

#radio buttons need different values to work properly, otherwise they will trigger eachoter
radio1 = ttk.Radiobutton(window, text = "rb1", value = 'Radio1', variable = radio_var, command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = "rb2", value = 2, variable = radio_var)
radio2.pack()

#run app
window.mainloop()