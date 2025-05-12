from tkinter import Tk, Frame, Label, Listbox, X, BOTH, END, RIGHT, BOTTOM
from Utils import Utils
from model.Customer import Customer
from model.Manager import Manager

class UserListView:
    def __init__(self, root, users_db):
        self.root = root
        self.users_db = users_db  
        
        root.title("User List")
        root.geometry("550x600")
        root.configure(bg=Utils.light_gray)
        
        self.create_header()
        self.create_user_list()
        self.create_close_button()
    
    def create_header(self):
        header_frame = Frame(self.root, bg=Utils.light_gray)
        header_frame.pack(fill=X, pady=20)

        try:
            logo_label = Utils.image(header_frame, "image/cat_banner.jpg")
            logo_label.pack()
        except:
            pass

        Label(
            self.root,
            text="User List",
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        Utils.separator(self.root).pack(fill=X, padx=20, pady=5)

    def create_user_list(self):
        list_frame = Frame(self.root, bg=Utils.light_gray)
        list_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        self.user_listbox = Listbox(
            list_frame,
            bg="white",
            fg="#333333",
            font=("Arial", 11),
            height=25
        )
        self.user_listbox.pack(fill=BOTH, expand=True)

        for user in self.users_db.get_users():
            if isinstance(user, Customer):
                display = f"Customer: {user.get_name()} ({user.get_email()})"
            elif isinstance(user, Manager):
                display = f"Manager: {user.get_name()} (ID: {user.get_manager_id()})"
            else:
                continue
            self.user_listbox.insert(END, display)

    def create_close_button(self):
        button_frame = Frame(self.root, bg=Utils.light_gray)
        button_frame.pack(side=BOTTOM, fill=X)

        Utils.button(button_frame, "Close", self.root.destroy).pack(
            side=RIGHT, expand=True, fill=X, ipady=10
        )
