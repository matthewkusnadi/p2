# ErrorView.py
from tkinter import Toplevel, Frame, Label, X
from Utils import Utils

class ErrorView:
    def __init__(self, parent, title, message):
        # Create window with fixed size
        self.error_window = Toplevel(parent)
        self.error_window.title("Error")
        
        # Hard-code window dimensions to 550x550
        self.error_window.geometry("550x550")
        self.error_window.minsize(550, 550)
        self.error_window.maxsize(550, 550)
        self.error_window.resizable(False, False)
        
        self.error_window.configure(bg=Utils.light_gray)
        
        # Make window modal
        self.error_window.transient(parent)
        
        # Main container
        main_frame = Frame(self.error_window, width=550, height=550, bg=Utils.light_gray)
        main_frame.pack(fill="both", expand=True)
        main_frame.pack_propagate(False)  # Prevent frame from shrinking
        
        # Add the error image
        image_frame = Frame(main_frame, bg=Utils.light_gray)
        image_frame.pack(pady=(50, 30))
        error_image = Utils.image(image_frame, "image/error_banner.jpg")
        error_image.pack()
        
        # Error title (e.g., "InvalidOperationException")
        Label(
            main_frame,
            text=title,
            fg="red",
            bg=Utils.light_gray,
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 20))

        Utils.separator(self).pack(fill=X, pady=1)

        
        # Error message (e.g., "Id must be an integer")
        Label(
            main_frame,
            text=message,
            fg=Utils.purple,
            bg=Utils.light_gray,
            font=("Arial", 14)
        ).pack()
        
        # Close button
        Utils.button(main_frame, "Close", self.close_window).pack(padx=100)
    
    def close_window(self):
        self.error_window.de