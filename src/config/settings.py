import os
import json

class AudioMIDISettings:
    def __init__(self, sample_rate=44100, buffer_size=512, midi_device="default", magenta_studio_path="", db_path="learning_data.db", pattern_save_path="patterns"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.midi_device = midi_device
        self.magenta_studio_path = os.path.join(script_dir, magenta_studio_path)
        self.db_path = db_path
        self.pattern_save_path = os.path.join(script_dir, pattern_save_path)

    def load_settings(self, settings_dict):
        self.sample_rate = settings_dict.get("sample_rate", self.sample_rate)
        self.buffer_size = settings_dict.get("buffer_size", self.buffer_size)
        self.midi_device = settings_dict.get("midi_device", self.midi_device)
        self.magenta_studio_path = settings_dict.get("magenta_studio_path", self.magenta_studio_path)
        self.db_path = settings_dict.get("db_path", self.db_path)
        self.pattern_save_path = settings_dict.get("pattern_save_path", self.pattern_save_path)

    def save_settings(self):
        return {
            "sample_rate": self.sample_rate,
            "buffer_size": self.buffer_size,
            "midi_device": self.midi_device,
            "magenta_studio_path": self.magenta_studio_path,
            "db_path": self.db_path,
            "pattern_save_path": self.pattern_save_path
        }

    def save_to_json(self, file_path):
        settings = self.save_settings()
        with open(file_path, 'w') as json_file:
            json.dump(settings, json_file)

    def load_from_json(self, file_path):
        with open(file_path, 'r') as json_file:
            settings = json.load(json_file)
            self.load_settings(settings)

# Note on Cloud and Online Features
# Please note that cloud and online features are future features. These features should be kept in the option menu and layout, but if clicked, they should show a message indicating that it is a feature that is coming later.
