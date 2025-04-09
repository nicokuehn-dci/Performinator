import customtkinter as ctk

class ChannelStrip(ctk.CTkFrame):
    def __init__(self, master, channel_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.channel_id = channel_id
        self.configure(border_width=2, corner_radius=8)

        # Channel Label
        self.label = ctk.CTkLabel(self, text=f"Channel {channel_id}", font=("Arial", 14, "bold"))
        self.label.pack(pady=4)

        # Preamp
        self.preamp = ctk.CTkSlider(self, from_=0, to=10)
        self._add_label("Preamp")
        self.preamp.pack()

        # EQ Section
        self._add_label("EQ - Low / Mid / High")
        self.eq_low = ctk.CTkSlider(self, from_=-12, to=12)
        self.eq_mid = ctk.CTkSlider(self, from_=-12, to=12)
        self.eq_high = ctk.CTkSlider(self, from_=-12, to=12)
        self.eq_low.pack()
        self.eq_mid.pack()
        self.eq_high.pack()

        # Compressor
        self._add_label("Compressor")
        self.compressor = ctk.CTkSlider(self, from_=0, to=10)
        self.compressor.pack()

        # VST3 Slot (Placeholder)
        self._add_label("VST3 Slot")
        self.vst_button = ctk.CTkButton(self, text="Load VST3", command=self.load_vst3_plugin)
        self.vst_button.pack(pady=2)

        # Saturation / Tape
        self.sat_var = ctk.BooleanVar()
        self.tape_var = ctk.BooleanVar()
        self.saturation = ctk.CTkCheckBox(self, text="Saturation", variable=self.sat_var)
        self.tape = ctk.CTkCheckBox(self, text="Tape", variable=self.tape_var)
        self.saturation.pack()
        self.tape.pack()

        # Line-In
        self.line_in_var = ctk.BooleanVar()
        self.line_in = ctk.CTkCheckBox(self, text="Line-In", variable=self.line_in_var, command=self.route_line_in)
        self.line_in.pack()

        # Loop Import
        self._add_label("Loop")
        self.loop_button = ctk.CTkButton(self, text="Import Loop")
        self.loop_button.pack(pady=2)

        # Volume & Pan
        self._add_label("Volume")
        self.volume = ctk.CTkSlider(self, from_=0, to=100, command=self.set_volume)
        self.volume.pack()

        self._add_label("Pan")
        self.pan = ctk.CTkSlider(self, from_=-1, to=1, command=self.set_pan)
        self.pan.pack()

    def _add_label(self, text):
        lbl = ctk.CTkLabel(self, text=text)
        lbl.pack(pady=(8, 2))

    def route_line_in(self):
        # Placeholder for routing external line-in
        print(f"Routing external line-in to channel {self.channel_id}")

    def load_vst3_plugin(self):
        # Placeholder for loading VST3 plugin
        print(f"Loading VST3 plugin for channel {self.channel_id}")

    def set_volume(self, value):
        # Placeholder for setting volume
        print(f"Setting volume for channel {self.channel_id} to {value}")

    def set_pan(self, value):
        # Placeholder for setting pan
        print(f"Setting pan for channel {self.channel_id} to {value}")
