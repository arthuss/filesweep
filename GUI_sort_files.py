import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def move_files(src_directory):
    if not src_directory:
        messagebox.showerror("Fehler", "Bitte geben Sie einen gültigen Pfad ein.")
        return
    if not os.path.exists(src_directory):
        messagebox.showerror("Fehler", "Der angegebene Pfad existiert nicht.")
        return
    
    # Definition der Dateiendungen und der zugehörigen neuen Ordner
    extensions_paths = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.webp','.svg','.jfif','.tif'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv','.aepx','.3gp'],
        '3d_files': ['.obj', '.stl', '.fbx', '.mtl', '.usd','.glb','.gltf','.bin','.stl'],
        'blender_files': ['.blend', '.blend1'],
        'zip_files': ['.zip', '.rar', '.7z'],
        'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx','.txt','.html','.dll'],
        'audio_files': ['.mp3'],
        'executable_files': ['.exe','.msi'],
        'config_files': ['.cfg', '.ctb'],
        'design_files': ['.ai']
    }
    
    actions = []
    for key in extensions_paths:
        os.makedirs(os.path.join(src_directory, key), exist_ok=True)

    for item in os.listdir(src_directory):
        item_path = os.path.join(src_directory, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1].lower()
            for key, ext_list in extensions_paths.items():
                if ext in ext_list:
                    shutil.move(item_path, os.path.join(src_directory, key, item))
                    actions.append(f"Moved {item} to {key}/")
                    break

    if actions:
        messagebox.showinfo("Fertig", "Dateien wurden erfolgreich sortiert:\n" + "\n".join(actions))
    else:
        messagebox.showinfo("Fertig", "Keine Dateien zum Verschieben gefunden.")

def browse_directory():
    filename = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, filename)

# GUI Setup
root = tk.Tk()
root.title("Datei Sortierer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

path_label = tk.Label(frame, text="Verzeichnispfad:")
path_label.pack(fill='x', expand=True)

path_entry = tk.Entry(frame, width=50)
path_entry.pack(fill='x', expand=True)

browse_button = tk.Button(frame, text="Durchsuchen...", command=browse_directory)
browse_button.pack(fill='x', expand=True)

sort_button = tk.Button(frame, text="Sortieren", command=lambda: move_files(path_entry.get()))
sort_button.pack(fill='x', expand=True)

root.mainloop()
