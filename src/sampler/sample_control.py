class SampleControl:
    def __init__(self, sample_name):
        self.sample_name = sample_name
        self.pitch = 1.0  # Default pitch
        self.loop = False
        self.playing = False

    def set_pitch(self, value):
        self.pitch = value
        print(f"[SampleControl] Pitch for {self.sample_name} set to {self.pitch}")

    def toggle_loop(self):
        self.loop = not self.loop
        print(f"[SampleControl] Looping for {self.sample_name} set to {self.loop}")

    def play(self):
        self.playing = True
        print(f"[SampleControl] Playing {self.sample_name}")

    def stop(self):
        self.playing = False
        print(f"[SampleControl] Stopped {self.sample_name}")
