from tkinter import *
from model.Animal import Cat, Dog, Rabbit
from model.Animals import Animals
from Utils import Utils
from CustomerDashboardView import CustomerDashboardView  

class AddAnimalView:
    def __init__(self, root, animals_db):
        self.root = root
        self.animals_db = animals_db

        root.title("Add Animal")
        root.geometry("550x600")
        root.configure(bg=Utils.light_gray)

        self.create_header()
        self.create_form()
        self.create_buttons()

    def create_header(self):
        header_frame = Frame(self.root, bg=Utils.light_gray)
        header_frame.pack(fill=X, pady=20)
        try:
            logo_label = Utils.image(header_frame, "image/cat_banner.jpg")
            if logo_label:
                logo_label.pack()
        except Exception as e:
            print(f"Error loading logo: {e}")

        Label(self.root, text="Add Animal", fg=Utils.purple, bg=Utils.light_gray, font=("Arial", 14, "bold")).pack(pady=10)
        Utils.separator(self.root).pack(fill=X, padx=20, pady=5)

    def create_form(self):
        form = Utils.frame(self.root)
        form.configure(bg=Utils.light_gray)
        form.pack(pady=20, padx=20, fill=X)

        Label(form, text="Animal Type:", fg=Utils.purple, bg=Utils.light_gray).grid(row=0, column=0, sticky=E, pady=5)
        self.animal_type = StringVar()
        self.animal_type.set("Cat")
        OptionMenu(form, self.animal_type, "Cat", "Dog", "Rabbit").grid(row=0, column=1, pady=5, sticky=W)

        Label(form, text="Name:", fg=Utils.purple, bg=Utils.light_gray).grid(row=1, column=0, sticky=E, pady=5)
        self.name_entry = Entry(form, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        Label(form, text="Age:", fg=Utils.purple, bg=Utils.light_gray).grid(row=2, column=0, sticky=E, pady=5)
        self.age_entry = Entry(form, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)

    def create_buttons(self):
        button_frame = Frame(self.root, bg=Utils.light_gray)
        button_frame.pack(side=BOTTOM, fill=X, padx=20)

        add_button = Utils.button(button_frame, "Add Animal", self.add_animal)
        cancel_button = Utils.button(button_frame, "Cancel", self.root.destroy)

        add_button.pack(side=LEFT, expand=True, fill=X, ipady=10, padx=(0, 10))
        cancel_button.pack(side=RIGHT, expand=True, fill=X, ipady=10, padx=(10, 0))

        add_button.config(foreground="black")
        cancel_button.config(foreground="black")

    def add_animal(self):
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        animal_type = self.animal_type.get()

        if not name:
            return

        try:
            age = int(age_str)
            if age <= 0:
                raise ValueError
        except ValueError:
            return  

        if animal_type == "Cat":
            new_animal = Cat(name, age)
        elif animal_type == "Dog":
            new_animal = Dog(name, age)
        elif animal_type == "Rabbit":
            new_animal = Rabbit(name, age)
        else:
            return

        self.animals_db.add(new_animal)
        self.root.destroy()
        self.open_customer_dashboard()

    def open_customer_dashboard(self):
        CustomerDashboardView(Tk(), self.animals_db)
