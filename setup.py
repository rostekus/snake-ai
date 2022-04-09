from setuptools import find_packages
from setuptools import setup
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + "/requirements.txt"
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(
    name="Snake RL",
    version="1.0.0",
    description="Snake game not only for humans",
    author="Rostyslav Mosorov",
    author_email="rmosorov@icloud.com",
    license="MIT License",
    url="https://github.com/rostekus/snake_game",
    install_requires=install_requires,
    packages=find_packages(where="src", exclude="tests*"),
    package_dir={"": "src"},
)
