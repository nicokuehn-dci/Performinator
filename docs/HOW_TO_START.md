# How to Start

This guide provides a step-by-step process to properly install, activate, and start the Performinator app.

## System Dependencies

Before installing Performinator, ensure that your system has the necessary dependencies. Open a terminal and run the following commands:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-dev build-essential pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse qtbase5-dev libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg git curl
```

## Virtual Environment Setup

To keep your Python environment clean and organized, it's recommended to use a virtual environment. Follow these steps to set up a virtual environment for Performinator:

1. Clone the Performinator repository:

    ```bash
    git clone https://github.com/nicokuehn-dci/Performinator.git
    cd Performinator
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv daw_env
    source daw_env/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Configuring PipeWire Audio

Performinator uses PipeWire for low-latency audio processing. Follow these steps to configure PipeWire on your system:

1. Install PipeWire and related packages:

    ```bash
    sudo apt-get install -y pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse
    ```

2. Add your user to the `audio` group to allow real-time audio processing:

    ```bash
    sudo usermod -a -G audio $USER
    ```

3. Configure real-time audio permissions by adding the following lines to `/etc/security/limits.conf`:

    ```bash
    @audio - rtprio 99
    @audio - memlock unlimited
    ```

4. Reboot your system to apply the changes:

    ```bash
    sudo reboot
    ```

## Running Performinator

Once you have completed the setup, you can start Performinator by running the following commands:

```bash
cd Performinator
source daw_env/bin/activate
python3 src/main.py
```

## Troubleshooting Tips and Common Issues

### Issue: User not in 'audio' group

**Solution:** Run the following command and then reboot your system:

```bash
sudo usermod -a -G audio $USER
sudo reboot
```

### Issue: PipeWire is not properly configured

**Solution:** Ensure that PipeWire is installed and running. You can check the status of PipeWire with the following command:

```bash
systemctl --user status pipewire
```

If PipeWire is not running, start it with:

```bash
systemctl --user start pipewire
```

### Issue: Missing dependencies

**Solution:** Ensure that all required dependencies are installed. Refer to the "System Dependencies" section and run the installation commands again.

### Issue: Virtual environment not activated

**Solution:** Ensure that the virtual environment is activated before running Performinator. Use the following command to activate the virtual environment:

```bash
source daw_env/bin/activate
```

### Issue: Python packages not installed

**Solution:** Ensure that all required Python packages are installed. Run the following command to install the packages:

```bash
pip install -r requirements.txt
```

## Additional Resources

For more detailed installation and configuration instructions, please refer to the [Setup Guide](docs/SETUP.md).

For any issues or questions, please open an issue on GitHub or refer to the [Help](docs/HELP.md) section.

Enjoy making music with Performinator!
