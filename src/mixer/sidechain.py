from pedalboard import Compressor, Gain
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class SidechainEngine:
    def __init__(self):
        self.threshold = -24
        self.ratio = 4.0
        self.attack = 10.0
        self.release = 100.0
        self.comp = Compressor(
            threshold_db=self.threshold,
            ratio=self.ratio,
            attack_ms=self.attack,
            release_ms=self.release
        )
        self.makeup_gain = Gain(gain_db=6)

    def process(self, main_audio, trigger_audio, sr):
        try:
            # Convert trigger audio to envelope
            envelope = np.abs(trigger_audio)
            envelope = np.convolve(envelope, np.ones(1024)/1024, mode='same')
            
            # Apply compression based on envelope
            compressed = self.comp(main_audio, sr)
            return self.makeup_gain(compressed * envelope, sr)
        except Exception as e:
            logger.error(f"Error in sidechain processing: {e}")
            return main_audio
