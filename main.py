import tkinter as tk
from tkinter import filedialog

# Create a new window
root = tk.Tk()
root.title("Ume TXT Reader")


# Define a function to open a file
def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A txt File",
                                               filetypes=[("txt files", "*.txt")])
    if not root.filename:
        print("No file selected!")
        return
    with open(root.filename, "r") as file:
        text.delete("1.0", tk.END)
        text.insert("1.0", file.read())


def warp_content():
    print("Content")


# Create a menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

content_menu = tk.Menu(menubar, tearoff=0)
content_menu.add_command(label="Get Content", command=warp_content)
menubar.add_cascade(label="Content", menu=content_menu)

root.config(menu=menubar)

# Create a text widget to display the contents of the file
text = tk.Text(root)
text.pack(expand=True, fill=tk.BOTH)

# Start the main event loop
root.mainloop()
