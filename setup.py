from setuptools import setup, find_packages

with open('requirements.txt') as f:
    DEPENDENCIES = f.readlines()

setup(
    name='pipelines_drfc',
    version='0.0.1',
    packages=find_packages(),
    install_requires=DEPENDENCIES
)
