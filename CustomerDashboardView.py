import tkinter as tk
from tkinter import Frame, Label, Listbox, Scrollbar, END, CENTER, BOTH
from Utils import Utils

class CustomerDashboardView:
    def __init__(self, root, customer, animals):
        self.root = root
        self.customer = customer
        self.animals = animals

        root.title("Customer Dashboard")
        root.geometry("550x600")

        self.main_container = Frame(root, bg=Utils.light_gray)
        self.main_container.pack(fill=BOTH, expand=True)

        self.main_container.grid_rowconfigure(0, weight=3)
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_rowconfigure(2, weight=6)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.create_logo()
        self.create_welcome()
        self.create_animals_list()

    def create_logo(self):
        frame = Frame(self.main_container, bg=Utils.light_gray)
        frame.grid(row=0, column=0, sticky="nsew")
        logo = Utils.image(frame, "image/cat_banner.jpg") 
        logo.pack()

    def create_welcome(self):
        frame = Frame(self.main_container, bg=Utils.light_gray)
        frame.grid(row=1, column=0, sticky="nsew")
        Label(
            frame,
            text=f"Welcome {self.customer.get_first_name()}",
            font=("Helvetica", 14, "bold"),
            fg=Utils.purple,
            bg=Utils.light_gray
        ).pack()

    def create_animals_list(self):
        frame = Frame(self.main_container, bg="white", bd=1, relief="solid")
        frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        list_container = Frame(frame, bg="white")
        list_container.grid(row=0, column=0, sticky="nsew")
        list_container.grid_rowconfigure(0, weight=1)
        list_container.grid_columnconfigure(0, weight=1)

        scrollbar = Scrollbar(list_container)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.animals_list = Listbox(
            list_container,
            font=("Arial", 12),
            bg="white",
            fg="#333333",
            highlightthickness=0,
            bd=0,
            yscrollcommand=scrollbar.set,
            justify=CENTER,
            selectbackground=Utils.purple,
            selectforeground="white",
            exportselection=False
        )
        self.animals_list.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.animals_list.yview)

        for animal in self.animals.get_animals():
            if not animal.is_already_adopted():
                self.animals_list.insert(END, f"{animal.name} (Age: {animal.age})")
