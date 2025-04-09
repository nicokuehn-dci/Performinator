import customtkinter as ctk

class ElektronMenu(ctk.CTkMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._create_menus()

    def _create_menus(self):
        self.file_menu = self.add_menu("File")
        self.edit_menu = self.add_menu("Edit")
        self.view_menu = self.add_menu("View")
        self.help_menu = self.add_menu("Help")
        self.options_menu = self.add_menu("Options")
        self.components_menu = self.add_menu("Components")

        self._add_file_menu_actions()
        self._add_edit_menu_actions()
        self._add_view_menu_actions()
        self._add_help_menu_actions()
        self._add_options_menu_actions()
        self._add_components_menu_actions()

    def _add_file_menu_actions(self):
        new_action = ctk.CTkMenuItem(self, text="New")
        open_action = ctk.CTkMenuItem(self, text="Open")
        save_action = ctk.CTkMenuItem(self, text="Save")
        exit_action = ctk.CTkMenuItem(self, text="Exit")
        select_ai_protocol_action = ctk.CTkMenuItem(self, text="Select AI Protocol")

        self.file_menu.add(new_action)
        self.file_menu.add(open_action)
        self.file_menu.add(save_action)
        self.file_menu.add(select_ai_protocol_action)
        self.file_menu.add(exit_action)

        new_action.configure(command=self.parent().new_file)
        open_action.configure(command=self.parent().open_file)
        save_action.configure(command=self.parent().save_file)
        select_ai_protocol_action.configure(command=self.parent().select_ai_protocol)
        exit_action.configure(command=self.parent().exit_app)

    def _add_edit_menu_actions(self):
        undo_action = ctk.CTkMenuItem(self, text="Undo")
        redo_action = ctk.CTkMenuItem(self, text="Redo")
        cut_action = ctk.CTkMenuItem(self, text="Cut")
        copy_action = ctk.CTkMenuItem(self, text="Copy")
        paste_action = ctk.CTkMenuItem(self, text="Paste")

        self.edit_menu.add(undo_action)
        self.edit_menu.add(redo_action)
        self.edit_menu.add(cut_action)
        self.edit_menu.add(copy_action)
        self.edit_menu.add(paste_action)

        undo_action.configure(command=self.parent().undo)
        redo_action.configure(command=self.parent().redo)
        cut_action.configure(command=self.parent().cut)
        copy_action.configure(command=self.parent().copy)
        paste_action.configure(command=self.parent().paste)

    def _add_view_menu_actions(self):
        zoom_in_action = ctk.CTkMenuItem(self, text="Zoom In")
        zoom_out_action = ctk.CTkMenuItem(self, text="Zoom Out")
        full_screen_action = ctk.CTkMenuItem(self, text="Full Screen")

        self.view_menu.add(zoom_in_action)
        self.view_menu.add(zoom_out_action)
        self.view_menu.add(full_screen_action)

        zoom_in_action.configure(command=self.parent().zoom_in)
        zoom_out_action.configure(command=self.parent().zoom_out)
        full_screen_action.configure(command=self.parent().toggle_full_screen)

    def _add_help_menu_actions(self):
        about_action = ctk.CTkMenuItem(self, text="About")
        help_action = ctk.CTkMenuItem(self, text="Help")

        self.help_menu.add(about_action)
        self.help_menu.add(help_action)

        about_action.configure(command=self.parent().show_about)
        help_action.configure(command=self.parent().show_help)

    def _add_options_menu_actions(self):
        audio_settings_action = ctk.CTkMenuItem(self, text="Audio Settings")
        midi_settings_action = ctk.CTkMenuItem(self, text="MIDI Settings")
        ai_protocol_settings_action = ctk.CTkMenuItem(self, text="AI Protocol Settings")
        rescan_audio_library_action = ctk.CTkMenuItem(self, text="Rescan Audio Library")
        cloud_feature_action = ctk.CTkMenuItem(self, text="Cloud Feature")

        self.options_menu.add(audio_settings_action)
        self.options_menu.add(midi_settings_action)
        self.options_menu.add(ai_protocol_settings_action)
        self.options_menu.add(rescan_audio_library_action)
        self.options_menu.add(cloud_feature_action)

        audio_settings_action.configure(command=self.parent().audio_settings)
        midi_settings_action.configure(command=self.parent().midi_settings)
        ai_protocol_settings_action.configure(command=self.parent().ai_protocol_settings)
        rescan_audio_library_action.configure(command=self.parent().rescan_audio_library)
        cloud_feature_action.configure(command=self.show_cloud_feature_message)

    def _add_components_menu_actions(self):
        add_component_action = ctk.CTkMenuItem(self, text="Add Component")
        remove_component_action = ctk.CTkMenuItem(self, text="Remove Component")
        manage_components_action = ctk.CTkMenuItem(self, text="Manage Components")

        self.components_menu.add(add_component_action)
        self.components_menu.add(remove_component_action)
        self.components_menu.add(manage_components_action)

        add_component_action.configure(command=self.parent().add_component)
        remove_component_action.configure(command=self.parent().remove_component)
        manage_components_action.configure(command=self.parent().manage_components)

    def show_cloud_feature_message(self):
        ctk.CTkMessageBox.showinfo("Coming Soon", "This feature is coming later.")
