#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
import shutil
import argparse
import logging
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import Qt
from src.utils.learning_manager import LearningManager

# Configuration
PYTHON_CMD = "python3" if platform.system() != "Windows" else "python"
REQUIRED_BINARIES = [
    'pw-cli', 'ffmpeg', 'pipewire', 'aconnect', 'amidi', 'arecord',
    'magenta-studio'
]

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def print_header():
    print(r"""
        ____            __                      _             _             
|  _ \ ___ _ __ / _| ___  _ __ _ __ ___ (_)_ __   __ _| |_ ___  _ __ 
| |_) / _ \ '__| |_ / _ \| '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
|  __/  __/ |  |  _| (_) | |  | | | | | | | | | | (_| | || (_) | |   
|_|   \___|_|  |_|  \___/|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_|   
            
           Performinator - AI Music Production Assistant       
    """)

def check_audio_group():
    try:
        groups = subprocess.check_output(['groups']).decode().split()
        return 'audio' in groups
    except subprocess.SubprocessError as e:
        logger.error("Error checking audio group: %s", e, exc_info=True)
        return False

def check_pipewire_version():
    try:
        output = subprocess.check_output(['pipewire', '--version'], stderr=subprocess.STDOUT)
        version_str = output.decode().split()[1]
        version = tuple(map(int, version_str.split('.')))
        return version >= (0, 3, 50)
    except subprocess.SubprocessError as e:
        logger.error("Error checking PipeWire version: %s", e, exc_info=True)
        return False

def check_pipewire_configuration():
    try:
        subprocess.run(['pw-cli', 'info'], check=True)
        logger.info("PipeWire is configured and running.")
        return True
    except subprocess.CalledProcessError as e:
        logger.error("PipeWire configuration failed: %s", e, exc_info=True)
        return False

def check_system_deps():
    missing = []
    for bin in REQUIRED_BINARIES:
        if not shutil.which(bin):
            missing.append(bin)
    return missing

def configure_pipewire():
    try:
        subprocess.run(['pw-cli', 'info'], check=True)
        logger.info("PipeWire is configured and running.")
    except subprocess.CalledProcessError as e:
        logger.error("Error configuring PipeWire: %s", e, exc_info=True)

def configure_pipewire_audio_midi():
    try:
        logger.info("🔧 Configuring PipeWire for audio and MIDI...")
        subprocess.run(['pw-cli', 'info'], check=True)
        subprocess.run(['pw-cli', 'load-module', 'module-alsa-source'], check=True)
        subprocess.run(['pw-cli', 'load-module', 'module-alsa-sink'], check=True)
        subprocess.run(['pw-cli', 'load-module', 'module-jack-source'], check=True)
        subprocess.run(['pw-cli', 'load-module', 'module-jack-sink'], check=True)
        logger.info("PipeWire audio and MIDI configuration complete.")
    except subprocess.CalledProcessError as e:
        logger.error("Error configuring PipeWire for audio and MIDI: %s", e, exc_info=True)

def setup_midi_devices():
    try:
        logger.info("🔧 Setting up MIDI devices...")
        subprocess.run(['aconnect', '-i', '-o'], check=True)
        subprocess.run(['amidi', '-l'], check=True)
    except subprocess.CalledProcessError as e:
        logger.error("Error setting up MIDI devices: %s", e, exc_info=True)

