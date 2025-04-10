import customtkinter as ctk
import json

# Apply custom theme settings
def apply_custom_theme():
    ctk.set_appearance_mode("dark")  # Set dark mode

    # Save the theme dictionary as a JSON file
    theme_path = "performance_grid_theme.json"
    theme_data = {
        "button": {"fg_color": "#FF4500", "hover_color": "#FF6347", "border_color": "#FF4500"},
        "label": {"text_color": "#FF4500"},
        "entry": {"fg_color": "#2E2E2E", "text_color": "#FF4500"}
    }
    with open(theme_path, "w") as theme_file:
        json.dump(theme_data, theme_file)

    # Use the JSON file path for the theme
    ctk.set_default_color_theme(theme_path)

apply_custom_theme()

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
