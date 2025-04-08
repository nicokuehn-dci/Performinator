from ttkbootstrap import Frame, Button

class Sidebar(Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)

        self.configure(width=200)
        Button(self, text="Dashboard", command=self.dummy).pack(fill="x", pady=5)
        Button(self, text="Tasks", command=self.dummy).pack(fill="x", pady=5)
        Button(self, text="Reports", command=self.dummy).pack(fill="x", pady=5)
        Button(self, text="Settings", command=self.dummy).pack(fill="x", pady=5)

    def dummy(self):
        print("Menu clicked")
