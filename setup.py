from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data
NAME = "fraud-detection-model"
DESCRIPTION = "Fraud detection model deployment project"
EMAIL = "ghktjd15gh@gmail.com"
AUTHOR = "minsoo9506"
REQUIRES_PYTHON = "==3.9.13"

# Load the package's VERSION file as a dictionary
about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'model'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version

# packages required for this module to be executed
def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()

# setup
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=("test",)),
    package_data={"model": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=False,
    license="MIT"
)