from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A sample test package'

# Setting up
setup(
    name='ft_package',
    version=VERSION,
    author="julemart",
    author_email="julemart@student.42angouleme.fr",
    description=DESCRIPTION,
    license="MIT",
    packages=find_packages(),
    url="https://github.com/julesmar/ft_package"
)