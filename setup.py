import subprocess
import sys
from setuptools import setup, find_packages
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def check_and_install(package):
    """Check if a package is installed, and install it if necessary."""
    try:
        __import__(package)
        logger.info(f"Package '{package}' is already installed.")
    except ImportError:
        logger.info(f"Package '{package}' is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def log_error(message, severity="non-severe"):
    logger.error(message)
    if severity == "severe":
        raise SystemExit(message)

# List of required packages
required_packages = [
    "numpy",
    "PyQt5",
    "pedalboard",
    "librosa",
    "sounddevice",
    "mido",
    "python-rtmidi",
    "pyqtgraph",
    "PyYAML",
    "soundfile",
    "pytest",
    "mutagen",
    "customtkinter",
    "pydbus",
    "pyudev",
    "PyPDF2",
]

# Check and install required packages
for package in required_packages:
    check_and_install(package)

try:
    setup(
        name="Performinator",
        version="0.1.0",
        packages=find_packages(where="src"),
        package_dir={"": "src"},  # Tell setuptools that packages are under the 'src' directory
        install_requires=required_packages,
        extras_require={
            'dev': [
                'pytest>=7.4.4',
                'flake8>=6.0.0',
                'black>=23.0.0',
            ],
            'ai': [
                # AI/ML dependencies in a separate extra to avoid installation issues
                'tensorflow>=2.9.0',  
                'magenta>=1.3.1',
            ],
        },
        entry_points={
            'console_scripts': [
                'performinator=src.main:main',  # Entry point for running the app
            ],
        },
        package_data={
            '': ['*.yaml', '*.json', '*.css', '*.html'],  # Include additional file types
        },
        include_package_data=True,
        python_requires='>=3.10',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author="Nico Kühn",
        author_email="nico.kuehn@dci-student.org",
        description="An Ubuntu-first live performance sampler and mixer",
        keywords="audio, music, sampler, daw, ubuntu, linux",
        url="https://github.com/nicokuehn-dci/Performinator",
        license="MIT",  # SPDX license expression
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: End Users/Desktop",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "License :: SPDX-License-Identifier :: MIT",
            "Operating System :: POSIX :: Linux",
            "Topic :: Multimedia :: Sound/Audio",
            "Topic :: Multimedia :: Sound/Audio :: MIDI",
            "Topic :: Multimedia :: Sound/Audio :: Mixers",
        ],
    )
    logger.info("Setup completed successfully.")
except Exception as e:
    log_error(f"Error during setup: {e}", severity="severe")

# Note on installation
logger.info("To install AI features, use: pip install -e .[ai]")

# Note on Cloud and Online Features
logger.info("Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.")
