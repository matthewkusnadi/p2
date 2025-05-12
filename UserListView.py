# UserListView.py
from tkinter import Tk, Frame, Label, Listbox, X, Y, BOTH, END, LEFT, RIGHT, BOTTOM, TOP
from Utils import Utils
from model.Users import Users
from model.Customer import Customer
from model.Manager import Manager
from DetailsView import DetailsView

class UserListView:
    def __init__(self, root, users_db):
        self.root = root
        self.users_db = users_db  # Users model object
        
        # Configure window
        root.title("User List")
        root.geometry("550x600")
        root.configure(bg=Utils.light_gray)
        
        # Header
        self.create_header()
        
        # Users list
        self.create_user_list()
        
        # Buttons
        self.create_buttons()
    
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
            text="User List",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        Utils.separator(self.root).pack(fill=X, padx=20, pady=5)
    
    def create_user_list(self):
        # Create frame for lists
        list_frame = Frame(self.root, bg=Utils.light_gray)
        list_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Customers section
        Label(
            list_frame,
            text="Customers",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        # Listbox for customers
        self.customer_listbox = Listbox(
            list_frame,
            bg="white",
            fg="#333333",
            selectbackground=Utils.purple,
            selectforeground="white",
            font=("Arial", 11),
            height=10
        )
        self.customer_listbox.pack(fill=X, pady=(0, 20))
        
        # Managers section
        Label(
            list_frame,
            text="Managers",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(0, 10))
        
        # Listbox for managers
        self.manager_listbox = Listbox(
            list_frame,
            bg="white",
            fg="#333333",
            selectbackground=Utils.purple,
            selectforeground="white",
            font=("Arial", 11),
            height=5
        )
        self.manager_listbox.pack(fill=X)
        
        # Populate lists from the model
        for user in self.users_db.get_users():
            if isinstance(user, Customer):
                self.customer_listbox.insert(END, str(user))
            elif isinstance(user, Manager):
                self.manager_listbox.insert(END, f"{user.get_name()} (ID: {user.get_manager_id()})")
    
    def create_buttons(self):
        button_frame = Frame(self.root, bg=Utils.light_gray)
        button_frame.pack(side=BOTTOM, fill=X)
        
        # View Details button
        Utils.button(button_frame, "View Details", self.view_details).pack(
            side=LEFT, expand=True, fill=X, ipady=10
        )
        
        # Close button
        Utils.button(button_frame, "Close", self.root.destroy).pack(
            side=RIGHT, expand=True, fill=X, ipady=10
        )
    
    def view_details(self):
        # Check if a customer is selected
        customer_sel = self.customer_listbox.curselection()
        manager_sel = self.manager_listbox.curselection()
        
        selected_user = None
        
        if customer_sel:
            # Get selected customer
            customer_str = self.customer_listbox.get(customer_sel[0])
            name = customer_str.split(" (")[0]
            
            # Find customer in the model
            for user in self.users_db.get_users():
                if isinstance(user, Customer) and user.get_name() == name:
                    selected_user = user
                    break
        
        elif manager_sel:
            # Get selected manager
            manager_str = self.manager_listbox.get(manager_sel[0])
            name = manager_str.split(" (ID:")[0]
            
            # Find manager in the model
            for user in self.users_db.get_users():
                if isinstance(user, Manager) and user.get_name() == name:
                    selected_user = user
                    break
        
        if selected_user:
            # Open details view for the selected user
            details_window = Tk()
            DetailsView(details_window, selected_user)