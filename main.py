import logging
import os
import subprocess
import sys

# Ensure required libraries are installed
try:
    from pydbus import SystemBus
    from pyudev import Context, Monitor, MonitorObserver
    from tkinter import filedialog
    import customtkinter as ctk
except ImportError as e:
    print("Required libraries are not installed. Please install them using 'pip install pydbus pyudev customtkinter'.")
    raise

from src.utils.learning_manager import LearningManager
from src.audio.midi_handler import MidiController

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class LoopLoader:

    def __init__(self):
        self.current_loop_path = None

    def import_loop(self):
        """Open file dialog to import a loop sample (WAV, MP3, etc.)"""
        filetypes = [("Audio Files", "*.wav *.mp3 *.aiff *.flac")]
        path = filedialog.askopenfilename(
            title="Import Loop",
            filetypes=filetypes
        )
        if path:
            self.current_loop_path = path
            print(f"[LoopLoader] Loop imported: {os.path.basename(path)}")
        return path

    def get_loop_name(self):
        if self.current_loop_path:
            return os.path.basename(self.current_loop_path)
        return "No loop loaded"

    def get_loop_path(self):
        return self.current_loop_path

    def play_loop(self):
        if self.current_loop_path:
            print(f"[LoopLoader] Playing loop: {self.current_loop_path}")
        else:
            print("[LoopLoader] No loop loaded.")

