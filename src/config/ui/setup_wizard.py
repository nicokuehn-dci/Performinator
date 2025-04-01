from PyQt5.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QPushButton, QComboBox, QLabel
from .dialogs.device_config import AudioDeviceDialog
from ..config.settings import AudioMIDISettings
import subprocess
import ctypes
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

class SetupWizard(QWizard):
    def __init__(self):
        super().__init__()
        self.settings = AudioMIDISettings()
        self.setWindowTitle("TuxTrax Initial Setup")
        self.addPage(AudioDevicePage())
        self.addPage(AudioRoutingPage())
        self.addPage(DeviceHotplugPage())
        self.addPage(AIProtocolPage())  # Add AI Protocol selection page
        self.addPage(OptionsPage())  # Add Options page
        self.addPage(ComponentsPage())  # Add Components page

class AudioDevicePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = AudioDeviceDialog()
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)
        
    def save_settings(self):
        self.settings.config['Audio']['buffersize'] = str(self.ui.buffer_spin.value())
        self.settings.save()

class AudioRoutingPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Audio Routing")
        self.setSubTitle("Configure your audio routing using Helvum.")
        
        layout = QVBoxLayout()
        self.helvum_button = QPushButton("Launch Helvum")
        self.helvum_button.clicked.connect(self.launch_helvum)
        layout.addWidget(self.helvum_button)
        self.setLayout(layout)
        
    def launch_helvum(self):
        try:
            subprocess.run(['helvum'], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error launching Helvum: {e}")
        except Exception as e:
            logger.error(f"Unhandled exception: {e}")

class DeviceHotplugPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Device Hotplug")
        self.setSubTitle("Monitor and configure hot-plugged devices.")
        
        layout = QVBoxLayout()
        self.monitor_button = QPushButton("Start Monitoring")
        self.monitor_button.clicked.connect(self.start_monitoring)
        layout.addWidget(self.monitor_button)
        self.setLayout(layout)
        
    def start_monitoring(self):
        try:
            libudev = ctypes.CDLL('libudev.so.1')
            context = libudev.udev_new()
            monitor = libudev.udev_monitor_new_from_netlink(context, b'udev')
            libudev.udev_monitor_filter_add_match_subsystem_devtype(monitor, b'usb', None)
            libudev.udev_monitor_enable_receiving(monitor)
            fd = libudev.udev_monitor_get_fd(monitor)
            
            while True:
                rlist, _, _ = select.select([fd], [], [], 1)
                if fd in rlist:
                    device = libudev.udev_monitor_receive_device(monitor)
                    action = libudev.udev_device_get_action(device)
                    self.device_event(action, device)
        except Exception as e:
            logger.error(f"Unhandled exception: {e}")
        
    def device_event(self, action, device):
        try:
            logger.info(f"Device {action}: {device}")
        except Exception as e:
            logger.error(f"Unhandled exception: {e}")

class AIProtocolPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("AI Protocol Selection")
        self.setSubTitle("Choose your preferred AI protocol for music generation.")
        
        layout = QVBoxLayout()
        self.ai_protocol_combo = QComboBox()
        self.ai_protocol_combo.addItems(['Magenta Studio', 'AIVA', 'ChatGPT-4 Music Plugins'])
        layout.addWidget(QLabel("AI Protocol:"))
        layout.addWidget(self.ai_protocol_combo)
        self.setLayout(layout)
        
    def save_settings(self):
        selected_protocol = self.ai_protocol_combo.currentText()
        self.settings.config['AI']['protocol'] = selected_protocol
        self.settings.save()

class OptionsPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Options")
        self.setSubTitle("Configure your audio, MIDI, and AI protocol settings.")
        
        layout = QVBoxLayout()
        self.audio_settings_button = QPushButton("Audio Settings")
        self.audio_settings_button.clicked.connect(self.audio_settings)
        layout.addWidget(self.audio_settings_button)
        
        self.midi_settings_button = QPushButton("MIDI Settings")
        self.midi_settings_button.clicked.connect(self.midi_settings)
        layout.addWidget(self.midi_settings_button)
        
        self.ai_protocol_settings_button = QPushButton("AI Protocol Settings")
        self.ai_protocol_settings_button.clicked.connect(self.ai_protocol_settings)
        layout.addWidget(self.ai_protocol_settings_button)
        
        self.setLayout(layout)
        
    def audio_settings(self):
        logger.info("Audio Settings action triggered")
        # Implement the logic to handle Audio Settings

    def midi_settings(self):
        logger.info("MIDI Settings action triggered")
        # Implement the logic to handle MIDI Settings

    def ai_protocol_settings(self):
        logger.info("AI Protocol Settings action triggered")
        # Implement the logic to handle AI Protocol Settings

class ComponentsPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Components")
        self.setSubTitle("Manage your components.")
        
        layout = QVBoxLayout()
        self.add_component_button = QPushButton("Add Component")
        self.add_component_button.clicked.connect(self.add_component)
        layout.addWidget(self.add_component_button)
        
        self.remove_component_button = QPushButton("Remove Component")
        self.remove_component_button.clicked.connect(self.remove_component)
        layout.addWidget(self.remove_component_button)
        
        self.manage_components_button = QPushButton("Manage Components")
        self.manage_components_button.clicked.connect(self.manage_components)
        layout.addWidget(self.manage_components_button)
        
        self.setLayout(layout)
        
    def add_component(self):
        logger.info("Add Component action triggered")
        # Implement the logic to handle Add Component

    def remove_component(self):
        logger.info("Remove Component action triggered")
        # Implement the logic to handle Remove Component

    def manage_components(self):
        logger.info("Manage Components action triggered")
        # Implement the logic to handle Manage Components
