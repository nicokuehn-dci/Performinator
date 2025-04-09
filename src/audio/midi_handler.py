from PyQt5.QtCore import QObject, pyqtSignal, QThread
import mido
import pipewire as pw
import logging
import rtmidi

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MidiWorker(QObject):
    note_on = pyqtSignal(int, float)  # (note, velocity 0.0-1.0)
    control_change = pyqtSignal(int, float)  # (cc_num, 0.0-1.0)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        try:
            with mido.open_input() as port:
                while self.running:
                    for msg in port.iter_pending():
                        if msg.type == 'note_on':
                            self.note_on.emit(msg.note, msg.velocity/127)
                        elif msg.type == 'control_change':
                            self.control_change.emit(msg.control, msg.value/127)
        except Exception as e:
            logger.error(f"Error in MIDI worker run loop: {e}")

class MidiManager:
    def __init__(self):
        self.thread = QThread()
        self.worker = MidiWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        
        # Initialize PipeWire MIDI
        try:
            pw.init(None, None)
            self.context = pw.Context()
            self.core = self.context.connect()
            self.midi_stream = pw.MidiStream(self.core, "TuxTrax-MIDI", pw.MIDI_DIRECTION_INPUT | pw.MIDI_DIRECTION_OUTPUT, None)
            self.midi_stream.connect(pw.ID_ANY, 0)
        except Exception as e:
            logger.error(f"Error initializing PipeWire MIDI: {e}")

    def start(self):
        self.thread.start()
    
    def stop(self):
        self.worker.running = False
        self.thread.quit()

    def setup_virtual_midi_patchbay(self):
        try:
            subprocess.run(['pw-link', 'TuxTrax:MIDI Out', 'fluidsynth:MIDI In'], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error setting up virtual MIDI patchbay: {e}")

    def monitor_latency(self):
        try:
            subprocess.run(['pw-top'], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error monitoring latency: {e}")

    def test_latency(self):
        try:
            subprocess.run(['audacity', '--pipewire-latency-test'], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error testing latency: {e}")

class MidiController:
    def __init__(self):
        self.midi_in = rtmidi.MidiIn()
        self.midi_out = rtmidi.MidiOut()

    def open_port(self, port=0):
        self.midi_in.open_port(port)
        self.midi_out.open_port(port)

    def listen_for_cc(self):
        while True:
            message = self.midi_in.get_message()
            if message:
                status, data = message
                if status == 176:  # CC event
                    cc_num = data[0]
                    value = data[1]
                    self.handle_cc(cc_num, value)

    def handle_cc(self, cc_num, value):
        # Mapping CC to Performinator parameters
        print(f"CC {cc_num} received with value {value}")
        if cc_num == 1:  # Example: Volume Control
            self.set_volume(value)
        elif cc_num == 2:  # Example: Pitch Control
            self.set_pitch(value)
        # Weitere CCs für andere Parameter wie Effekte oder Filter hinzufügen

    def set_volume(self, value):
        # Volume-Anpassung in Performinator
        pass

    def set_pitch(self, value):
        # Pitch-Anpassung in Performinator
        pass
