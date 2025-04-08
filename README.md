# Performinator: Unleash Your Inner Penguin DJ

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Ubuntu-First](https://img.shields.io/badge/Platform-Linux%20(Ubuntu)-brightgreen)
![Python](https://img.shields.io/badge/Language-Python-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-orange)

## Jam Like a Penguin: The Ubuntu-First Live Performance Sampler & Mixer

**Performinator** is a powerful, open-source live performance sampler and mixer, built from the ground up for Ubuntu and the vibrant Linux audio community. Embrace the spirit of Tux, the Linux penguin, and unleash your creativity with this powerful and versatile tool. Whether you're a seasoned DJ or just starting your musical journey, Performinator combines intuitive sampling, mixing, and performance features with cutting-edge AI-powered tools, providing everything you need to create captivating live soundscapes.

## Core Features - Assembled By Penguins

*   **Sampler Section:** Effortlessly import, slice, and manipulate samples with MIDI mapping for full expressive control.
*   **Mixer Section:** Craft polished mixes with analog-style channel strips, a pro-grade effects rack, and dynamic sidechain compression.
*   **Ubuntu-First Focus:** Experience exceptional low-latency performance thanks to our PipeWire integration.
*   **Hybrid GUI:** Leverage the power of Electron for a modern, responsive user interface.

## Feature Highlights: From Ice Floe to Stage

### Sampler Section: Your Palette of Sound

*   **Multi-Sample Import:** Drag and drop WAV, MP3, and FLAC files, then automatically slice loops for rhythmic perfection.
*   **Smart Pitch/Time:** Manipulate tempo and pitch with ease. The Paulstretch algorithm delivers pristine time-stretching, while auto-tune helps lock your samples into perfect harmony.
*   **Sampler Modes:** Explore a range of modes:
    *   **One-Shot:** Perfect for percussive hits and short samples.
    *   **ADSR Envelopes:** Sculpt the dynamics of your sounds.
    *   **Loop Modes:** Create evolving textures and soundscapes.
*   **MIDI Mapping:** Assign samples to notes or pads for expressive play with drum pads and melodic instruments.
*   **Swing Function:** Apply swing to all channels or individual channels, with options for old-school Akai sampler and new-school styles.

### Mixer Section: Sculpt Your Sonic Landscape

*   **Analog-Style Channel Strips:** Tweak levels, pan, and EQ on each channel for a polished, balanced mix. Choose from a variety of EQ styles to impart character and shape to your tracks.
*   **Pro Effects Rack:** Elevate your mixes with high-quality effects:
    *   **Inserts:** Inject warmth and character with the Tube Saturator, capture vintage vibes with Tape Emulation, or add digital grit with the Bitcrusher.
    *   **Sends:** Generate immersive sonic spaces with Convolution Reverb, build hypnotic rhythms with Analog Delay, or add swirling movement with Phaser, Chorus, Flanger, and Stutter effects.
*   **Sidechain Compression:** Add rhythmic pumping to your mix by ducking channels with kick drums or basslines.

## Pro Features: Evolve Your Sound

### AI-Powered Workflow: The Future of Sound

*   **Auto-Tag Samples:** Spend less time organizing and more time creating, thanks to ML-driven tagging for genre, instrument type, key, and BPM.
*   **Smart Sample Matching:** Uncover hidden sonic gems by finding harmonically compatible samples.
*   **AI Mastering:** Achieve a professional, polished sound with one-click EQ, limiter, and stereo widening.
*   **Style Transfer:** Transform your audio between genres. Want to turn a rock riff into a DnB banger? Performinator has you covered! (Experimental feature)

### Sample Library Integration: Dive Into Your Sound Collection

*   **Deep Library Scanning:** Automatically index your Splice, Loopmasters, or other sample folders.
*   **Cloud Sync:** Performinator can synchronize your sample library with cloud storage. Currently, it supports folder synchronization with Google Drive, Dropbox, Splice, and Noiiz. Direct API integration is planned for future releases. File conflicts are resolved by keeping the most recently modified version.
*   **Auto-Fill Channels:** Spark inspiration with:
    *   **Style-Based Channel Population:** Quickly create complete kits based on genre (e.g., "Hip-Hop Kit").
    *   **"Surprise Me" Randomization:** Embrace the unexpected and discover new sounds.

### MIDI & Sequencing: Sequence Your Way

*   **MIDI Style Library:** Jumpstart your creativity with:
    *   **Genre Templates:** Load pre-made templates for House, Trap, Techno, Lo-fi, and more.
    *   **Humanization:** Inject groove and swing into your MIDI sequences with realistic humanization templates.
*   **MIDI Drag & Drop:** Seamlessly export MIDI clips to your favorite DAWs or hardware for further refinement.
*   **MIDI Learn:** Take hands-on control by mapping hardware knobs and faders to Performinator parameters.

### Modulation & Automation: Bring Your Sounds to Life

*   **LFO Tool:** Add dynamic movement by modulating FX parameters like filter cutoff or tremolo depth.
*   **Automation Lanes:** Precisely control volume, pan, and FX parameters over time with custom-drawn automation curves.

### Hardware Integration: Bridge the Digital and Analog Worlds

*   **Eurorack Sync:** Integrate with modular synthesizers using CV/Gate support via `python-osc`.
*   **DAW Controller Support:** Enjoy tactile control with popular controllers like Akai APC and Ableton Push.

### Collaboration: Create Together

*   **Cloud Projects:** Collaborate with other penguins by syncing your projects with Google Drive or Dropbox, complete with versioning.
*   **Live Collaboration (Experimental):** Jam with musicians in real-time with our WebSockets + Firebase-powered live editing feature.

### Visual Feedback: See the Sound

*   **Spectrogram View:** Analyze the frequency content of your audio with real-time spectrogram visualization powered by `pyqtgraph`.
*   **Phase Correlation Meter:** Prevent mono compatibility issues with real-time phase monitoring.

## Unique Selling Points: Why Choose Performinator?

*   **Vintage Mode:** Add the warmth and character of classic analog gear with tape hiss and vinyl crackle emulation.
*   **Modular FX Grid:** Design your own custom effects chains with drag-and-drop routing (inspired by Bitwig).
*   **Live Looping:** Overdub and layer sounds in real-time with our intuitive live looping functionality (inspired by Boss RC-505).
*   **Ubuntu-First:** Optimized for low-latency performance and a smooth user experience on Linux. **This isn't just cross-platform, it's built for Linux first.**

## Tech Stack: Under the Hood

Performinator is built on a foundation of powerful, open-source technologies:

*   **Python Libraries:**
    *   **Audio Engine:** `pedalboard`, `sounddevice`, `pydub`
    *   **AI/ML:** `librosa`, `tensorflow-lite`
    *   **GUI:** `Electron`, `Node.js`
    *   **Cloud:** `boto3`, `firebase-admin`, `websockets`
    *   **MIDI/CV:** `mido`, `python-rtmidi`, `python-osc`
*   **Performance Optimizations:**
    *   **Real-Time Audio:** PipeWire
    *   **C Extensions:** `cython`/`numba` for blazing-fast DSP.
    *   **Multicore Processing:** Harness the power of modern CPUs with `ray`/`multiprocessing`.

## Getting Started: Let's Make Some Noise!

1.  **Clone the repository:**

    ```
    git clone git@github.com:nicokuehn-dci/Performinator.git
    cd Performinator
    ```

2.  **Dive into the [Setup Guide](docs/SETUP.md) for detailed installation and configuration instructions.**

## Contributing: Join the Penguin Party

We welcome contributions from the open-source community! Whether you're a seasoned developer, a talented sound designer, or just eager to help, there's a place for you in the Performinator community. Check out our [Contribution Guidelines](CONTRIBUTING.md) for more information.

## License: Open Source, Open Minds

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support: We're Here to Help

Encounter a bug? Have a feature request? Let us know by opening an issue on GitHub!

## Roadmap: The Future of Performinator

*   [ ] **Implement Style Transfer:** Expand our AI-powered style transfer capabilities.
*   [ ] **Expand the MIDI Style Library:** Provide even more genre-specific MIDI templates.
*   [ ] **Improve Cloud Collaboration Features:** Make real-time jamming even more seamless.
*   [ ] **Native Plugin Support**: Host VST/AU plugins within Performinator.

## Experimental Features Development Lifecycle

To provide clarity on the development status of experimental features, we have implemented a development lifecycle with the following stages:

* **Alpha:** Initial implementation, may have significant bugs and incomplete functionality.
* **Beta:** Feature is more stable but may still have some issues and missing features.
* **Stable:** Feature is considered complete and stable for general use.

### Experimental Features Status

* **Style Transfer (Beta):** Currently supports basic style transfer between a limited set of genres. Known limitations: May produce artifacts in some cases. Expected to reach stable in Q4 2024.

## Show Your Support: Give a Penguin a Fish

If you find Performinator useful, please give this project a ⭐ to show your support! And don't forget to share your creations with the world!

## Connect with the Community:

*   [ ] Discord: (Add a link to a Discord server if you have one)
*   [ ] Forum: (Add a link to a forum or discussion board)


Structure of Performinator Project

## Project Structure

```bash
Performinator/
├── .gitignore
├── requirements.txt
├── setup.py
├── README.md
├── samples/
├── docs/
├── tests/
│
├── src/
│   ├── main.py
│   ├── config/
│   │   ├── default.yaml
│   │   └── keybindings.py
│   │
│   ├── sampler/
│   │   ├── engine.py
│   │   ├── waveform_editor.py
│   │   └── midi_mapper.py
│   │
│   ├── mixer/
│   │   ├── channel_strip.py
│   │   ├── fx_rack.py
│   │   └── sidechain.py
│   │
│   ├── gui/
│   │   ├── elektron_menu.py
│   │   ├── performance_grid.py
│   │   └── styles.qss
│   │
│   └── utils/
│       ├── audio_utils.py
│       └── midi_utils.py
│
└── .vscode/
    ├── settings.json
    └── extensions.json



Installation (Ubuntu/Linux)

# Clone repository
git clone https://github.com/nicokuehn-dci/Performinator.git
cd Performinator

# Install system dependencies
sudo apt-get install -y python3-tk ffmpeg pipewire libportaudio2

# Create virtual environment
python3 -m venv daw_env
source daw_env/bin/activate

# Install Python packages
pip install -r requirements.txt

# Configure PipeWire audio (reboot after)
sudo usermod -a -G audio $USER
echo "@audio - rtprio 99" | sudo tee -a /etc/security/limits.conf

## Contribution Guidelines

We welcome contributions from the open-source community! Whether you're a seasoned developer, a talented sound designer, or just eager to help, there's a place for you in the Performinator community. Here are some ways you can contribute:

1. **Report Bugs:** If you encounter any issues while using Performinator, please report them by opening an issue on GitHub. Be sure to include detailed information about the problem and steps to reproduce it.

2. **Request Features:** Have an idea for a new feature? We'd love to hear it! Open an issue on GitHub to share your suggestion.

3. **Submit Pull Requests:** If you'd like to contribute code, follow these steps:
    - Fork the repository
    - Create a new branch for your feature or bugfix
    - Make your changes
    - Submit a pull request with a clear description of your changes

4. **Improve Documentation:** Help us keep our documentation up-to-date and comprehensive. If you find any gaps or errors, please submit a pull request with your improvements.

5. **Join the Discussion:** Engage with the community by participating in discussions on GitHub, Discord, or our forum. Your feedback and ideas are invaluable to the project's growth.

## Detailed Setup Guide

For detailed installation and configuration instructions, please refer to the [Setup Guide](docs/SETUP.md). This guide includes step-by-step instructions for installing Performinator on Ubuntu, including system dependencies, virtual environment setup, and configuring PipeWire audio.

## New Features

### Audio Loops and Auto Quantize to BPM

Performinator now includes handling for audio loops and auto quantize to BPM. This allows you to seamlessly integrate loops into your projects and ensure they are perfectly in sync with your desired tempo.

### Time-Stretching

With the new time-stretching feature, you can adjust the tempo of your audio samples without affecting their pitch. This is particularly useful for creating remixes or matching the tempo of different samples.

### High-Quality Output

Performinator now offers high-quality output options, ensuring your final mix sounds professional and polished. This includes advanced processing techniques to enhance the overall sound quality.

### MIDI Auto Quantize

The MIDI auto quantize feature allows you to automatically align your MIDI notes to the nearest beat, ensuring tight and precise timing in your performances.

### Updated Documentation

The documentation has been updated to reflect these new features. Be sure to check out the [Quickstart Guide](docs/quickstart.md) for more information on how to use these new capabilities.

## Project Purpose

Performinator is designed to provide a powerful and versatile tool for live performance sampling and mixing, with a focus on the Ubuntu and Linux audio community. It aims to combine intuitive sampling, mixing, and performance features with cutting-edge AI-powered tools, enabling users to create captivating live soundscapes.

## Setup Steps

1. **Clone the repository:**

    ```
    git clone git@github.com:nicokuehn-dci/Performinator.git
    cd Performinator
    ```

2. **Install system dependencies:**

    ```
    sudo apt-get install -y python3-tk ffmpeg pipewire libportaudio2
    ```

3. **Create a virtual environment:**

    ```
    python3 -m venv daw_env
    source daw_env/bin/activate
    ```

4. **Install Python packages:**

    ```
    pip install -r requirements.txt
    ```

5. **Configure PipeWire audio (reboot after):**

    ```
    sudo usermod -a -G audio $USER
    echo "@audio - rtprio 99" | sudo tee -a /etc/security/limits.conf
    ```

## Dependencies

Performinator relies on the following dependencies:

*   **Python Libraries:**
    *   **Audio Engine:** `pedalboard`, `sounddevice`, `pydub`
    *   **AI/ML:** `librosa`, `tensorflow-lite`
    *   **GUI:** `Electron`, `Node.js`
    *   **Cloud:** `boto3`, `firebase-admin`, `websockets`
    *   **MIDI/CV:** `mido`, `python-rtmidi`, `python-osc`
*   **System Dependencies:**
    *   **PipeWire:** For real-time audio processing
    *   **FFmpeg:** For audio and video processing
    *   **PortAudio:** For cross-platform audio input/output

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

## Hybrid Approach with Electron and Python

Performinator leverages a hybrid approach, combining the power of Electron for the GUI and regular Python code for other functionalities. This allows us to create a modern, responsive user interface while maintaining the flexibility and performance of Python for audio processing, MIDI handling, and other core features.

### Why Electron?

* **Cross-Platform:** Electron allows us to build a single codebase that runs on multiple platforms, including Linux, Windows, and macOS.
* **Modern UI:** With Electron, we can create a sleek, modern user interface using web technologies like HTML, CSS, and JavaScript.
* **Community Support:** Electron has a large and active community, providing a wealth of resources, plugins, and tools to enhance development.

### How It Works

* **Electron for GUI:** The user interface is built using Electron, leveraging web technologies for a responsive and visually appealing experience.
* **Python for Core Functionality:** Audio processing, MIDI handling, and other core functionalities are implemented in Python, ensuring high performance and flexibility.
* **Communication:** Electron and Python communicate through a combination of IPC (Inter-Process Communication) and WebSockets, enabling seamless integration between the frontend and backend.

### Benefits

* **Separation of Concerns:** By separating the GUI and core functionalities, we can develop and maintain each component independently, improving code quality and maintainability.
* **Performance:** Python's performance and extensive library support make it ideal for audio processing and other computationally intensive tasks.
* **Flexibility:** The hybrid approach allows us to leverage the strengths of both Electron and Python, creating a powerful and versatile application.

### New Methods for Generating, Filtering, and Recombining MIDI Drum Patterns

Performinator now includes new methods for generating, filtering, and recombining MIDI drum patterns using Python scripts. These methods are designed to enhance your creative workflow and provide more flexibility in creating unique drum patterns.

#### Generating Original MIDI Drum Patterns

You can generate original MIDI drum patterns using the `generate_drum_pattern` method. This method creates a 16-step pattern with kick, snare, and hi-hat components.

#### Filtering Patterns into Categories

The `filter_patterns` method allows you to filter patterns into categories, such as "hip-hop grooves" or "techno kicks". This helps you organize your patterns and quickly find the ones that fit your project.

#### Recombining Elements Using Markov Chains

The `recombine_patterns` method uses Markov chains to mix elements from your own library, creating new and unique drum patterns. This method provides endless possibilities for creative recombination of your existing patterns.

### AI-Assisted Generation

#### Tools:

* **Magenta Studio:** Open-source AI music tools
* **AIVA:** AI composition assistant
* **ChatGPT-4 Music Plugins:** e.g., Melobytes

#### Automated MIDI Generation Tools

| Tool           | Features                                                      |
|----------------|---------------------------------------------------------------|
| DrumGizmo      | Open-source drum sampler with MIDI pattern randomization       |
| Hydrogen       | Pattern-based drum machine with MIDI export                   |
| ZynAddSubFX    | Synthesizer with algorithmic MIDI generation                  |

#### Instructions for Using Magenta Studio, AIVA, and ChatGPT-4 Music Plugins

1. **Magenta Studio:**
    - Install Magenta Studio using the provided setup script.
    - Configure Magenta Studio by running `magenta-studio --configure`.
    - Use the `generate_music_magenta` method in the audio engine to generate music.

2. **AIVA:**
    - Install AIVA using the provided setup script.
    - Configure AIVA by running `aiva --configure`.
    - Use the `generate_music_aiva` method in the audio engine to generate music.

3. **ChatGPT-4 Music Plugins:**
    - Install ChatGPT-4 Music Plugins using the provided setup script.
    - Configure ChatGPT-4 Music Plugins by running `chatgpt4-music-plugins --configure`.
    - Use the `generate_music_chatgpt4` method in the audio engine to generate music.

## Learning Capabilities: Continuous Improvement

Performinator now includes learning capabilities that allow the software to learn from every user input and output, making it more stable and intelligent over time. This is achieved through the integration of the `LearningManager` class, which captures user interactions and updates the model accordingly.

### How It Works

* **Capture User Inputs:** The `LearningManager` captures user inputs, such as actions taken within the software.
* **Capture User Outputs:** The `LearningManager` also captures user outputs, such as the results of actions taken.
* **Update Model:** Based on the captured inputs and outputs, the `LearningManager` updates the model to improve the software's performance and stability.

### Benefits

* **Continuous Learning:** The software continuously learns from user interactions, becoming more intelligent and stable over time.
* **Personalized Experience:** As the software learns from your interactions, it can provide a more personalized and optimized experience.

### Example

For example, if you frequently use certain effects or settings, the software can learn to prioritize those options, making your workflow more efficient.

### Getting Started with Learning Capabilities

To start using the learning capabilities, simply use Performinator as you normally would. The `LearningManager` will automatically capture your interactions and update the model in the background.

### Future Enhancements

We plan to further enhance the learning capabilities by incorporating more advanced machine learning algorithms and expanding the range of interactions that the software can learn from.

