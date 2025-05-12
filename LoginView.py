from tkinter import Tk, Frame, Label, Button, Entry, X, BOTTOM, LEFT, RIGHT
from Utils import Utils
from model.Users import Users
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView
from ErrorView import ErrorView

class LoginView:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("550x550")
        root.configure(bg=Utils.light_gray)

        from model.Animals import Animals  # Import here to avoid circular imports
        self.animals = Animals().insert_seed_data()
        self.users_db = Users()
        self.users_db.insert_seed_data(self.animals)

        self.create_logo_section(root)
        self.create_login_section(root)
        self.create_button_section(root)

    def create_logo_section(self, root):
        logo_frame = Frame(root, bg=Utils.light_gray)
        logo_frame.pack()

        logo_label = Utils.image(logo_frame, "image/cat_banner.jpg")
        logo_label.pack()

        Utils.separator(root).pack(fill=X, pady=1)

        Label(root, text="Login", font=("Arial", 16, "bold"), fg=Utils.purple, bg=Utils.light_gray).pack(pady=20)
        Utils.separator(root).pack(fill=X, pady=1)

    def create_login_section(self, root):
        customer_form = Utils.frame(root)
        customer_form.configure(bg=Utils.light_gray)
        customer_form.pack(pady=10, anchor="center")

        Label(customer_form, text="Username:", fg=Utils.purple, bg=Utils.light_gray, font=("Arial", 11)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.username_entry = Entry(customer_form, width=20)
        self.username_entry.grid(row=0, column=1, pady=5)

        Label(customer_form, text="Email:", fg=Utils.purple, bg=Utils.light_gray, font=("Arial", 11)).grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.email_entry = Entry(customer_form, width=20)
        self.email_entry.grid(row=1, column=1, pady=5)

        Utils.separator(root).pack(fill=X, padx=20, pady=10)

        manager_form = Utils.frame(root)
        manager_form.configure(bg=Utils.light_gray)
        manager_form.pack(pady=0, anchor="center")

        Label(manager_form, text="Manager ID:", fg=Utils.purple, bg=Utils.light_gray, font=("Arial", 11)).grid(row=0, column=0, sticky='w', padx=5, pady=0)
        self.manager_id_entry = Entry(manager_form)
        self.manager_id_entry.grid(row=0, column=1, pady=0)

    def create_button_section(self, root):
        btn_frame = Frame(root)
        btn_frame.pack(side=BOTTOM, fill=X, pady=0)

        login_button = Button(btn_frame, text="Login", padx=10, pady=10, bg=Utils.purple, command=self.login)
        login_button.pack(side=LEFT, expand=True, fill="both")

        exit_button = Button(btn_frame, text="Exit", bg=Utils.purple, command=root.quit)
        exit_button.pack(side=RIGHT, fill="both", expand=True)

    def login(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        manager_id = self.manager_id_entry.get().strip()

        if manager_id:
            try:
                manager = self.users_db.validate_manager(manager_id)
                self._open_dashboard(manager, ManagerDashboardView)
                return
            except Exception as ex:
                ErrorView(self.root, "Invalid Manager ID", str(ex))
                return

        if not username:
            ErrorView(self.root, "Missing Field", "Username is required for customer login.")
            return

        if not email:
            ErrorView(self.root, "Missing Field", "Email is required for customer login.")
            return
