from pedalboard import Pedalboard, Compressor, Reverb, Gain, Chorus, Delay, Distortion
import logging
from src.mixer.channel_strip import EffectUnit

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

class FXEngine:
    def __init__(self):
        try:
            self.inserts = Pedalboard([
                Compressor(threshold=-20, ratio=4),
                Gain(gain_db=6),
                Distortion(drive_db=20)
            ])
            
            self.sends = Pedalboard([
                Reverb(room_size=0.7, damping=0.5),
                Chorus(),
                Delay()
            ])
            self.effect_unit = EffectUnit()
        except Exception as e:
            logger.error(f"Error initializing FXEngine: {e}")
            raise

    def process_audio(self, audio, sample_rate):
        try:
            processed = self.inserts(audio, sample_rate)
            send_effect = self.sends(processed, sample_rate)
            return processed + send_effect * 0.3  # Dry/Wet mix
        except Exception as e:
            logger.error(f"Error processing audio: {e}")
            return audio

    def toggle_effect(self, channel_id, effect_name, state):
        self.effect_unit.toggle_effect(channel_id, effect_name, state)

    def is_effect_active(self, channel_id, effect_name):
        return self.effect_unit.is_active(channel_id, effect_name)
