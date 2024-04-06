import customtkinter as ctk
from Encryption import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("772x508")
        self.title("PenPass")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.Navigation = ctk.CTkFrame(master=self, width=80, height=508, fg_color="purple", corner_radius=0)
        self.Navigation.grid(row=0, column=0, rowspan=4)

        self.PasswordFrame = ctk.CTkScrollableFrame(master=self, width=400, height=508, fg_color="#000208", corner_radius=0)
        self.PasswordFrame.grid(row=0, column=1, rowspan=4, columnspan=4)

        self.PasswordSlot0 = ctk.CTkLabel(self.PasswordFrame, text="this is where password 1 is!", font_size=20)
        self.PasswordSlot1 = ctk.CTkLabel(self.PasswordFrame, text="this is where password 2 is!")
        self.PasswordSlot2 = ctk.CTkLabel(self.PasswordFrame, text="this is where password 3 is!")
        self.PasswordSlot3 = ctk.CTkLabel(self.PasswordFrame, text="this is where password 4 is!")
        
        self.PasswordSlot0.grid(row=0, column=0, padx=10, pady=20, stick="ew")
        self.PasswordSlot1.grid(row=1, column=0, padx=10, pady=20, stick="ew")
        self.PasswordSlot2.grid(row=2, column=0, padx=10, pady=20, stick="ew")
        self.PasswordSlot3.grid(row=3, column=0, padx=10, pady=20, stick="ew")


app = App()
app.mainloop()
        