import os
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, Dict

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Dict[str, Any]:
    """Reads a YAML file and returns its content as a dictionary.

    Args:
        path_to_yaml (Path): Path-like input to the YAML file.

    Raises:
        ValueError: If YAML file is empty or cannot be read.

    Returns:
        Dict[str, Any]: Content of the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty or cannot be read.")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return content
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the YAML file: {e}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
