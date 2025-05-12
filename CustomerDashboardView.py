import tkinter as tk
from tkinter import Frame, Label, Button, FLAT, LEFT, X, BOTH, Listbox,Scrollbar, END, RIGHT, Y
from Utils import Utils

class CustomerDashboardView:
    def __init__(self, root, customer, animals):
        self.root = root
        self.customer = customer
        self.animals = animals
        
        # Setup the window
        root.title("Customer Dashboard")
        root.geometry("550x600")
        
        # Main container
        self.main_container = Frame(root, bg=Utils.light_gray)
        self.main_container.pack(fill="both", expand=True)
        
        # Add components
        self.create_logo(self.main_container)
        self.create_welcome(self.main_container)
        self.create_animals_list(self.main_container)
        self.create_buttons(self.main_container)
    
    def create_logo(self, container):
        # Logo section
        logo_frame = Frame(container, bg=Utils.light_gray)
        logo_frame.pack()
        
        # Display the logo image
        logo = Utils.image(logo_frame, "image/cat_banner.jpg")
        logo.pack()
    
    def create_welcome(self, container):
    # Welcome message frame
        welcome_frame = Frame(container, bg=Utils.light_gray)
        welcome_frame.pack(fill=X)
    
    # Simple welcome label
        Label(
            welcome_frame,
            text=f"Welcome {self.customer.get_name()}",
            font=("Helvetica", 14, "bold"),
            fg=Utils.purple,
            bg=Utils.light_gray
        ).pack(pady=10)

    def create_animals_list(self):
        # Create a frame for the animals list
        animals_frame = Frame(self.main_container, bg="white")
        animals_frame.pack(fill=BOTH, expand=True)
        
        # Create scrollbar
        scrollbar = Scrollbar(animals_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Create listbox with scrollbar
        animals_list = Listbox(
            animals_frame,
            font=("Arial", 12),
            bg="white",
            fg="#333333",
            highlightthickness=0,
            bd=0,
            yscrollcommand=scrollbar.set
        )
        
        # Get animals from the Animals class and add to listbox
        # Your Animal class has both direct attributes and getters, we'll use direct attributes
        for animal in self.animals.get_animals():
            animals_list.insert(END, f"{animal.name} (Age: {animal.age})")
        
        # Pack the listbox
        animals_list.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=animals_list.yview)
    
    def create_buttons(self):
        # Button frame at the bottom
        button_frame = Frame(self.main_container, bg=Utils.purple)
        button_frame.pack(side="bottom", fill=X)
        
        # Add the three buttons
        Utils.button(button_frame, "My Details", self.show_details).pack(side=LEFT, expand=True, fill=X)
        Utils.button(button_frame, "Adopt", self.adopt_animal).pack(side=LEFT, expand=True, fill=X)
        Utils.button(button_frame, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)
    
    def show_details(self):
        print("My Details clicked")
    
    def adopt_animal(self):
        print("Adopt clicked")