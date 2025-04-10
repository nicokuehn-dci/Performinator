import sys
import sounddevice as sounddevice
import numpy as np
from threading import Thread, Lock
import customtkinter as ctk
from tkinter import messagebox
from src.gui.elektron_menu import ElektronMenu
from src.gui.performance_grid import PerformanceGrid
# Comment out missing module
# from gui.transport_controls import TransportControls
from sampler.waveform_editor import WaveformEditor
from sampler.engine import SamplerEngine
from mixer.channel_strip import ChannelStrip
from src.sampler.midi_mapper import MidiMapper
from pedalboard import Pedalboard
from src.audio.engine import AudioEngine
import logging
import pipewire as pw
import os
from src.sampler.sample_control import SampleControl
from src.utils.learning_manager import SamplerLoader
from src.utils.state_manager import ProjectManager

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.sampler_loader = SamplerLoader()
        self.sampler = SamplerEngine()
        self.midi_mapper = MidiMapper()
        self.midi_mapper.start_listening_thread()
        self._setup_ui()
        try:
            self.audio_engine = AudioEngine()
            self.audio_thread = Thread(target=self.audio_engine.start)
            self.audio_thread.start()
        except Exception as e:
            logger.error(f"Error initializing AudioEngine: {e}")
            sys.exit(1)
        
    def _setup_ui(self):
        self.title("Performinator")
        self.geometry("1280x720")

        # Central waveform editor
        self.waveform_editor = WaveformEditor()
        self.waveform_editor.pack(fill="both", expand=True)
        
        # Mixer
        self.mixer_frame = ctk.CTkFrame(self)
        self.mixer_frame.pack(side="left", fill="y")
        for i in range(8):
            strip = ChannelStrip(self.mixer_frame, channel_id=i+1)
            strip.pack(pady=5)
        
        # Performance Grid
        self.grid = PerformanceGrid(self)
        self.grid.pack(side="right", fill="both", expand=True)
        
        # Elektron-style menu
        self.menu = ElektronMenu(self)
        self.menu.pack(side="top", fill="x")
        
        # Transport controls
        # self.transport_controls = TransportControls(self)
        # self.transport_controls.pack(side="bottom", fill="x")

        # Connect menu actions to functions
        self.menu.file_menu.actions()[0].configure(command=self.new_file)
        self.menu.file_menu.actions()[1].configure(command=self.open_file)
        self.menu.file_menu.actions()[2].configure(command=self.save_file)
        self.menu.file_menu.actions()[3].configure(command=self.select_ai_protocol)
        self.menu.file_menu.actions()[4].configure(command=self.exit_app)
        self.menu.edit_menu.actions()[0].configure(command=self.undo)
        self.menu.edit_menu.actions()[1].configure(command=self.redo)
        self.menu.edit_menu.actions()[2].configure(command=self.cut)
        self.menu.edit_menu.actions()[3].configure(command=self.copy)
        self.menu.edit_menu.actions()[4].configure(command=self.paste)
        self.menu.view_menu.actions()[0].configure(command=self.zoom_in)
        self.menu.view_menu.actions()[1].configure(command=self.zoom_out)
        self.menu.view_menu.actions()[2].configure(command=self.toggle_full_screen)
        self.menu.help_menu.actions()[0].configure(command=self.show_about)
        self.menu.help_menu.actions()[1].configure(command=self.show_help)
        self.menu.options_menu.actions()[0].configure(command=self.audio_settings)
        self.menu.options_menu.actions()[1].configure(command=self.midi_settings)
        self.menu.options_menu.actions()[2].configure(command=self.ai_protocol_settings)
        self.menu.options_menu.actions()[3].configure(command=self.rescan_audio_library)
        self.menu.options_menu.actions()[4].configure(command=self.show_cloud_feature_message)
        self.menu.components_menu.actions()[0].configure(command=self.add_component)
        self.menu.components_menu.actions()[1].configure(command=self.remove_component)
        self.menu.components_menu.actions()[2].configure(command=self.manage_components)

        # Connect button actions to functions
        self.grid.play_button.configure(command=self.play)
        self.grid.stop_button.configure(command=self.stop)
        self.grid.record_button.configure(command=self.record)

        # Add UI elements for saving and loading patterns
        self.save_pattern_button = ctk.CTkButton(self, text="Save Pattern", command=self.save_pattern)
        self.load_pattern_button = ctk.CTkButton(self, text="Load Pattern", command=self.load_pattern)
        self.pattern_name_input = ctk.CTkEntry(self)
        self.pattern_name_input.insert(0, "Pattern Name")
        self.pattern_status_label = ctk.CTkLabel(self)

        self.grid.layout.addWidget(self.pattern_name_input)
        self.grid.layout.addWidget(self.save_pattern_button)
        self.grid.layout.addWidget(self.load_pattern_button)
        self.grid.layout.addWidget(self.pattern_status_label)

    def __del__(self):
        self.midi_mapper.stop_listening()
        self.audio_engine.stop()
        self.audio_thread.join()

    def closeEvent(self, event):
        self.midi_mapper.stop_listening()
        self.audio_engine.stop()
        self.audio_thread.join()
        event.accept()

    def new_file(self):
        logger.info("New file action triggered")

    def open_file(self):
        logger.info("Open file action triggered")

    def save_file(self):
        logger.info("Save file action triggered")

    def exit_app(self):
        logger.info("Exit app action triggered")
        self.close()

    def undo(self):
        logger.info("Undo action triggered")

    def redo(self):
        logger.info("Redo action triggered")

    def cut(self):
        logger.info("Cut action triggered")

    def copy(self):
        logger.info("Copy action triggered")

    def paste(self):
        logger.info("Paste action triggered")

    def zoom_in(self):
        logger.info("Zoom in action triggered")

    def zoom_out(self):
        logger.info("Zoom out action triggered")

    def toggle_full_screen(self):
        logger.info("Toggle full screen action triggered")
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def show_about(self):
        logger.info("Show about action triggered")

    def show_help(self):
        logger.info("Show help action triggered")

    def play(self):
        logger.info("Play action triggered")

    def stop(self):
        logger.info("Stop action triggered")

    def record(self):
        logger.info("Record action triggered")

    def select_ai_protocol(self):
        logger.info("Select AI Protocol action triggered")
        # Implement the logic to handle AI protocol selection

    def audio_settings(self):
        logger.info("Audio Settings action triggered")
        # Implement the logic to handle Audio Settings

    def midi_settings(self):
        logger.info("MIDI Settings action triggered")
        # Implement the logic to handle MIDI Settings

    def ai_protocol_settings(self):
        logger.info("AI Protocol Settings action triggered")
        # Implement the logic to handle AI Protocol Settings

    def add_component(self):
        logger.info("Add Component action triggered")
        # Implement the logic to handle Add Component

    def remove_component(self):
        logger.info("Remove Component action triggered")
        # Implement the logic to handle Remove Component

    def manage_components(self):
        logger.info("Manage Components action triggered")
        # Implement the logic to handle Manage Components

    def save_pattern(self):
        pattern_name = self.pattern_name_input.get()
        if pattern_name:
            pattern = self.sampler.generate_drum_pattern()  # Example pattern generation
            self.sampler.save_pattern(pattern_name, pattern)
            self.pattern_status_label.configure(text=f"Pattern '{pattern_name}' saved.")
        else:
            self.pattern_status_label.configure(text="Please enter a pattern name.")

    def load_pattern(self):
        pattern_name = self.pattern_name_input.get()
        if pattern_name:
            pattern = self.sampler.load_pattern(pattern_name)
            if pattern:
                self.pattern_status_label.configure(text=f"Pattern '{pattern_name}' loaded.")
                # Implement logic to use the loaded pattern
            else:
                self.pattern_status_label.configure(text=f"Pattern '{pattern_name}' not found.")
        else:
            self.pattern_status_label.configure(text="Please enter a pattern name.")

    def rescan_audio_library(self):
        logger.info("Rescan Audio Library action triggered")
        self.sampler.rescan_audio_library()

    def show_cloud_feature_message(self):
        messagebox.showinfo("Coming Soon", "This feature is coming later.")

    def set_volume(self, channel_id, value):
        self.audio_engine.set_volume(channel_id, value)

    def set_pan(self, channel_id, value):
        self.audio_engine.set_pan(channel_id, value)

    def route_line_in(self, channel_id):
        self.audio_engine.route_line_in(channel_id)

    def load_vst3_plugin(self, path, channel_id):
        self.audio_engine.load_vst3_plugin(path, channel_id)

