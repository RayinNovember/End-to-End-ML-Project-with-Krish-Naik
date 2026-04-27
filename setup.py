from setuptools import find_packages, setup

setup(
    name = 'krishmlproject',
    version = '0.0.1',
    author = 'Krish',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt') #['pandas','numpy','seaborn'],
)