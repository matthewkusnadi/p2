# LoginView.py
from tkinter import Tk, Frame, Label, Entry, X, E, BOTTOM, LEFT, RIGHT, messagebox, Toplevel
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

        # instantiate your Users "database"
        self.users_db = Users()

        # logo
        logo_f = Frame(root, bg=Utils.light_gray)
        logo_f.pack(pady=20)
        try:
            lbl = Utils.image(logo_f, "image/cat_banner.jpg")
            lbl.pack()
        except:
            pass

        Utils.separator(root).pack(fill=X, padx=20, pady=5)
        Utils.label(root, "Login").pack(pady=10)
        Utils.separator(root).pack(fill=X, padx=20, pady=5)

        form = Utils.frame(root)
        form.configure(bg=Utils.light_gray)
        form.pack(pady=20, padx=20, fill=X)

        Label(form, text="Username:", fg=Utils.purple, bg=Utils.light_gray).grid(row=0, column=0, sticky=E, pady=5)
        self.user_ent = Entry(form, width=30)
        self.user_ent.grid(row=0, column=1, pady=5)

        Label(form, text="Email:", fg=Utils.purple, bg=Utils.light_gray).grid(row=1, column=0, sticky=E, pady=5)
        self.email_ent = Entry(form, width=30)
        self.email_ent.grid(row=1, column=1, pady=5)

        Label(form, text="Manager ID:", fg=Utils.purple, bg=Utils.light_gray).grid(row=2, column=0, sticky=E, pady=5)
        self.mgr_ent = Entry(form, width=30)
        self.mgr_ent.grid(row=2, column=1, pady=5)

        Frame(root, height=40, bg=Utils.light_gray).pack(fill=X)
        btn_f = Frame(root, bg=Utils.light_gray)
        btn_f.pack(side=BOTTOM, fill=X)
        Utils.button(btn_f, "Login", self.login).pack(side=LEFT, expand=True, fill=X, ipady=10)
        Utils.button(btn_f, "Exit", root.quit).pack(side=RIGHT, expand=True, fill=X, ipady=10)

    def login(self):
        username = self.user_ent.get().strip()
        email    = self.email_ent.get().strip()
        mgr_id   = self.mgr_ent.get().strip()

        if not username:
            return messagebox.showerror("Error", "Username is required")

        # manager login if ID provided
        if mgr_id:
            try:
                manager = self.users_db.validate_manager(mgr_id)
                self._open_dashboard(manager, ManagerDashboardView)
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
        else:
            if not email:
                return messagebox.showerror("Error", "Email is required for customer login")
            customer = self.users_db.validate_customer(username, email)
            if customer:
                self._open_dashboard(customer, CustomerDashboardView)
            else:
                messagebox.showerror("Error", "Invalid username or email")

    def _open_dashboard(self, user_obj, ViewClass):
        # hide login
        self.root.withdraw()
        win = Toplevel(self.root)
        ViewClass(win, user_obj)
        # when dash closes, destroy and re-show login
        win.protocol("WM_DELETE_WINDOW", lambda: (win.destroy(), self.root.deiconify()))

if __name__ == "__main__":
    root = Tk()
    LoginView(root)
    root.mainloop()
