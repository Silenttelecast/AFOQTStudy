# main.py
import tkinter as tk
from gui import AFOQTGUI
from config import SUBTESTS

def main():
    root = tk.Tk()
    root.title("AFOQT Study Simulation")
    app = AFOQTGUI(root, SUBTESTS)
    root.mainloop()

if __name__ == "__main__":
    main()