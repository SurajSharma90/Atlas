import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#functions
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly')
window.title("Miles 2 Km")
window.geometry("300x150")

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window) #frame to put widgets into
entry_int = tk.IntVar()
entry_field = ttk.Entry(master = input_frame, textvariable = entry_int)
convert_buttom = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry_field.pack(side = 'left', padx = 10)
convert_buttom.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string
)
output_label.pack(pady = 5)

#main loop to run
window.mainloop()