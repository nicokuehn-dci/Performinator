import customtkinter as ctk

class Topbar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, padding=(10, 5))

        ctk.CTkLabel(self, text="Performinator", font=("Helvetica", 16)).pack(side="left")
