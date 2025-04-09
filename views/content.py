import customtkinter as ctk

class ContentArea(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, padding=10)

        ctk.CTkLabel(self, text="Welcome to Performinator!", font=("Helvetica", 12)).pack()
