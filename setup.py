"""
The setup.py file is used to specify the configuration for
packaging and distributing a Python project.
It typically includes metadata about the project, such as its name, version, author,
and description, as well as information about dependencies and entry points for command-line
interfaces.
This file is essential for making the project installable via package managers like pip.
"""

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    Reads the requirements from a given file and returns them as a list of strings.

    Args:
        file_path (str): The path to the requirements file.

    Returns:

        List[str]: A list of requirements.
    """
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            requirements = [
                line.strip()
                for line in lines
                if line.strip() and not line.startswith("-e .")
            ]
    except FileNotFoundError:
        print(
            "requirements.txt file not found. Please ensure it exists in the project directory."
        )
    return requirements


setup(
    name="NetworkScurity",
    version="0.0.1",
    author="Suraj Bhosale",
    author_email="bhosalesuraj2012@",
    packages=find_packages(),
    install_require=get_requirements(),
)