class SamplerInterface(ctk.CTkFrame):
    def __init__(self, master, sampler_loader, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.sampler_loader = sampler_loader
        self.sample_controls = {}

        # Button to load sample
        self.load_button = ctk.CTkButton(self, text="Load Sample", command=self.load_sample)
        self.load_button.pack(pady=10)

        # Listbox to display samples
        self.sample_listbox = ctk.CTkListbox(self)
        self.sample_listbox.pack(pady=10)

    def load_sample(self):
        try:
            sample_path = self.sampler_loader.load_sample()
            if sample_path:
                sample_name = os.path.basename(sample_path)
                self.sample_controls[sample_name] = SampleControl(sample_name)
                self.sample_listbox.insert(ctk.END, sample_name)
        except Exception as e:
            logger.error(f"Error loading sample: {e}")

    def control_sample(self, sample_name, action):
        if sample_name in self.sample_controls:
            sample_control = self.sample_controls[sample_name]
            if action == "play":
                sample_control.play()
            elif action == "stop":
                sample_control.stop()
            elif action == "loop":
                sample_control.toggle_loop()
            elif action == "pitch":
                new_pitch = float(input("Set pitch value: "))
                sample_control.set_pitch(new_pitch)

class ProjectSelector(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.project_listbox = ctk.CTkListbox(self)
        self.project_listbox.pack(pady=10)

        self.load_button = ctk.CTkButton(self, text="Load Project", command=self.load_project)
        self.load_button.pack(pady=10)

    def load_project(self):
        selected_project = self.project_listbox.get(self.project_listbox.curselection())
        print(f"Loading Project: {selected_project}")
        project_manager = ProjectManager()
        project_data = project_manager.load_project_data(selected_project)
        if project_data:
            self.update_ui_with_project_data(project_data)

    def update_ui_with_project_data(self, project_data):
        # Update the relevant UI elements with the loaded project data
        pass

def main():
    app = ctk.CTk()
    window = MainWindow()
    window.geometry("1280x720")
    project_selector = ProjectSelector(window)
    project_selector.pack(side="left", fill="y")
    window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        sys.exit(1)

# Note on Cloud and Online Features
# Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.
