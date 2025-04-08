# Audio System Configuration Guide

## 1. Required Packages
```bash
# KX Studio variant (recommended)
sudo apt-get install cadence carla pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse

# Minimal setup
sudo apt-get install pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse
```

## 2. Configuring MIDI Devices
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

## 3. Configuring Recording Choices
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

## 4. PipeWire Configuration Tweaks

### Low-Latency Audio Setup
Edit `/etc/pipewire/pipewire.conf` (or `~/.config/pipewire/pipewire.conf`):
```ini
# Set quantum (buffer size) for pro-audio use
default.clock.quantum = 64  # For low-latency (adjust based on your hardware)
default.clock.min-quantum = 32
default.clock.max-quantum = 1024

# Prioritize real-time scheduling
context.properties = {
    default.clock.rate = 48000
    default.clock.allowed-rates = [ 44100 48000 96000 ]
    log.level = 2  # Debug logs if needed
}
```

### Persistent Device Routing
Create custom rules in `/etc/pipewire/pipewire-pulse.conf.d/` to:
- Remember device connections
- Set default sample rates
- Prioritize USB audio interfaces over built-in sound cards

## 5. System Tweaks

### RTKit Priority
Ensure PipeWire has real-time privileges:
```bash
sudo systemctl edit rtkit-daemon.service
```
Add:
```ini
[Service]
LimitRTPRIO=33
LimitMEMLOCK=64M
```

### USB Audio Optimization
For USB interfaces (e.g., Focusrite):
```bash
echo 'options snd-usb-audio nrpacks=1' | sudo tee /etc/modprobe.d/audio.conf
sudo apt install linux-lowlatency  # If on Ubuntu
```

## Detailed Setup Instructions

### Step-by-Step Guide

1. **Install Required Packages:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y cadence carla pipewire pipewire-audio-client-libraries libspa-0.2-jack pipewire-pulse
   ```

2. **Configure MIDI Devices:**
   - List available MIDI devices:
     ```bash
     aconnect -i -o
     amidi -l
     ```
   - Connect a MIDI input to a MIDI output:
     ```bash
     aconnect <input_id> <output_id>
     ```

3. **Configure Recording Choices:**
   - List available recording devices:
     ```bash
     arecord -l
     ```
   - Set the recording format and bitrate:
     ```bash
     arecord -D plughw:<card_number>,<device_number> -f <format> -r <bitrate> -d <duration> <output_file>
     ```

4. **Apply PipeWire Configuration Tweaks:**
   - Edit `/etc/pipewire/pipewire.conf` (or `~/.config/pipewire/pipewire.conf`):
     ```ini
     default.clock.quantum = 64
     default.clock.min-quantum = 32
     default.clock.max-quantum = 1024
     context.properties = {
         default.clock.rate = 48000
         default.clock.allowed-rates = [ 44100 48000 96000 ]
         log.level = 2
     }
     ```

5. **Apply System Tweaks:**
   - Ensure PipeWire has real-time privileges:
     ```bash
     sudo systemctl edit rtkit-daemon.service
     ```
     Add:
     ```ini
     [Service]
     LimitRTPRIO=33
     LimitMEMLOCK=64M
     ```
   - Optimize USB audio:
     ```bash
     echo 'options snd-usb-audio nrpacks=1' | sudo tee /etc/modprobe.d/audio.conf
     sudo apt install linux-lowlatency
     ```

## Examples and Screenshots

### Example 1: Configuring MIDI Devices

![Configuring MIDI Devices](images/configuring_midi_devices.png)

### Example 2: Setting Recording Format and Bitrate

![Setting Recording Format and Bitrate](images/setting_recording_format_bitrate.png)

### Example 3: Applying PipeWire Configuration Tweaks

![Applying PipeWire Configuration Tweaks](images/applying_pipewire_tweaks.png)

### Example 4: Applying System Tweaks

![Applying System Tweaks](images/applying_system_tweaks.png)

## Note on Cloud and Online Features

Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.
