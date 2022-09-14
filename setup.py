
  
from setuptools import setup, find_packages

# read the requirements file
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(name="MGN",
      version="1.0",
      description="Mesh Graph Networks",
      author="MGN team",
      author_email="",
      packages=find_packages(),
      package_dir={"MGN": "MGN"},
      install_requires=None,
      extras_require={
            "dev": [],
      },
      requires=required,
      include_package_data=True)