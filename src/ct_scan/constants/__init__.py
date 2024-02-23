from pathlib import Path

# Get the directory of the current script
current_dir = Path(__file__).resolve().parent

# Define the paths relative to the current directory
CONFIG_FILE_PATH = current_dir / "config" / "config.yaml"
PARAMS_FILE_PATH = current_dir / "params.yaml"
