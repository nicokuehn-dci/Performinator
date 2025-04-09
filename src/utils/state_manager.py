import json
import pickle
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ProjectManager:
    def save_project(self, path, sampler_state, mixer_state):
        try:
            project_data = {
                'samples': sampler_state.samples,
                'midi_mapping': sampler_state.midi_mapper.mapping,
                'mixer_presets': mixer_state.get_presets()
            }
            
            with open(Path(path) / 'project.tux', 'wb') as f:
                pickle.dump(project_data, f)
        except Exception as e:
            logger.error(f"Error saving project: {e}")
            raise

    def load_project(self, path):
        try:
            with open(Path(path) / 'project.tux', 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            logger.error(f"Error loading project: {e}")
            raise

    def save_state(self, path, state):
        try:
            with open(Path(path) / 'state.json', 'w') as f:
                json.dump(state, f)
        except Exception as e:
            logger.error(f"Error saving state: {e}")
            raise

    def load_state(self, path):
        try:
            with open(Path(path) / 'state.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading state: {e}")
            raise

    def save_pattern(self, path, name, pattern):
        try:
            pattern_path = Path(path) / f'{name}.json'
            with open(pattern_path, 'w') as f:
                json.dump(pattern, f)
        except Exception as e:
            logger.error(f"Error saving pattern {name}: {e}")
            raise

    def load_pattern(self, path, name):
        try:
            pattern_path = Path(path) / f'{name}.json'
            with open(pattern_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading pattern {name}: {e}")
            raise

    def save_project_to_json(self, path, sampler_state, mixer_state):
        try:
            project_data = {
                'samples': sampler_state.samples,
                'midi_mapping': sampler_state.midi_mapper.mapping,
                'mixer_presets': mixer_state.get_presets()
            }
            
            with open(Path(path) / 'project.json', 'w') as f:
                json.dump(project_data, f)
        except Exception as e:
            logger.error(f"Error saving project to JSON: {e}")
            raise

    def load_project_from_json(self, path):
        try:
            with open(Path(path) / 'project.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading project from JSON: {e}")
            raise

    def load_project_data(self, project_name):
        try:
            project_path = Path("projects") / f"{project_name}.json"
            with open(project_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading project data for {project_name}: {e}")
            return None
