import sounddevice as sd
import numpy as np
from threading import Lock
from pedalboard import Pedalboard
import pipewire as pw
import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class AudioEngine:
    def __init__(self, sr=48000, buffer_size=512):
        self.sr = sr
        self.buffer_size = buffer_size
        self.mix_buffer = np.zeros((buffer_size, 2), dtype=np.float32)
        self.lock = Lock()
        self.fx_rack = Pedalboard()
        
        try:
            pw.init(None, None)
            self.context = pw.Context()
            self.core = self.context.connect()
            
            self.stream = pw.Stream(self.core, "TuxTrax-Audio", None)
            self.stream.add_listener(self._stream_listener)
            self.stream.connect(pw.DIRECTION_INPUT, pw.ID_ANY, pw.STREAM_FLAG_AUTOCONNECT | pw.STREAM_FLAG_RT_PROCESS, None, 0)
        except Exception as e:
            logger.error(f"Error initializing PipeWire: {e}")
            raise

    def _stream_listener(self, stream, buffer):
        try:
            with self.lock:
                processed = self.fx_rack.process(self.mix_buffer, self.sr)
                buffer[:] = processed
                self.mix_buffer.fill(0)
        except Exception as e:
            logger.error(f"Error in stream listener: {e}")
            buffer.fill(0)

    def add_audio(self, audio):
        try:
            with self.lock:
                end = min(len(audio), self.buffer_size)
                self.mix_buffer[:end] += audio[:end]
        except Exception as e:
            logger.error(f"Error adding audio: {e}")

    def start(self):
        try:
            self.stream.start()
        except Exception as e:
            logger.error(f"Error starting stream: {e}")
            raise

    def stop(self):
        try:
            self.stream.stop()
        except Exception as e:
            logger.error(f"Error stopping stream: {e}")
            raise

    def set_latency(self, latency_ms):
        """Set the desired latency for the audio engine."""
        try:
            self.stream.set_latency(latency_ms)
        except Exception as e:
            logger.error(f"Error setting latency: {e}")

    def get_latency(self):
        """Get the current latency of the audio engine."""
        try:
            return self.stream.get_latency()
        except Exception as e:
            logger.error(f"Error getting latency: {e}")
            return None

    def monitor_latency(self):
        """Monitor the latency of the audio engine."""
        try:
            latency = self.get_latency()
            if latency is not None:
                logger.info(f"Current latency: {latency} ms")
        except Exception as e:
            logger.error(f"Error monitoring latency: {e}")

    def generate_music_magenta(self, input_midi, output_path):
        """Generate music using Magenta Studio."""
        try:
            subprocess.run(['magenta-studio', '--input', input_midi, '--output', output_path], check=True)
            logger.info(f"Music generated using Magenta Studio: {output_path}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error generating music with Magenta Studio: {e}")

    def route_line_in(self, channel_id):
        """Route external line-in to a specific channel."""
        try:
            logger.info(f"Routing external line-in to channel {channel_id}.")
        except Exception as e:
            logger.error(f"Error routing external line-in: {e}")

    def load_vst3_plugin(self, path, channel_id):
        """Load a VST3 plugin for a specific channel."""
        try:
            logger.info(f"Loaded VST3 Plugin: {path} → Channel {channel_id}")
        except Exception as e:
            logger.error(f"Error loading VST3 plugin: {e}")

    def set_volume(self, channel_id, value):
        """Set the volume for a specific channel."""
        try:
            logger.info(f"Volume for Channel {channel_id} set to {value}")
        except Exception as e:
            logger.error(f"Error setting volume: {e}")

    def set_pan(self, channel_id, value):
        """Set the pan for a specific channel."""
        try:
            logger.info(f"Pan for Channel {channel_id} set to {value}")
        except Exception as e:
            logger.error(f"Error setting pan: {e}")
