import tkinter as tk
from ttkbootstrap import Frame
from views.sidebar import Sidebar
from views.topbar import Topbar
from views.content import ContentArea

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
