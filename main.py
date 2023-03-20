import tkinter as tk
from tkinter import filedialog

# Create a new window
root = tk.Tk()
root.title("Text File Reader")

# Define a function to open a file
def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        text.delete("1.0", tk.END)
        text.insert("1.0", file.read())

# Create a menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# Create a text widget to display the contents of the file
text = tk.Text(root)
text.pack(expand=True, fill=tk.BOTH)

# Start the main event loop
root.mainloop()
