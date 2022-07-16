from setuptools import setup

NAME = "Crypttool"
DESCRIPTION = "Encrypt text or file"
URL = "https://github.com/varvaruk-v/Crypt-file"
EMAIL = ""
AUTHOR = "Viktor Varvaruk"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.5.0"

with open("requirements.txt", encoding="utf-8") as f:
    REQUIRED = f.readlines()

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["crypttool"],
    entry_points={
        "console_scripts": ["crypttool=crypttool.cli:main"]
    },
    install_requires=REQUIRED,
    license="MIT",
)