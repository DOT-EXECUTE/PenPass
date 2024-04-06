from tkinter import messagebox as msbx
import customtkinter as ctk
from MainApp import *
import PIL.Image
import time

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")
        self.title("PenPass Login")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        # Create a frame for the login section with a gray background
        self.login_frame = ctk.CTkFrame(master=self, width=30, height=70, fg_color="#000208", corner_radius=13)
        self.login_frame.grid(row=0, column=1, padx=15)  # Position the frame with padding

        # Load your image (replace "image.png" with your image path)
        self.bg_image = ctk.CTkImage(dark_image=PIL.Image.open("Login-page_image.jpeg"), size=(275,400))
        self.bg_image = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image.grid(row=0, column=0)

        # Create login UI elements within the login frame
        self.username_label = ctk.CTkLabel(master=self.login_frame, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(master=self.login_frame, width=200)
        self.username_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(master=self.login_frame, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ctk.CTkEntry(master=self.login_frame, width=200, show="*")  # Hide password characters
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(master=self.login_frame, text="Login", command=self.handle_login)
        self.login_button.pack(pady=10)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate username and password (replace with actual validation)
        if username == "EXE" and password == "PenPass":

            # Create an instance of the main app window (assuming it's defined in a separate class)
            main_app = App()

            #Destroy the login window and create a new main app window
            self.destroy()  # Destroy the login window
            time.wait(0.5)
            main_app = App()  # Create a new instance of the main app window
            main_app.mainloop()  # Start the event loop for the main app

        else:
            msbx.showinfo("You have given invalid info", "The provided username or password is incorrect")

app = LoginPage()
app.mainloop()  # Start the event loop
