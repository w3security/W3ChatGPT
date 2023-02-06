
from setuptools import find_packages
from setuptools import setup

setup(
    name="W3ChatGPT",
    version="1.1.5",
    license="GNU General Public License v2.0",
    author="W3Security",
    author_email="chat@log4j.codes",
    description="W3ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["W3ChatGPT", "GPTserver", "Official"],
    url="https://github.com/w3security/w3Chat",
    install_requires=[
        "openai",
        "tiktoken",
    ],
    # optional dependencies
    extras_require={
        "api": ["flask"],
        "unofficial": [
            "undetected_chromedriver>=3.1.7",
            "selenium>=4.7.2",
            "tls_client>=0.1.7",
            "2captcha-python>=1.1.3",
        ],
    },
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "W3ChatGPT = W3ChatGPT.__main__:main",
            "W3ChatGPTApiGPT = W3ChatGPT.GPTserver:main",
            "OfficialChatGPT = W3ChatGPT.Official:main",
        ],
    },
)

