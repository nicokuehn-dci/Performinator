import subprocess
import sys
import os
import logging
import pydbus  # For PipeWire metadata
from pyudev import Context, Monitor, MonitorObserver  # For MIDI hotplug
from src.utils.learning_manager import LearningManager

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def setup_virtualenv():
    try:
        logger.info("🔧 Setting up virtual environment...")
        if not os.path.exists("daw_env"):
            subprocess.run([sys.executable, "-m", "venv", "daw_env"], check=True)
        activate_script = "daw_env/bin/activate" if os.name != "nt" else "daw_env\\Scripts\\activate"
        activate_command = f"source {activate_script}" if os.name != "nt" else activate_script
        subprocess.run(activate_command, shell=True, check=True)
        logger.info("Virtual environment activated.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error setting up virtual environment: {e}")
        if e.returncode == 1:
            logger.error("Severe error: Virtual environment setup failed.")
            raise
        else:
            logger.error("Non-severe error: Continuing execution.")

def install_dependencies():
    try:
        logger.info("📦 Installing Python dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        logger.info("Python dependencies installed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error installing Python dependencies: {e}")
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
        bus = pydbus.SystemBus()
        pipewire = bus.get("org.freedesktop.pipewire1")
        # Example: Set metadata (replace with actual implementation)
        pipewire.SetMetadata("example.key", "example.value")
        logger.info("PipeWire metadata setup complete.")
    except Exception as e:
        logger.error(f"Error setting up PipeWire metadata: {e}")
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
        logger.error(f"Error monitoring MIDI hotplug events: {e}")
        raise

def midi_hotplug_callback(action, device):
    """
    Callback for MIDI device hotplug events.
    """
    if action == "add":
        logger.info(f"MIDI device connected: {device.device_node}")
    elif action == "remove":
        logger.info(f"MIDI device disconnected: {device.device_node}")

def launch_electron_app():
    try:
        subprocess.run(["npm", "start"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error launching Performinator: {e}")
        if e.returncode == 1:
            logger.error("Severe error: Performinator launch failed.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")

def main():
    try:
        setup_virtualenv()
        install_dependencies()
        setup_pipewire_metadata()  # Add PipeWire metadata setup
        monitor_midi_hotplug()  # Start MIDI hotplug monitoring
        learning_manager = LearningManager()
        learning_manager.capture_user_input("Setup and dependencies installed")
        launch_electron_app()
        learning_manager.capture_user_output("Performinator launched")
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        if isinstance(e, subprocess.CalledProcessError) and e.returncode == 1:
            logger.error("Severe error: Unhandled exception occurred.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        if isinstance(e, subprocess.CalledProcessError) and e.returncode == 1:
            logger.error("Severe error: Unhandled exception occurred.")
            sys.exit(1)
        else:
            logger.error("Non-severe error: Continuing execution.")
