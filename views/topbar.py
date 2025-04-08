from ttkbootstrap import Frame, Label

class Topbar(Frame):
    def __init__(self, master):
        super().__init__(master, padding=(10, 5))

        Label(self, text="Performinator", font=("Helvetica", 16)).pack(side="left")
