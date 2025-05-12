from tkinter import Tk, Frame, Label, Button, Canvas, Scrollbar, LEFT, RIGHT, X, Y
from Utils import Utils
from model.Animals import Animals

class ManagerDashboardView:
    def __init__(self, root):
        self.root = root
        self.animals = Animals().insert_seed_data()  # Using actual Animals class
        
        root.title("Manager Dashboard")
        root.geometry("700x600")
        root.configure(bg=Utils.light_gray)
        
        # Main container
        self.main_container = Frame(root, bg=Utils.light_gray)
        self.main_container.pack(fill="both", expand=True)
        
        # Header with logo
        self.create_header()
        
        # Title bar
        self.create_title_bar()
        
        # Animal Categories and List
        self.create_animal_categories()
        
        # Initialize the animal list frame with scrollbar
        self.create_animal_list_frame()
        
        # Action buttons at the bottom
        self.create_action_buttons()

    def create_header(self):
        # Header frame with logo or fallback text
        header_frame = Frame(self.main_container, bg=Utils.light_gray)
        header_frame.pack(fill=X, pady=20)
        
        try:
            logo_label = Utils.image(header_frame, "image/cat_banner.jpg")
            logo_label.pack()
        except Exception as e:
            Label(
                header_frame, 
                text="Manager Dashboard",
                font=("Arial", 24, "bold"),
                fg=Utils.purple,
                bg=Utils.light_gray
            ).pack()

    def create_title_bar(self):
        # Title with text
        title_bar = Frame(self.main_container, bg=Utils.light_gray)
        title_bar.pack(fill=X, pady=10)
        Utils.label(title_bar, "Manager Dashboard").pack()

    def create_animal_categories(self):
        # Frame for animal categories (Dog, Cat, Rabbit)
        categories_frame = Frame(self.main_container, bg=Utils.light_gray)
        categories_frame.pack(fill=X, padx=20, pady=10)
        
        # Match the actual class names used in your filter
        categories = ["Cat", "Dog", "Rabbit"]
        
        for category in categories:
            button = Utils.filter_button(
                categories_frame,
                text=category,
                callback=lambda cat=category: self.display_animals_by_category(cat)
            )
            button.pack(side=LEFT, expand=True, fill=X, padx=2)

    def create_animal_list_frame(self):
        # Create the initial animal list frame
        self.animal_list_frame = Frame(self.main_container, bg="white")
        self.animal_list_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def display_animals_by_category(self, category):
        # Display animals by category using the get_animals_by_filter method
        print(f"Showing animals for: {category}")
        self.clear_animal_list()
        
        # Create a canvas with scrollbar for the animal list
        canvas = Canvas(self.animal_list_frame, bg="white")
        scrollbar = Scrollbar(self.animal_list_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Use get_animals_by_filter to get animals of the selected category
        animals = self.animals.get_animals_by_filter(category)
        
        if not animals:
            Label(
                scrollable_frame,
                text=f"No {category}s found",
                font=("Arial", 12),
                fg="#333333",
                bg="white"
            ).pack(fill=X, padx=10, pady=5)
        else:
            for animal in animals:
                # Assuming your animal classes have name and age attributes
                Label(
                    scrollable_frame,
                    text=f"{animal.name} - {animal.age} years old",
                    font=("Arial", 12),
                    fg="#333333",
                    bg="white"
                ).pack(fill=X, padx=10, pady=5)
    
    def clear_animal_list(self):
        # Clear previous animal list
        if hasattr(self, 'animal_list_frame'):
            for widget in self.animal_list_frame.winfo_children():
                widget.destroy()

    def create_action_buttons(self):
        # Bottom action buttons (User List, Add, Remove, Close)
        button_frame = Frame(self.main_container, bg=Utils.light_gray, height=60)
        button_frame.pack(side="bottom", fill=X, pady=10)

        Utils.button(button_frame, "User List", self.view_users).pack(side=LEFT, expand=True, fill=X, padx=5)
        Utils.button(button_frame, "Add", self.add_animal).pack(side=LEFT, expand=True, fill=X, padx=5)
        Utils.button(button_frame, "Remove", self.remove_animal).pack(side=LEFT, expand=True, fill=X, padx=5)
        Utils.button(button_frame, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X, padx=5)

    def view_users(self):
        print("View Users clicked")
        # Implement user list view

    def add_animal(self):
        print("Add Animal clicked")
        # Implement add animal functionality

    def remove_animal(self):
        print("Remove Animal clicked")
        # Implement remove animal functionality


# Test function to run just this view
def test_manager_dashboard():
    root = Tk()
    ManagerDashboardView(root)
    root.mainloop()

if __name__ == "__main__":
    test_manager_dashboard()