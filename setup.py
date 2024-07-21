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
        "python-dateutil ~=2.8.2",
        "psutil ~=5.9.5",
        "opencv-python-headless ~=4.10.0",
        # "opencv-python ~=4.10.0",
        "expiringdict ~=1.2.2",
        "camera-stage-mapping",
        "picamerax",
        "piexif ~=1.1.3",
        "typing-extensions",
        "pythonnet ~=3.0.1",
        "xthings",
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
    entry_points={"console_scripts": ["tetalab-serve=tetalab.app:tetalab_serve"]},
)
