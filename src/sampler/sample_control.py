class SampleControl:
    def __init__(self, sample_name):
        self.sample_name = sample_name
        self.is_playing = False
        self.is_looping = False
        self.pitch = 1.0

    def play(self):
        self.is_playing = True
        print(f"Playing sample: {self.sample_name}")

    def stop(self):
        self.is_playing = False
        print(f"Stopped sample: {self.sample_name}")

    def toggle_loop(self):
        self.is_looping = not self.is_looping
        print(f"Looping {'enabled' if self.is_looping else 'disabled'} for sample: {self.sample_name}")

    def set_pitch(self, pitch):
        self.pitch = pitch
        print(f"Set pitch to {self.pitch} for sample: {self.sample_name}")
