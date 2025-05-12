from tkinter import Tk, Frame, Label, Button, Canvas, Scrollbar, LEFT, RIGHT, X, Y
from Utils import Utils
from model.Animals import Animals

class ManagerDashboardView:
    def __init__(self, root):
        self.root = root
        self.animals = Animals().insert_seed_data()  # Using actual Animals class
        
        root.title("Manager Dashboard")
        root.geometry("700x600")
        root.configure(bg=Utils.light_gray)
        
        # Main container
