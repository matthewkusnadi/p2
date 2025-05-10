# view/ManagerDashboardView.py
from tkinter import Label
from Utils import Utils

class ManagerDashboardView:
    def __init__(self, root, manager):
        root.title(f"Manager Dashboard – {manager.get_name()}")
        root.geometry("400x200")
        Label(root,
              text=f"Welcome, {manager.get_name()} (Manager)!",
              fg=Utils.purple,
              bg=Utils.light_gray,
              font=("Arial", 14, "bold")
        ).pack(expand=True)
