
  
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
      install_requires=required,
      extras_require={
            "dev": [],
      })
