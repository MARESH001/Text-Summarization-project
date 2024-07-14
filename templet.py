import os
from pathlib import Path
import logging

# Set up logging to show debug messages and errors
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "textSummarizer"

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile.txt",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Process each path in the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Extract directory and filename
    
    logging.debug(f"Processing file: {filepath}")

    if filedir:
        try:
            os.makedirs(filedir, exist_ok=True)  # Create directory if it does not exist
            logging.info(f"Ensured directory exists: {filedir} for the file {filename}")
        except Exception as e:
            logging.error(f"Error creating directory {filedir}: {e}")
            continue  # Skip to the next file in case of an error

    if not filepath.exists() or filepath.stat().st_size == 0:  # Check if file does not exist or is empty
        try:
            with open(filepath, 'w') as f:  # Create an empty file
                pass
            logging.info(f"Created empty file: {filepath}")
        except Exception as e:
            logging.error(f"Error creating file {filepath}: {e}")
    else:
        logging.info(f"File already exists: {filepath}")
