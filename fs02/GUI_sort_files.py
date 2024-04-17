import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
from datetime import datetime
import time  # for adding delays

def sort_files(src_directory):
    # Collect all unique extensions in the directory
    unique_extensions = set()
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            if extension:  # ensure it's not an empty string
                unique_extensions.add(extension)

    # Set up directories for each type of file based on extension
    extensions_paths = {ext: [] for ext in unique_extensions}
    for ext in unique_extensions:
        folder_name = ext[1:] + '_files' if ext.startswith('.') else ext + '_files'
        extensions_paths[ext].append(folder_name)
        os.makedirs(os.path.join(src_directory, folder_name), exist_ok=True)

    # Move files into their respective directories
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in extensions_paths:
                shutil.move(os.path.join(root, file), os.path.join(src_directory, extensions_paths[ext][0], file))

def copy_files(src_directory, dest_directory):
    # Function to handle possible file name collision
    def handle_collision(target_path):
        base, extension = os.path.splitext(target_path)
        counter = 1
        while os.path.exists(target_path):
            target_path = f"{base}_{counter}{extension}"
            counter += 1
        return target_path

    for root, dirs, files in os.walk(src_directory):
        relative_path = os.path.relpath(root, src_directory)
        new_root = os.path.join(dest_directory, relative_path)
        os.makedirs(new_root, exist_ok=True)
        for file in files:
            dest_file = os.path.join(new_root, file)
            dest_file = handle_collision(dest_file)  # Check for collision
            shutil.copy(os.path.join(root, file), dest_file)

def delete_files(src_directory):
    if messagebox.askokcancel("Löschen bestätigen", "Möchten Sie die Dateien wirklich löschen?"):
        for root, dirs, files in os.walk(src_directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        messagebox.showinfo("Erfolg", "Dateien wurden erfolgreich gelöscht.")

def browse_directory(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)

# GUI Setup
root = tk.Tk()
root.title("Datei Sortierer und Überträger")
root.geometry('600x400')

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

path_label = ttk.Label(frame, text="Verzeichnispfad zum Ordnen:")
path_label.grid(row=0, column=0, sticky=tk.W)
path_entry = ttk.Entry(frame, width=50)
path_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))
browse_button = ttk.Button(frame, text="Durchsuchen...", command=lambda: browse_directory(path_entry))
browse_button.grid(row=1, column=1, sticky=tk.W)

dest_label = ttk.Label(frame, text="Netzwerkzielverzeichnis:")
dest_label.grid(row=2, column=0, sticky=tk.W)
dest_entry = ttk.Entry(frame, width=50)
dest_entry.grid(row=3, column=0, sticky=(tk.W, tk.E))
browse_dest_button = ttk.Button(frame, text="Durchsuchen...", command=lambda: browse_directory(dest_entry))
browse_dest_button.grid(row=3, column=1, sticky=tk.W)

sort_button = ttk.Button(frame, text="Dateien ordnen", command=lambda: sort_files(path_entry.get()))
sort_button.grid(row=4, column=0, sticky=tk.W)
copy_button = ttk.Button(frame, text="Zum Server kopieren", command=lambda: copy_files(path_entry.get(), dest_entry.get()))
copy_button.grid(row=5, column=0, sticky=tk.W)
delete_button = ttk.Button(frame, text="Dateien löschen", command=lambda: delete_files(path_entry.get()))
delete_button.grid(row=6, column=0, sticky=tk.W)

# Status bar setup
status = ttk.Label(frame, text="Bereit", relief=tk.SUNKEN, anchor=tk.W)
status.grid(row=7, column=0, sticky=(tk.W, tk.E))

root.mainloop()
