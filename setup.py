# Import required function from setuptools
from setuptools import find_packages, setup

# Helper function to get requirements from a requirements file
def get_requirements(path: str):
    return [l.strip() for l in open(path)]

# Package setup configuration
setup(
    name="llama",  # Name of the package
    version="0.0.1",  # Version of the package
    packages=find_packages(),  # Find all packages in the current directory and its subdirectories
    install_requires=get_requirements("requirements.txt"),  # Get required packages from the "requirements.txt" file
)
