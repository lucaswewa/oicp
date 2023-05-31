from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oicp",
    version="0.1.0",
    description="Python module, and Flask-based web API, to run OICP",
    long_description=long_description,
    packages=find_packages(exclude=["contrib", "docs", "tests", "*node_module*"]),
    install_requires=[
        "apispec[validation]",
        "Flask ~=1.1",
        "Pillow ~=9.5.0",
        "numpy ~=1.24.3",
        "scipy ~=1.10.1",
        "python-dateutil ~=2.8.2",
        "psutil ~=5.9.5",
        "markupsafe ~=2.0.1",
        "opencv-python-headless ~=4.7.0.72",
        "sangaboard",
        "expiringdict ~=1.2.2",
        "camera-stage-mapping",
        "picamerax",
        "pyyaml ~=6.0",
        "pytest-cov ~=4.1.0",
        "piexif ~=1.1.3",
        "labthings ~=1.3.2",
        "typing-extensions ~=4.6.2",
        "RPI.GPIO;platform_machine=='armv7l'"
    ],
    extra_require={
        "dev": [
            "sphinx",
            "sphinxcontrib-openapi",
            "sphinx_rtd_theme",
            "pylint",
            "pytest",
            "mypy",
            "types-python-dateutil",
            "types-setuptools",
            "poethepoet",
            "freezegun",
            "lxml",
            "black",
        ]
    },
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "tetalab-serve=tetalab.app:tetalab_serve"
        ]
    }
)