def setup_recording_choices():
    try:
        logger.info("🔧 Setting up recording choices...")
        subprocess.run(['arecord', '-l'], check=True)
        
        while True:
            card_number = input("Enter the card number for recording: ")
            device_number = input("Enter the device number for recording: ")
            format = input("Enter the desired format (e.g., cd, dat): ")
            bitrate = input("Enter the desired bitrate (e.g., 16, 24): ")

            if card_number.isdigit() and device_number.isdigit() and bitrate.isdigit():
                break
            else:
                logger.error("Invalid input. Please enter numeric values for card/device/bitrate.")

        logger.info("Recording configuration: Card %s, Device %s, Format %s, Bitrate %s",
                    card_number, device_number, format, bitrate)
        
        subprocess.run(
            ['arecord', '-D', f'plughw:{card_number},{device_number}', '-f', format, '-r', bitrate, '-d', '10', 'test_recording.wav'],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        logger.error("Error setting up recording choices: %s", e, exc_info=True)

def setup_multitrack_recording():
    logger.info("🔧 Setting up multi-track recording...")
    # Add any necessary configuration or setup for multi-track recording here

def configure_magenta_studio():
    try:
        logger.info("🔧 Configuring Magenta Studio...")
        subprocess.run(['magenta-studio', '--configure'], check=True)
    except subprocess.CalledProcessError as e:
        logger.error("Error configuring Magenta Studio: %s", e, exc_info=True)

def launch_electron_app():
    try:
        logger.info("Launching Performinator Electron app...")
        subprocess.run(["npx", "electron", "."], check=True)
    except subprocess.CalledProcessError as e:
        logger.error("Error launching Performinator: %s", e)
        if e.returncode == 1:
            logger.error("Severe error: Performinator launch failed.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")

def system_check():
    logger.info("🔍 Running system checks...")
    issues = []
    
    if not check_audio_group():
        issues.append("User not in 'audio' group - run:\n  sudo usermod -a -G audio $USER && reboot")
    
    if not check_pipewire_version():
        issues.append("PipeWire >= 0.3.50 required")
    
    if not check_pipewire_configuration():
        issues.append("PipeWire is not properly configured")
    
    if missing := check_system_deps():
        issues.append("Missing binaries: %s\n  sudo apt install pipewire ffmpeg pipewire-pulse aconnect amidi arecord magenta-studio" % ', '.join(missing))
    
    if issues:
        logger.error("\n❌ System configuration issues:")
        for i, issue in enumerate(issues, 1):
            logger.error("%d. %s", i, issue)
        return False
    
    return True

def parse_args():
    parser = argparse.ArgumentParser(description="Launch Performinator with system checks and configuration.")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    return parser.parse_args()

def setup_virtualenv():
    try:
        logger.info("🔧 Setting up virtual environment...")
        if not os.path.exists("daw_env"):
            subprocess.run([PYTHON_CMD, "-m", "venv", "daw_env"], check=True)
        activate_script = "daw_env/bin/activate" if platform.system() != "Windows" else "daw_env\\Scripts\\activate"
        activate_command = f"source {activate_script}" if platform.system() != "Windows" else activate_script
        subprocess.run(activate_command, shell=True, check=True)
        logger.info("Virtual environment activated.")
    except subprocess.CalledProcessError as e:
        logger.error("Error setting up virtual environment: %s", e, exc_info=True)

def install_dependencies():
    try:
        logger.info("📦 Installing Python dependencies...")
        subprocess.run([PYTHON_CMD, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([PYTHON_CMD, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        logger.info("Python dependencies installed.")
    except subprocess.CalledProcessError as e:
        logger.error("Error installing Python dependencies: %s", e, exc_info=True)

# Create a splash screen using PyQt5
def show_splash():
    app = QApplication([])
    splash = QSplashScreen()
    splash.setWindowFlags(Qt.FramelessWindowHint)
    splash.setStyleSheet(
        "background-color: #121212; color: #00ffee; font-size: 24px;"
    )
    splash.showMessage(
        "🐧 Performinator is warming up...",
        Qt.AlignCenter
    )
    splash.show()
    app.processEvents()
    splash.close()

def main():
    args = parse_args()
    
    # Set logging level based on debug flag
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    print_header()
    
    # Run system checks before proceeding
    if not system_check():
        sys.exit(1)

    # Perform configurations after successful system checks
    try:
        setup_virtualenv()
        install_dependencies()
        learning_manager = LearningManager()
        learning_manager.capture_user_input("Setup and dependencies installed")
        configure_pipewire()
        configure_pipewire_audio_midi()
        setup_midi_devices()
        setup_recording_choices()
        setup_multitrack_recording()
        configure_magenta_studio()
        
        # Process text files for AI learning
        text_files = ["path/to/textfile1.txt", "path/to/textfile2.pdf"]
        for text_file in text_files:
            text_content = learning_manager.process_text_file(text_file)
            if text_content:
                learning_manager.learn_from_text(text_content)
        
        # Launch application after all configurations are complete
        launch_electron_app()
        learning_manager.capture_user_output("Performinator launched")
        
    except Exception as e:
        logger.error("\n❌ Setup failed: %s", e, exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    show_splash()
    try:
        launch_electron_app()
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user.")

# Note on Cloud and Online Features
# Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.
