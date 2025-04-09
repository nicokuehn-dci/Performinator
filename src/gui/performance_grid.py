import customtkinter as ctk

class PerformanceGrid(ctk.CTkFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = ctk.CTkFrame(self)
        self.play_button = ctk.CTkButton(self, text="Play")
        self.stop_button = ctk.CTkButton(self, text="Stop")
        self.record_button = ctk.CTkButton(self, text="Record")
        self.layout.pack(pady=10, padx=10)
        self.play_button.pack(pady=5)
        self.stop_button.pack(pady=5)
        self.record_button.pack(pady=5)
        self.setLayout(self.layout)

        self.play_button.configure(command=self.parent().play)
        self.stop_button.configure(command=self.parent().stop)
        self.record_button.configure(command=self.parent().record)