class ArtistProfileForm(ctk.CTkFrame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.artist_name_label = ctk.CTkLabel(self, text="Artist Name:")
        self.artist_name_label.pack(pady=5)
        self.artist_name_entry = ctk.CTkEntry(self)
        self.artist_name_entry.pack(pady=5)

        self.profile_picture_label = ctk.CTkLabel(
            self,
            text="Profile Picture (URL or File Path):"
        )
        self.profile_picture_label.pack(pady=5)
        self.profile_picture_entry = ctk.CTkEntry(self)
        self.profile_picture_entry.pack(pady=5)

    def get_artist_profile(self):
        artist_name = self.artist_name_entry.get()
        profile_picture = self.profile_picture_entry.get()
        return artist_name, profile_picture

class NewProjectForm(ctk.CTkFrame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.genre_label = ctk.CTkLabel(self, text="Genre:")
        self.genre_label.pack(pady=5)
        self.genre_dropdown = ctk.CTkOptionMenu(
            self,
            values=["Pop", "Rock", "Electronic", "Jazz"]
        )
        self.genre_dropdown.pack(pady=5)

        self.bpm_label = ctk.CTkLabel(self, text="BPM:")
        self.bpm_label.pack(pady=5)
        self.bpm_entry = ctk.CTkEntry(self)
        self.bpm_entry.pack(pady=5)

        self.scale_label = ctk.CTkLabel(self, text="Scale:")
        self.scale_label.pack(pady=5)
        self.scale_dropdown = ctk.CTkOptionMenu(
            self,
            values=["Major", "Minor", "Pentatonic", "Blues"]
        )
        self.scale_dropdown.pack(pady=5)

        self.create_button = ctk.CTkButton(
            self,
            text="Create New Project",
            command=self.create_project
        )
        self.create_button.pack(pady=10)

    def create_project(self):
        genre = self.genre_dropdown.get()
        bpm = self.bpm_entry.get()
        scale = self.scale_dropdown.get()

        project_details = {
            "genre": genre,
            "bpm": bpm,
            "scale": scale
        }

        project_path = os.path.join(
            "projects",
            f"{genre}_{bpm}_{scale}.txt"
        )
        with open(project_path, "w", encoding="utf-8") as file:
            file.write(str(project_details))

        print(f"New Project Created: Genre={genre}, BPM={bpm}, Scale={scale}")
        print(f"Project details saved to {project_path}")

def setup_virtualenv():
    try:
        logger.info("🔧 Setting up virtual environment...")
        if not os.path.exists("daw_env"):
            subprocess.run(
                [sys.executable, "-m", "venv", "daw_env"],
                check=True
            )
        activate_script = (
            "daw_env/bin/activate"
            if os.name != "nt"
            else "daw_env\\Scripts\\activate"
        )
        activate_command = (
            f"source {activate_script}"
            if os.name != "nt"
            else activate_script
        )
        subprocess.run(activate_command, shell=True, check=True)
        logger.info("Virtual environment activated.")
    except subprocess.CalledProcessError as e:
        logger.error("Error setting up virtual environment: %s", e)
        if e.returncode == 1:
            logger.error("Severe error: Virtual environment setup failed.")
            raise
        else:
            logger.error("Non-severe error: Continuing execution.")

def install_dependencies():
    try:
        logger.info("📦 Installing Python dependencies...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            check=True
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        logger.info("Python dependencies installed.")
    except subprocess.CalledProcessError as e:
        logger.error("Error installing Python dependencies: %s", e)
        if e.returncode == 1:
            logger.error("Severe error: Dependency installation failed.")
            raise
        else:
            logger.error("Non-severe error: Continuing execution.")

def setup_pipewire_metadata():
    """
    Sets up PipeWire metadata for DAW integration.
    """
    try:
        logger.info("🎵 Setting up PipeWire metadata for DAW integration...")
        bus = SystemBus()
        pipewire = bus.get("org.freedesktop.pipewire1")
        pipewire.SetMetadata("example.key", "example.value")
        logger.info("PipeWire metadata setup complete.")
    except Exception as e:
        logger.error("Error setting up PipeWire metadata: %s", e)
        raise

def monitor_midi_hotplug():
    """
    Monitors MIDI device hotplug events using libudev.
    """
    try:
        logger.info("🎹 Monitoring MIDI device hotplug events...")
        context = Context()
        monitor = Monitor.from_netlink(context)
        monitor.filter_by(subsystem="sound")
        observer = MonitorObserver(monitor, callback=midi_hotplug_callback)
        observer.start()
        logger.info("MIDI hotplug monitoring started.")
    except Exception as e:
        logger.error("Error monitoring MIDI hotplug events: %s", e)
        raise

def midi_hotplug_callback(action, device):
    """
    Callback for MIDI device hotplug events.
    """
    if action == "add":
        logger.info("MIDI device connected: %s", device.device_node)
    elif action == "remove":
        logger.info("MIDI device disconnected: %s", device.device_node)

def launch_electron_app():
    try:
        subprocess.run(["npx", "electron", "."], check=True)
    except subprocess.CalledProcessError as e:
        logger.error("Error launching Performinator: %s", e)
        sys.exit(1)

def main():
    try:
        setup_virtualenv()
        install_dependencies()
        setup_pipewire_metadata()
        monitor_midi_hotplug()
        learning_manager = LearningManager()
        learning_manager.capture_user_input("Setup and dependencies installed")
        
        midi_controller = MidiController()
        midi_controller.open_port()
        midi_controller.listen_for_cc()
        
        launch_electron_app()
        learning_manager.capture_user_output("Performinator launched")
    except Exception as e:
        logger.error("Unhandled exception: %s", e)
        if isinstance(e, subprocess.CalledProcessError) and e.returncode == 1:
            logger.error("Severe error: Unhandled exception occurred.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")

def show_cloud_feature_message():
    logger.info("This is a feature that is coming later.")

if __name__ == "__main__":
    try:
        launch_electron_app()
    except Exception as e:
        logger.error("Unhandled exception: %s", e)
        if isinstance(e, subprocess.CalledProcessError) and e.returncode == 1:
            logger.error("Severe error: Unhandled exception occurred.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")

while True:
    line = sys.stdin.readline().strip()
    if line == 'dashboard':
        print('Loading Dashboard...')
    elif line == 'sequencer':
        print('Loading Sequencer...')
    elif line == 'sampler':
        print('Loading Sampler...')
    elif line == 'effects':
        print('Loading Effects...')
    elif line == 'settings':
        print('Loading Settings...')
    else:
        print('Unknown command:', line)
