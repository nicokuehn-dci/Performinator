#!/bin/bash

set -e  # Exit immediately on error
set -u  # Treat unset variables as errors

APP_NAME="Performinator"
PYTHON_VERSION="3.12"
VENV_NAME="daw_env"

echo "🐧 Installing Performinator: Unleash Your Inner Penguin DJ"
echo "========================================================"

echo "🔧 Updating system..."
sudo apt update && sudo apt upgrade -y

echo "📦 Installing required system packages..."
sudo apt install -y python$PYTHON_VERSION python$PYTHON_VERSION-venv python$PYTHON_VERSION-dev \
                     build-essential pipewire pipewire-audio-client-libraries libspa-0.2-jack \
                     pipewire-pulse qtbase5-dev libasound2-dev portaudio19-dev libportaudio2 \
                     libportaudiocpp0 ffmpeg git curl \
                     nodejs npm \
                     libpulse-dev libjack-jackd2-dev \
                     libudev-dev # Required for MIDI hotplug monitoring

# Skipping installation of brake system packages as they are not available in the default repositories
# sudo apt install -y libbrake-dev brake-tools brake-utils

echo "⚠️ Skipping brake system packages installation. These packages are not available in the default repositories."

# Set up PipeWire audio permissions
echo "🔊 Configuring PipeWire for real-time performance..."
if ! grep -q "@audio - rtprio 99" /etc/security/limits.conf; then
    echo "@audio - rtprio 99" | sudo tee -a /etc/security/limits.conf
    echo "@audio - memlock unlimited" | sudo tee -a /etc/security/limits.conf
    sudo usermod -a -G audio $USER
    echo "⚠️ Please log out and log back in to apply PipeWire audio group settings."
fi

# Create and activate virtual environment
echo "🐍 Setting up Python $PYTHON_VERSION virtual environment..."
if [ ! -d "$VENV_NAME" ]; then
    python$PYTHON_VERSION -m venv $VENV_NAME
fi
source $VENV_NAME/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Node.js dependencies
echo "🟢 Installing Node.js dependencies..."
npm install

# Install custom tkinter for the GUI
echo "🖌️ Installing CustomTkinter..."
pip install customtkinter

# Install additional dependencies that might be missing
echo "➕ Installing additional dependencies..."
pip install PyPDF2 pydbus pyudev

# Set up brake system configuration
echo "🛑 Configuring brake system..."
sudo mkdir -p /etc/performinator/brake
sudo cp -r config/brake/* /etc/performinator/brake/ 2>/dev/null || echo "No brake configs to copy"

# Create folders required for the app
mkdir -p projects samples

echo "✅ Installation complete!"
echo ""
echo "🚀 To run Performinator:"
echo "----------------------------------------"
echo "cd $APP_NAME"
echo "source $VENV_NAME/bin/activate"
echo "python3 main.py"
echo "----------------------------------------"
