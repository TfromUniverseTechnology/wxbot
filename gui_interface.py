
import tkinter as tk
from tkinter import messagebox

class GUIInterface:
    def __init__(self, window_title="GUI Interface"):
        self.window = tk.Tk()
        self.window.title(window_title)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def close_window(self):
        self.window.destroy()

# Example usage:
# gui = GUIInterface()
# gui.show_message("Hello, World!")
# gui.close_window()
