import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=200)
        ctk.CTkButton(self, text="Dashboard", command=self.dummy).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Tasks", command=self.dummy).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Reports", command=self.dummy).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Settings", command=self.dummy).pack(fill="x", pady=5)

    def dummy(self):
        print("Menu clicked")
