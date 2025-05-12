# DetailsView.py
from tkinter import Tk, Frame, Label, Listbox, X, Y, BOTH, END, BOTTOM
from Utils import Utils
from model.Customer import Customer
from model.Manager import Manager

class DetailsView:
    def __init__(self, root, user):
        self.root = root
        self.user = user  # User model object (Customer or Manager)
        
        # Configure window
        root.title(f"User Details - {user.get_name()}")
        root.geometry("500x600")
        root.configure(bg=Utils.light_gray)
        
        # Header
        self.create_header()
        
        # User details
        self.create_details()
        
        # Close button
        Utils.button(self.root, "Close", self.root.destroy).pack(
            side=BOTTOM, fill=X, padx=20, pady=20, ipady=10
        )
    
    def create_header(self):
        header_frame = Frame(self.root, bg=Utils.light_gray)
        header_frame.pack(fill=X, pady=20)
        
        # Logo
        try:
            logo_label = Utils.image(header_frame, "image/cat_banner.jpg")
            logo_label.pack()
        except:
            pass
        
        # Title
        Label(
            self.root,
            text=f"Details for {self.user.get_name()}",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        Utils.separator(self.root).pack(fill=X, padx=20, pady=5)
    
    def create_details(self):
        details_frame = Frame(self.root, bg=Utils.light_gray)
        details_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # User type (Customer or Manager)
        user_type = "Customer" if isinstance(self.user, Customer) else "Manager"
        Label(
            details_frame,
            text=f"User Type: {user_type}",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill=X, pady=5)
        
        # User name
        Label(
            details_frame,
            text=f"Name: {self.user.get_name()}",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill=X, pady=5)
        
        # If Customer, show email and adopted animals
        if isinstance(self.user, Customer):
            # Email
            Label(
                details_frame,
                text=f"Email: {self.user.get_email()}",
                fg=Utils.purple,
                bg=Utils.light_gray,
                font=("Arial", 12),
                anchor="w"
            ).pack(fill=X, pady=5)
            
            # Adopted animals section
            Label(
                details_frame,
                text="Adopted Animals:",
                fg=Utils.purple,
                bg=Utils.light_gray,
                font=("Arial", 12, "bold"),
                anchor="w"
            ).pack(fill=X, pady=(20, 10))
            
            # List of adopted animals
            adopted_animals = self.user.get_adopted_animals().get_animals()
            
            if adopted_animals:
                animals_listbox = Listbox(
                    details_frame,
                    bg="white",
                    fg="#333333",
                    font=("Arial", 11),
                    height=len(adopted_animals) + 1
                )
                animals_listbox.pack(fill=X)
                
                for animal in adopted_animals:
                    animals_listbox.insert(END, str(animal))
            else:
                Label(
                    details_frame,
                    text="No animals adopted yet",
                    fg="#666666",
                    bg=Utils.light_gray,
                    font=("Arial", 11),
                    anchor="w"
                ).pack(fill=X, pady=5)
        
        # If Manager, show manager ID
        elif isinstance(self.user, Manager):
            Label(
                details_frame,
                text=f"Manager ID: {self.user.get_manager_id()}",
                fg=Utils.purple,
                bg=Utils.light_gray,
                font=("Arial", 12),
                anchor="w"
            ).pack(fill=X, pady=5)