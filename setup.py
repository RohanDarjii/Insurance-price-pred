from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE = 'requirements.txt'
HYPEN_E_DOT = '-e .'

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE) as f:
        requirements_list = f.readlines()
        requirements_list = [i.replace("\n","") for i in requirements_list]

    if HYPEN_E_DOT in requirements_list:
        requirements_list.remove(HYPEN_E_DOT)
    return requirements_list



setup(
    name="Insurance",
    version="0.0.1",
    author="Rohan Darji",
    author_email="rohan.darji@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),
)