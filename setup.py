from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    with open("requirements.txt", "r") as file:
        for line in file:
            requirement_list.append(line.strip())
    return requirement_list

setup(
    name="sensor-fault",
    version="0.0.1",
    author="yashwanth",
    author_email="yashwanthreddy7178@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
    description="sensor fault detection",
    long_description="sensor fault detection",
    long_description_content_type="text/markdown",
)