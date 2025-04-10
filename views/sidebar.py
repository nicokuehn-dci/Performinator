import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=200)
        ctk.CTkButton(self, text="Dashboard", command=self.load_dashboard).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Sequencer", command=self.load_sequencer).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Sampler", command=self.load_sampler).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Effects", command=self.load_effects).pack(fill="x", pady=5)
        ctk.CTkButton(self, text="Settings", command=self.load_settings).pack(fill="x", pady=5)

    def load_dashboard(self):
        print("Loading Dashboard...")
        # Add logic to fetch and display dashboard data

    def load_sequencer(self):
        print("Loading Sequencer...")
        # Add logic to initialize sequencer interface

    def load_sampler(self):
        print("Loading Sampler...")
        # Add logic to load sampler functionalities

    def load_effects(self):
        print("Loading Effects...")
        # Add logic to display effects rack

    def load_settings(self):
        print("Loading Settings...")
        # Add logic to load settings interface
