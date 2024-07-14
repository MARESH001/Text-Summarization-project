import setuptools
from pathlib import Path

def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    return long_description

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "MARESH001"
SRC_REPO = "src"
AUTHOR_EMAIL = "nagalakshmi3502@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    long_description=get_long_description(),  # Correctly call the function
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where=SRC_REPO),
    package_dir={"": SRC_REPO},
    python_requires=">=3.6",
)
