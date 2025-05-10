from tkinter import Label
from Utils import Utils

class CustomerDashboardView:
    def __init__(self, root, customer):
        root.title(f"Customer Dashboard – {customer.get_name()}")
        root.geometry("400x200")
        Label(root,
              text=f"Welcome, {customer.get_name()} (Customer)!",
              fg=Utils.purple,
              bg=Utils.light_gray,
              font=("Arial", 14, "bold")
        ).pack(expand=True)
