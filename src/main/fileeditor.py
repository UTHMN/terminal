from tkinter import *
from tkinter import filedialog


class FileEditor:
    def __init__(self) -> None:
        self.gui = Tk()  # For tkinter object.
        self.gui.title("Text editor")
        self.gui.geometry("600x500")  # 600 is length and 500 is breadth of the text editor.
        self.text = Text(self.gui)
        self.text.pack()  # To display the text in the centre.
        self.mymenu = Menu()
        self.list1 = Menu()
        self.list1.add_command(label='New file', command=self.new_file)  # To create menus.
        self.list1.add_command(label='Open file', command=self.open_file)
        self.list1.add_command(label='Save', command=self.save_file)
        self.list1.add_command(label='Save as', command=self.save_as)
        self.list1.add_command(label='Exit', command=self.gui.quit)
        self.mymenu.add_cascade(label='File', menu=self.list1)  # To create a file option.
        self.gui.config(menu=self.mymenu)
        self.gui.mainloop()  # To display the window in the screen.This line is compulsory.

    def new_file(self):
        self.text.delete(0.0, END)  # Deletes all the contents of the text editor.

    def open_file(self):
        self.file1 = filedialog.askopenfile(mode='r')  # To open open_file filedialog.
        self.data = self.file1.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, self.data)  # Inserts data variable in text editor.

    def save_file(self):
        self.filename = "Untitled.txt"
        self.data = self.text.get(0.0, END)
        self.file1 = open(self.filename, "w")
        self.file1.write(self.data)

    def save_as(self):
        file1 = filedialog.asksaveasfile(mode='w')  # To open save_as filedialog.
        data = self.text.get(0.0, END)
        file1.write(data)
