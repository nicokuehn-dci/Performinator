import os
import yaml
from pathlib import Path
import json
import logging

def load_config(config_path="config/default.yaml"):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_sample_library_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_path = os.path.join(script_dir, "TuxTrax_Samples")
    config = load_config()
    return [
        default_path,
        *config.get('library_paths', [])
    ]

def create_project_folder(project_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(script_dir, "TuxTrax_Projects")
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)
    return str(project_path)

def save_pattern_to_file(pattern, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(pattern, f)
    except Exception as e:
        logging.error(f"Error saving pattern to file {file_path}: {e}")

def load_pattern_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading pattern from file {file_path}: {e}")
        return None

def get_sample_path(file_path):
    """Get the absolute path of a sample file."""
    try:
        return os.path.abspath(file_path)
    except Exception as e:
        logging.error(f"Error getting sample path for {file_path}: {e}")
        return None

def get_sample_name(file_path):
    """Get the name of a sample file without extension."""
    try:
        return os.path.splitext(os.path.basename(file_path))[0]
    except Exception as e:
        logging.error(f"Error getting sample name for {file_path}: {e}")
        return None
