from setuptools import setup, find_packages
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def log_error(message, severity="non-severe"):
    logger.error(message)
    if severity == "severe":
        raise SystemExit(message)

try:
    setup(
        name="Performinator",  # Updated app name
        version="0.1.0",
        packages=find_packages(where="src"),
        package_dir={"": "src"},  # Tell setuptools that packages are under the 'src' directory
        install_requires=[
            # Keep only Python dependencies
            'numpy>=1.26',
            'PyQt5>=5.15',
            'pedalboard>=0.7',
            'librosa>=0.10',
            'sounddevice>=0.4',
            'mido>=1.2',
            'python-rtmidi>=1.5',
            'pyqtgraph>=0.13',
            'PyYAML>=6.0',
            'soundfile>=0.12',
            'pytest>=7.4.4',
            'setuptools>=69.2.0',
            'pyyaml>=6.0.1',
            'pipewire>=0.3.50',
            'alsa>=1.2.4',
            'magenta-studio>=1.0.0',  # Added dependency for Magenta Studio
            'aiva>=1.0.0',  # Added dependency for AIVA
            'chatgpt4-music-plugins>=1.0.0'  # Added dependency for ChatGPT-4 Music Plugins
        ],
        entry_points={
            'console_scripts': [
                'performinator=main:main',  # Updated entry point
            ],
        },
        package_data={
            '': ['*.yaml'],  # Include any .yaml files in the package
        },
        long_description=long_description,
        long_description_content_type='text/markdown',
    )
    logger.info("Setup completed successfully.")
except Exception as e:
    log_error(f"Error during setup: {e}", severity="severe")

# Note on Cloud and Online Features
logger.info("Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.")
