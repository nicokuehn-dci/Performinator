import customtkinter as ctk
import tkinter as tk
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

class ElektronMenu(tk.Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._create_menus()

    def _create_menus(self):
        self.file_menu = tk.Menu(self, tearoff=0)
        self.edit_menu = tk.Menu(self, tearoff=0)
        self.view_menu = tk.Menu(self, tearoff=0)
        self.help_menu = tk.Menu(self, tearoff=0)
        self.options_menu = tk.Menu(self, tearoff=0)
        self.components_menu = tk.Menu(self, tearoff=0)

        self.add_cascade(label="File", menu=self.file_menu)
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.add_cascade(label="View", menu=self.view_menu)
        self.add_cascade(label="Help", menu=self.help_menu)
        self.add_cascade(label="Options", menu=self.options_menu)
        self.add_cascade(label="Components", menu=self.components_menu)

        self._add_file_menu_actions()
        self._add_edit_menu_actions()
        self._add_view_menu_actions()
        self._add_help_menu_actions()
        self._add_options_menu_actions()
        self._add_components_menu_actions()

    def _add_file_menu_actions(self):
        self.file_menu.add_command(label="New", command=self.parent().new_file)
        self.file_menu.add_command(label="Open", command=self.parent().open_file)
        self.file_menu.add_command(label="Save", command=self.parent().save_file)
        self.file_menu.add_command(label="Select AI Protocol", command=self.parent().select_ai_protocol)
        self.file_menu.add_command(label="Exit", command=self.parent().exit_app)

    def _add_edit_menu_actions(self):
        self.edit_menu.add_command(label="Undo", command=self.parent().undo)
        self.edit_menu.add_command(label="Redo", command=self.parent().redo)
        self.edit_menu.add_command(label="Cut", command=self.parent().cut)
        self.edit_menu.add_command(label="Copy", command=self.parent().copy)
        self.edit_menu.add_command(label="Paste", command=self.parent().paste)

    def _add_view_menu_actions(self):
        self.view_menu.add_command(label="Zoom In", command=self.parent().zoom_in)
        self.view_menu.add_command(label="Zoom Out", command=self.parent().zoom_out)
        self.view_menu.add_command(label="Full Screen", command=self.parent().toggle_full_screen)

    def _add_help_menu_actions(self):
        self.help_menu.add_command(label="About", command=self.parent().show_about)
        self.help_menu.add_command(label="Help", command=self.parent().show_help)

    def _add_options_menu_actions(self):
        self.options_menu.add_command(label="Audio Settings", command=self.parent().audio_settings)
        self.options_menu.add_command(label="MIDI Settings", command=self.parent().midi_settings)
        self.options_menu.add_command(label="AI Protocol Settings", command=self.parent().ai_protocol_settings)
        self.options_menu.add_command(label="Rescan Audio Library", command=self.parent().rescan_audio_library)
        self.options_menu.add_command(label="Cloud Feature", command=self.show_cloud_feature_message)

    def _add_components_menu_actions(self):
        self.components_menu.add_command(label="Add Component", command=self.parent().add_component)
        self.components_menu.add_command(label="Remove Component", command=self.parent().remove_component)
        self.components_menu.add_command(label="Manage Components", command=self.parent().manage_components)

    def show_cloud_feature_message(self):
        tk.messagebox.showinfo("Coming Soon", "This feature is coming later.")
