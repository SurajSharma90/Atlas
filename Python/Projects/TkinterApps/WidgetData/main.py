import tkinter as tk
from tkinter import ttk

#Functions
def button_func():
    #print(entry.get())
    entry_text = entry.get()
    
    #update the label
    #main_label.config(text = 'some other text')
    #main_label.configure(text = 'some other text')
    main_label['text'] = entry_text
    entry['state'] = 'disabled' #disables the widget
    #print(main_label.configure()) # shows all options you can work with

def button_func_enable():
    main_label['text'] = 'Default Text'
    entry['state'] = 'enabled' #disables the widget

#Create and setup window
window = tk.Tk()
window.title("Widgets and Data")
window.geometry('800x500')

#Widgets
main_label = ttk.Label(master = window, text = 'Test label')
main_label.pack()

entry = ttk.Entry(master = window, )
entry.pack()

button = ttk.Button(master = window, text = 'Submit', command = button_func)
button.pack()

button_enable = ttk.Button(master = window, text = 'Reset', command = button_func_enable)
button_enable.pack()

#Run app
window.mainloop()