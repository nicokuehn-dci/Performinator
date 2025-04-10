import customtkinter as ctk
import json

# Apply custom theme settings
def apply_custom_theme():
    ctk.set_appearance_mode("dark")  # Set dark mode

    # Save the theme dictionary as a JSON file
    theme_path = "custom_theme.json"
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

class Topbar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, padding=(10, 5))

        ctk.CTkLabel(self, text="Performinator", font=("Helvetica", 16)).pack(side="left")
