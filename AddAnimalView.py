# AddAnimalView.py
from tkinter import Tk, Frame, Label, Entry, StringVar, Radiobutton, X, Y, E, BOTTOM, LEFT, RIGHT, messagebox, Toplevel
from Utils import Utils
from model.Animal import Cat, Dog, Rabbit
from model.Animals import Animals

class AddAnimalView:
    def __init__(self, root, animals_db):
        self.root = root
        self.animals_db = animals_db  # Animals model object
        
        # Configure window
        root.title("Add New Animal")
        root.geometry("500x500")
        root.configure(bg=Utils.light_gray)
        
        # Header
        self.create_header()
        
        # Form fields
        self.create_form()
        
        # Buttons
        self.create_buttons()
    
    def create_header(self):
        header_frame = Frame(self.root, bg=Utils.light_gray)
        header_frame.pack(fill=X, pady=20)
        
        # Logo (smaller version)
        try:
            logo_label = Utils.image(header_frame, "image/cat_banner.jpg")
            logo_label.pack()
        except:
            pass
        
        # Title
        Label(
            self.root,
            text="Add New Animal",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        Utils.separator(self.root).pack(fill=X, padx=20, pady=5)
    
    def create_form(self):
        form = Utils.frame(self.root)
        form.configure(bg=Utils.light_gray)
        form.pack(pady=20, padx=20, fill=X)
        
        # Name field
        Label(form, text="Name:", fg=Utils.purple, bg=Utils.light_gray).grid(row=0, column=0, sticky=E, pady=5)
        self.name_entry = Entry(form, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)
        
        # Age field
        Label(form, text="Age:", fg=Utils.purple, bg=Utils.light_gray).grid(row=1, column=0, sticky=E, pady=5)
        self.age_entry = Entry(form, width=30)
        self.age_entry.grid(row=1, column=1, pady=5)
        
        # Animal type selection
        Label(form, text="Animal Type:", fg=Utils.purple, bg=Utils.light_gray).grid(row=2, column=0, sticky=E, pady=5)
        
        self.animal_type = StringVar()
        self.animal_type.set("Cat")  # Default selection
        
        type_frame = Frame(form, bg=Utils.light_gray)
        type_frame.grid(row=2, column=1, sticky="w", pady=5)
        
        Radiobutton(type_frame, text="Cat", variable=self.animal_type, value="Cat", bg=Utils.light_gray).pack(side=LEFT, padx=5)
        Radiobutton(type_frame, text="Dog", variable=self.animal_type, value="Dog", bg=Utils.light_gray).pack(side=LEFT, padx=5)
        Radiobutton(type_frame, text="Rabbit", variable=self.animal_type, value="Rabbit", bg=Utils.light_gray).pack(side=LEFT, padx=5)
    
    def create_buttons(self):
        button_frame = Frame(self.root, bg=Utils.light_gray)
        button_frame.pack(side=BOTTOM, fill=X, pady=20)
        
        # Add button
        Utils.button(button_frame, "Add Animal", self.add_animal).pack(
            side=LEFT, expand=True, fill=X, ipady=10, padx=10
        )
        
        # Cancel button
        Utils.button(button_frame, "Cancel", self.root.destroy).pack(
            side=RIGHT, expand=True, fill=X, ipady=10, padx=10
        )
    
    def add_animal(self):
        # Get the form data
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        animal_type = self.animal_type.get()
        
        # Validate inputs
        if not name:
            return messagebox.showerror("Error", "Name is required")
        
        try:
            age = int(age_str)
            if age <= 0:
                raise ValueError("Age must be positive")
        except ValueError:
            return messagebox.showerror("Error", "Age must be a positive number")
        
        # Create new animal based on type
        new_animal = None
        if animal_type == "Cat":
            new_animal = Cat(name, age)
        elif animal_type == "Dog":
            new_animal = Dog(name, age)
        elif animal_type == "Rabbit":
            new_animal = Rabbit(name, age)
        
        # Add to the animals collection
        self.animals_db.add(new_animal)
        
        # Show success message and close window
        messagebox.showinfo("Success", f"{animal_type} {name} added successfully!")
        self.root.destroy()