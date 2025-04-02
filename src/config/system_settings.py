import configparser
import json

config = configparser.ConfigParser()

# Default settings
config['Audio'] = {
    'sample_rate': '44100',
    'buffer_size': '512',
    'default_path': '~/samples'
}

config['MIDI'] = {
    'default_port': '0',
    'velocity_curve': 'exponential'
}

config['GUI'] = {
    'theme': 'dark',
    'default_scale': 'C Major'
}

config['AI'] = {
    'magenta_studio_path': '/usr/local/bin/magenta-studio'
}

# Write default settings to file
with open('system_settings.ini', 'w') as configfile:
    config.write(configfile)

def read_settings():
    config.read('system_settings.ini')
    return config

def write_settings(section, option, value):
    config.set(section, option, value)
    with open('system_settings.ini', 'w') as configfile:
        config.write(configfile)

def save_settings_to_json(file_path):
    settings = {section: dict(config.items(section)) for section in config.sections()}
    with open(file_path, 'w') as json_file:
        json.dump(settings, json_file)

def load_settings_from_json(file_path):
    with open(file_path, 'r') as json_file:
        settings = json.load(json_file)
        for section, options in settings.items():
            if section not in config.sections():
                config.add_section(section)
            for option, value in options.items():
                config.set(section, option, value)
        with open('system_settings.ini', 'w') as configfile:
            config.write(configfile)
