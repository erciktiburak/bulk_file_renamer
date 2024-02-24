import tkinter as tk
from tkinter import filedialog
from bulk_file_renamer import bulk_rename_files

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def rename_files():
    folder_path = folder_entry.get()
    prefix = prefix_entry.get()
    bulk_rename_files(folder_path, prefix)
    status_label.config(text="Files renamed successfully!")

# Create the main window
root = tk.Tk()
root.title("Bulk File Renamer")

# Create and place widgets
tk.Label(root, text="Folder Path:").pack()
folder_entry = tk.Entry(root, width=50)
folder_entry.pack()
tk.Button(root, text="Browse", command=browse_folder).pack()
tk.Label(root, text="Prefix:").pack()
prefix_entry = tk.Entry(root, width=50)
prefix_entry.pack()
tk.Button(root, text="Rename Files", command=rename_files).pack()
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
