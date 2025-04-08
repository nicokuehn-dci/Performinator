# TuxTrax Setup Guide

This guide provides step-by-step instructions for installing TuxTrax on Ubuntu, including system dependencies, virtual environment setup, and configuring PipeWire audio.

## System Dependencies

Before installing TuxTrax, ensure that your system has the necessary dependencies. Open a terminal and run the following commands:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-dev build-essential pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse qtbase5-dev libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg git curl
```

## Virtual Environment Setup

To keep your Python environment clean and organized, it's recommended to use a virtual environment. Follow these steps to set up a virtual environment for TuxTrax:

1. Clone the TuxTrax repository:

    ```bash
    git clone https://github.com/nicokuehn-dci/TuxTrax.git
    cd TuxTrax
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

TuxTrax uses PipeWire for low-latency audio processing. Follow these steps to configure PipeWire on your system:

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

## Configuring MIDI Devices

To configure MIDI devices, you can use `aconnect` and `amidi` tools.

### Listing MIDI Devices
To list available MIDI devices, run:
```bash
aconnect -i -o
amidi -l
```

### Connecting MIDI Devices
To connect a MIDI input to a MIDI output, use:
```bash
aconnect <input_id> <output_id>
```
Replace `<input_id>` and `<output_id>` with the appropriate IDs from the `aconnect -i -o` output.

## Configuring Recording Choices

To configure recording choices such as format and bitrate, you can use `arecord`.

### Listing Recording Devices
To list available recording devices, run:
```bash
arecord -l
```

### Setting Recording Format and Bitrate
To set the recording format and bitrate, use:
```bash
arecord -D plughw:<card_number>,<device_number> -f <format> -r <bitrate> -d <duration> <output_file>
```
Replace `<card_number>`, `<device_number>`, `<format>`, `<bitrate>`, `<duration>`, and `<output_file>` with the appropriate values.

## Running TuxTrax

Once you have completed the setup, you can start TuxTrax by running the following commands:

```bash
cd TuxTrax
source daw_env/bin/activate
python3 src/main.py
```

## Examples and Screenshots

### Example 1: Importing and Slicing Samples

![Importing and Slicing Samples](docs/images/import_slicing_samples.png)

### Example 2: Mixing with Analog-Style Channel Strips

![Mixing with Analog-Style Channel Strips](docs/images/mixing_channel_strips.png)

### Example 3: Using the Pro Effects Rack

![Using the Pro Effects Rack](docs/images/pro_effects_rack.png)

### Example 4: Live Looping

![Live Looping](docs/images/live_looping.png)

### Example 5: AI-Powered Sample Matching

![AI-Powered Sample Matching](docs/images/ai_sample_matching.png)

### Example 6: Spectrogram View

![Spectrogram View](docs/images/spectrogram_view.png)

### Example 7: Phase Correlation Meter

![Phase Correlation Meter](docs/images/phase_correlation_meter.png)

## Note on Cloud and Online Features

Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.

Enjoy making music with TuxTrax!
