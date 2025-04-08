from ttkbootstrap import Frame, Label

class ContentArea(Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)

        Label(self, text="Welcome to Performinator!", font=("Helvetica", 12)).pack()
