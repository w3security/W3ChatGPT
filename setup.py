from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

setup(
    name="W3ChatGPT",
    version="0.0.31.1",
    license="GNU General Public License v2.0",
    author="W3Security",
    author_email="alerts@log4j.codes",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/w3security/W3ChatGPT",
    install_requires=[
        "requests",
        "tls-client",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
