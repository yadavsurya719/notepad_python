import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import webbrowser

class EnhancedNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Notepad")

        # Text widget
        self.text_widget = tk.Text(self.root, wrap="word", undo=True)
        self.text_widget.pack(expand=True, fill="both")

        # Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_application)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.find_text)

        # Cloud menu
        self.cloud_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cloud", menu=self.cloud_menu)
        self.cloud_menu.add_command(label="Upload to Cloud", command=self.upload_to_cloud)
        self.cloud_menu.add_command(label="Download from Cloud", command=self.download_from_cloud)

        # Code menu
        self.code_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Code", menu=self.code_menu)
        self.code_menu.add_command(label="Syntax Highlighting", command=self.syntax_highlighting)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        if not hasattr(self, "current_file"):
            self.save_file_as()
        else:
            content = self.text_widget.get(1.0, tk.END)
            with open(self.current_file, "w") as file:
                file.write(content)

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
        if file_path:
            self.current_file = file_path
            self.save_file()

    def exit_application(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()

    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    def find_text(self):
        query = simpledialog.askstring("Find", "Enter text to find:")
        if query:
            start_index = self.text_widget.search(query, 1.0, tk.END)
            if start_index:
                end_index = f"{start_index}+{len(query)}c"
                self.text_widget.tag_add(tk.SEL, start_index, end_index)
                self.text_widget.mark_set(tk.INSERT, end_index)
                self.text_widget.see(tk.INSERT)

    def upload_to_cloud(self):
        messagebox.showinfo("Cloud Upload", "Uploading to cloud... (Feature not implemented)")

    def download_from_cloud(self):
        messagebox.showinfo("Cloud Download", "Downloading from cloud... (Feature not implemented)")

    def syntax_highlighting(self):
        messagebox.showinfo("Syntax Highlighting", "Syntax highlighting... (Feature not implemented)")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedNotepad(root)
    root.mainloop()
