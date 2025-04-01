import sys
import sounddevice as sounddevice
import numpy as np
from threading import Thread, Lock
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget
from gui.elektron_menu import ElektronMenu
from gui.performance_grid import PerformanceGrid
from gui.transport_controls import TransportControls
from sampler.waveform_editor import WaveformEditor
from sampler.engine import SamplerEngine
from mixer.channel_strip import ChannelStrip
from src.sampler.midi_mapper import MidiMapper
from pedalboard import Pedalboard
from src.audio.engine import AudioEngine
import logging
import pipewire as pw

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        # Central waveform editor
        self.waveform_editor = WaveformEditor()
        self.setCentralWidget(self.waveform_editor)
        
        # Dock widgets
        self.mixer_dock = QDockWidget("Mixer", self)
        self.mixer_dock.setWidget(ChannelStrip())
        self.addDockWidget(2, self.mixer_dock)
        
        self.grid = PerformanceGrid()
        grid_widget = QWidget()
        grid_widget.setLayout(self.grid)
        self.addDockWidget(1, QDockWidget("Performance Grid", self)).setWidget(grid_widget)
        
        # Elektron-style menu
        self.menu = ElektronMenu()
        self.addDockWidget(1, QDockWidget("Controls", self)).setWidget(self.menu)
        
        # Transport controls
        self.transport_controls = TransportControls()
        self.addDockWidget(1, QDockWidget("Transport", self)).setWidget(self.transport_controls)

        # Connect menu actions to functions
        self.menu.file_menu.actions()[0].triggered.connect(self.new_file)
        self.menu.file_menu.actions()[1].triggered.connect(self.open_file)
        self.menu.file_menu.actions()[2].triggered.connect(self.save_file)
        self.menu.file_menu.actions()[3].triggered.connect(self.select_ai_protocol)
        self.menu.file_menu.actions()[4].triggered.connect(self.exit_app)
        self.menu.edit_menu.actions()[0].triggered.connect(self.undo)
        self.menu.edit_menu.actions()[1].triggered.connect(self.redo)
        self.menu.edit_menu.actions()[2].triggered.connect(self.cut)
        self.menu.edit_menu.actions()[3].triggered.connect(self.copy)
        self.menu.edit_menu.actions()[4].triggered.connect(self.paste)
        self.menu.view_menu.actions()[0].triggered.connect(self.zoom_in)
        self.menu.view_menu.actions()[1].triggered.connect(self.zoom_out)
        self.menu.view_menu.actions()[2].triggered.connect(self.toggle_full_screen)
        self.menu.help_menu.actions()[0].triggered.connect(self.show_about)
        self.menu.help_menu.actions()[1].triggered.connect(self.show_help)

        # Connect button actions to functions
        self.grid.play_button.clicked.connect(self.play)
        self.grid.stop_button.clicked.connect(self.stop)
        self.grid.record_button.clicked.connect(self.record)

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

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 1280, 720)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        sys.exit(1)
