import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
import customtkinter as ctk
from ttkbootstrap import Frame
from views.sidebar import Sidebar
from views.topbar import Topbar
from views.content import ContentArea

GLOW_ORANGE = "#FF8000"

class MainView(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsw")

        self.topbar = Topbar(self)
        self.topbar.grid(row=0, column=1, sticky="new")

        self.content = ContentArea(self)
        self.content.grid(row=1, column=1, sticky="nsew")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.saturation = ctk.CTkCheckBox(self, text="Saturation",
                                          fg_color=GLOW_ORANGE,
                                          hover_color=GLOW_ORANGE)

        # Connect sidebar buttons to content updates
        self.sidebar.load_dashboard = self.update_content("Dashboard")
        self.sidebar.load_sequencer = self.update_content("Sequencer")
        self.sidebar.load_sampler = self.update_content("Sampler")
        self.sidebar.load_effects = self.update_content("Effects")
        self.sidebar.load_settings = self.update_content("Settings")

    def update_content(self, section):
        def inner():
            self.content.update_content(f"<h2>{section}</h2><p>Content for {section}.</p>")
        return inner
