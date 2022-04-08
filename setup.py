from setuptools import setup
import tdk_cli.__main__ as m

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

VERSION = m.__version__
DESCRIPTION = "Command-line tool for TDK Dictionary, sozluk.gov.tr with rich output."

setup(
    name="tdk-cli",
    version=VERSION,
    url="https://github.com/agmmnn/tdk-cli",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["tdk_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"tdk_cli": ["tdk_cli/*"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["tdk = tdk_cli.__main__:cli"]},
)
