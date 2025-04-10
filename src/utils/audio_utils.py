import librosa
from pydub import AudioSegment
import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_audio_file(file_path):
    """Load audio file from the local file system"""
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True)
        return y, sr
    except Exception as e:
        logger.error(f"Error loading audio file {file_path}: {e}")
        return None, None

def convert_format(input_path, output_format='wav'):
    """Convert audio files using pydub"""
    try:
        sound = AudioSegment.from_file(input_path)
        output_path = input_path.rsplit('.', 1)[0] + f'.{output_format}'
        sound.export(output_path, format=output_format)
        return output_path
    except Exception as e:
        logger.error(f"Error converting audio file {input_path} to {output_format}: {e}")
        return None

def load_audio_into_memory(file_path):
    """Load audio file into memory using librosa"""
    try:
        audio_data, sr = librosa.load(file_path, sr=None, mono=False)
        return audio_data, sr
    except Exception as e:
        logger.error(f"Error loading audio into memory from {file_path}: {e}")
        return None, None

def time_stretch_audio(audio_data, rate):
    """Time-stretch audio using librosa"""
    try:
        return librosa.effects.time_stretch(audio_data, rate)
    except Exception as e:
        logger.error(f"Error time-stretching audio: {e}")
        return None

def quantize_to_bpm(audio_data, sr, bpm):
    """Quantize audio to the given BPM using librosa"""
    try:
        hop_length = int(60 / bpm * sr)
        return librosa.effects.time_stretch(audio_data, hop_length)
    except Exception as e:
        logger.error(f"Error quantizing audio to BPM {bpm}: {e}")
        return None

def load_loop_file(file_path):
    """Load loop file using librosa"""
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True)
        return y, sr
    except Exception as e:
        logger.error(f"Error loading loop file {file_path}: {e}")
        return None, None

def quantize_loop_to_bpm(audio_data, sr, bpm):
    """Quantize loop to the given BPM using librosa"""
    try:
        hop_length = int(60 / bpm * sr)
        return librosa.effects.time_stretch(audio_data, hop_length)
    except Exception as e:
        logger.error(f"Error quantizing loop to BPM {bpm}: {e}")
        return None

def load_sample(file_path):
    """Load a sample file using librosa"""
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True)
        return y, sr
    except Exception as e:
        logger.error(f"Error loading sample file {file_path}: {e}")
        return None, None

def get_sample(sample_name, samples_dict):
    """Retrieve a sample by its name from the samples dictionary"""
    try:
        return samples_dict.get(sample_name, None)
    except Exception as e:
        logger.error(f"Error retrieving sample {sample_name}: {e}")
        return None

def setup_pipewire():
    """Set up PipeWire for audio processing."""
    try:
        # Check if PipeWire is running
        result = subprocess.run(['systemctl', 'is-active', '--quiet', 'pipewire'], check=False)
        if result.returncode != 0:
            logger.info("Starting PipeWire service...")
            subprocess.run(['systemctl', 'start', 'pipewire'], check=True)

        # Ensure PipeWire is enabled on boot
        subprocess.run(['systemctl', 'enable', 'pipewire'], check=True)
        logger.info("PipeWire setup complete.")
    except Exception as e:
        logger.error(f"Error setting up PipeWire: {e}")
