from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QComboBox, QListWidget, QSpinBox, QLabel
)
import sounddevice as sd

class AudioDeviceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.devices = sd.query_devices()
        self._init_ui()
        
    def _init_ui(self):
        layout = QVBoxLayout()
        
        self.engine_combo = QComboBox()
        self.engine_combo.addItems(['PipeWire', 'JACK', 'ALSA', 'Pulse'])
        layout.addWidget(QLabel("Audio Engine:"))
        layout.addWidget(self.engine_combo)
        
        self.device_list = QListWidget()
        for dev in self.devices:
            if dev['max_inputs'] > 0:
                self.device_list.addItem(dev['name'])
        layout.addWidget(QLabel("Input Devices:"))
        layout.addWidget(self.device_list)
        
        self.buffer_spin = QSpinBox()
        self.buffer_spin.setRange(64, 4096)
        self.buffer_spin.setValue(256)
        layout.addWidget(QLabel("Buffer Size:"))
        layout.addWidget(self.buffer_spin)
        
        self.ai_protocol_combo = QComboBox()
        self.ai_protocol_combo.addItems(['Magenta Studio'])
        layout.addWidget(QLabel("AI Protocol:"))
        layout.addWidget(self.ai_protocol_combo)
        
        self.setLayout(layout)
