# LoginView.py
from tkinter import Tk, Frame, Label, Entry, X, E, BOTTOM, LEFT, RIGHT, TOP, messagebox, Toplevel
from Utils import Utils
from model.Users import Users
from model.Customer import Customer
from model.Manager import Manager
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView

class LoginView:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("550x700")
        root.configure(bg=Utils.light_gray)

        # Initialize user database
        self.users_db = Users()
        
        # Create main content area
        self.create_logo_section(root)
        self.create_login_section(root)
        self.create_button_section(root)
    
    def create_logo_section(self, root):
        # Logo frame
        logo_frame = Frame(root, bg=Utils.light_gray)
        logo_frame.pack(pady=20, expand=True)
        
        # Logo image
        try:
            logo_label = Utils.image(logo_frame, "image/cat_banner.jpg")
            logo_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
            # Fallback text if image can't be loaded
            Label(logo_frame, text="PROG2\nADOPTION CENTRE", 
                  font=("Arial", 24, "bold"), fg="#006666", bg=Utils.light_gray).pack(pady=40)
        
        # Add separator
        Utils.separator(root).pack(fill=X, padx=20, pady=5)
        Utils.label(root, "Login").pack(pady=10)
        Utils.separator(root).pack(fill=X, padx=20, pady=5)
    
    def create_login_section(self, root):
        # Form frame
        form = Utils.frame(root)
        form.configure(bg=Utils.light_gray)
        form.pack(pady=20, padx=20, fill=X)
        
        # Username field
        Label(form, text="Username:", fg=Utils.purple, bg=Utils.light_gray).grid(row=0, column=0, sticky=E, pady=5)
        self.username_entry = Entry(form, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)
        
        # Email field
        Label(form, text="Email:", fg=Utils.purple, bg=Utils.light_gray).grid(row=1, column=0, sticky=E, pady=5)
        self.email_entry = Entry(form, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)
        
        # Manager ID field
        Label(form, text="Manager ID:", fg=Utils.purple, bg=Utils.light_gray).grid(row=2, column=0, sticky=E, pady=5)
        self.manager_id_entry = Entry(form, width=30)
        self.manager_id_entry.grid(row=2, column=1, pady=5)
    
    def create_button_section(self, root):
        # Spacer
        Frame(root, height=40, bg=Utils.light_gray).pack(fill=X)
        
        # Button frame
        btn_frame = Frame(root, bg=Utils.light_gray)
        btn_frame.pack(side=BOTTOM, fill=X)
        
        # Login and Exit buttons
        Utils.button(btn_frame, "Login", self.login).pack(side=LEFT, expand=True, fill=X, ipady=10)
        Utils.button(btn_frame, "Exit", root.quit).pack(side=RIGHT, expand=True, fill=X, ipady=10)
    
    def login(self):
        # Get user input
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        manager_id = self.manager_id_entry.get().strip()
        
        # Validate input
        if not username:
            messagebox.showerror("Error", "Username is required")
            return
        
        # Manager login path
        if manager_id:
            try:
                manager = self.users_db.validate_manager(manager_id)
                self._open_dashboard(manager, ManagerDashboardView)
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
        # Customer login path
        else:
            if not email:
                messagebox.showerror("Error", "Email is required for customer login")
                return
                
            customer = self.users_db.validate_customer(username, email)
            if customer:
                self._open_dashboard(customer, CustomerDashboardView)
            else:
                messagebox.showerror("Error", "Invalid username or email")
    
    def _open_dashboard(self, user_obj, ViewClass):
        # Hide the login window
        self.root.withdraw()
        
        # Create the dashboard window
        dashboard_window = Toplevel(self.root)
        ViewClass(dashboard_window, user_obj)
        
        # Restore login window when dashboard is closed
        dashboard_window.protocol("WM_DELETE_WINDOW", 
                                 lambda: (dashboard_window.destroy(), self.root.deiconify()))

if __name__ == "__main__":
    root = Tk()
    LoginView(root)
    root.mainloop()