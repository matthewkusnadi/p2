import tkinter as tk
from tkinter import Frame, Label, Button, X, Y, BOTH, LEFT, RIGHT, ttk, FLAT, TOP, BOTTOM
from Utils import Utils
from model.Animals import Animals
from model.Animal import Cat, Dog, Rabbit
from UserListView import UserListView
from AddAnimalView import AddAnimalView

class ManagerDashboardView:
    def __init__(self, root, manager, animals=None, users= None):
        self.root = root
        self.manager = manager
        
        if animals:
            self.animals = animals
        else:
            self.animals = Animals().insert_seed_data()
        
        self.users = users
        self.current_filter = "all"
        
        root.title("Manager Dashboard")
        root.geometry("550x700")
        root.configure(bg=Utils.light_gray)
        
        self.main_container = Frame(root, bg=Utils.light_gray)
        self.main_container.pack(fill="both", expand=True)
        
        self.create_logo(self.main_container)
        self.create_header(self.main_container)
        self.create_filter_buttons(self.main_container)
        self.create_animal_table(self.main_container)
        self.create_action_buttons(self.main_container)
    
    def create_logo(self, container):
        logo_frame = Frame(container, bg=Utils.light_gray)
        logo_frame.pack(fill=X)
        logo = Utils.image(logo_frame, "image/cat_banner.jpg")
        logo.pack()
    
    def create_header(self, container):
        header_frame = Frame(container, bg=Utils.light_gray)
        header_frame.pack(fill=X)
        Label(
            header_frame,
            text="Manager Dashboard",
            font=("Helvetica", 14, "bold"),
            fg=Utils.purple,
            bg=Utils.light_gray
        ).pack(pady=10)
    
    def create_filter_buttons(self, container):
        filter_frame = Frame(container, bg="#444444")
        filter_frame.pack(fill=X)

        all_btn = Utils.filter_button(filter_frame, "All", lambda: self.apply_filter("all"))
        all_btn.pack(side=LEFT, expand=True, fill=X)
        all_btn.config(font=("Arial", 12), padx=10, pady=5, fg="black")

        cat_btn = Utils.filter_button(filter_frame, "Cat", lambda: self.apply_filter("Cat"))
        cat_btn.pack(side=LEFT, expand=True, fill=X)
        cat_btn.config(font=("Arial", 12), padx=10, pady=5, fg="black")

        dog_btn = Utils.filter_button(filter_frame, "Dog", lambda: self.apply_filter("Dog"))
        dog_btn.pack(side=LEFT, expand=True, fill=X)
        dog_btn.config(font=("Arial", 12), padx=10, pady=5, fg="black")

        rabbit_btn = Utils.filter_button(filter_frame, "Rabbit", lambda: self.apply_filter("Rabbit"))
        rabbit_btn.pack(side=LEFT, expand=True, fill=X)
        rabbit_btn.config(font=("Arial", 12), padx=10, pady=5, fg="black")

    
    def create_animal_table(self, container):
        table_frame = Frame(container, bg="white")
        table_frame.pack(fill=BOTH, expand=True, padx=0, pady=0)
        
        columns = ("name", "type", "age", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        self.tree.column("name", width=175, anchor="center")
        self.tree.column("type", width=100, anchor="center")
        self.tree.column("age", width=100, anchor="center")
        self.tree.column("status", width=175, anchor="center")
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground=Utils.purple)
        
        self.tree.heading("name", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("age", text="Age")
        self.tree.heading("status", text="Adoption Status")
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        
        self.populate_table()
    
    def populate_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        filtered_animals = self.animals.get_animals_by_filter(self.current_filter)
        
        for animal in filtered_animals:
            animal_type = type(animal).__name__
            status = "Adopted" if animal.is_already_adopted() else "Available"
            self.tree.insert("", "end", values=(animal.name, animal_type, animal.age, status))
    
    def create_action_buttons(self, container):
        button_frame = Frame(container, bg=Utils.purple)
        button_frame.pack(side=BOTTOM, fill=X)

        user_list_btn = Utils.button(button_frame, "User List", self.show_user_list)
        user_list_btn.pack(side=LEFT, expand=True, fill=X)
        user_list_btn.config(font=("Arial", 13), padx=15, pady=8, fg="black", height=1)

        add_btn = Utils.button(button_frame, "Add", self.add_animal)
        add_btn.pack(side=LEFT, expand=True, fill=X)
        add_btn.config(font=("Arial", 13), padx=15, pady=8, fg="black", height=1)

        remove_btn = Utils.button(button_frame, "Remove", self.remove_animal)
        remove_btn.pack(side=LEFT, expand=True, fill=X)
        remove_btn.config(font=("Arial", 13), padx=15, pady=8, fg="black", height=1)

        close_btn = Utils.button(button_frame, "Close", self.root.destroy)
        close_btn.pack(side=LEFT, expand=True, fill=X)
        close_btn.config(font=("Arial", 13), padx=15, pady=8, fg="black", height=1)

    
    def apply_filter(self, filter_type):
        self.current_filter = filter_type
        self.populate_table()
    
    def show_user_list(self):
        if self.users:
            user_list_window = tk.Toplevel(self.root)
            UserListView(user_list_window, self.users)
        else:
            print("Users database not provided")
    
    def add_animal(self):
        add_window = tk.Toplevel(self.root)
        AddAnimalView(add_window, self.animals)
        add_window.wait_window()
        self.populate_table()
    
    def remove_animal(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        
        animal_name = self.tree.item(selected_item[0], "values")[0]
        animal = self.animals.animal(animal_name)
        if animal:
            self.animals.remove(animal)
            self.populate_table()

    def show_user_list(self):
            user_list_window = tk.Toplevel(self.root)
            UserListView(user_list_window, self.users)


