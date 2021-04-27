import csv, json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.title('CSV to JSON File Dialog')
root.resizable(False, False)
root.geometry('300x150')

def convert(file):
    with open(file, encoding='utf-8') as csvfile, open('csv_converted.json', 'w', encoding='utf-8') as jsonfile:
        json_data = []

        csv_reader = csv.DictReader(csvfile, delimiter=';')

        for line in csv_reader:
            json_data.append(line)
        
        json.dump(json_data, jsonfile, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

def select_file():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/Users/Carl_/Desktop/python-elective/ses11_context-managers/',
        filetypes = filetypes
    )

    showinfo(
        title = 'Converting Selected File',
        message=filename,
        command=convert(filename)
    )
    return filename

open_button = ttk.Button(
    root,
    text = 'Open a File',
    command = select_file
)

open_button.pack(expand=True)

root.mainloop()





