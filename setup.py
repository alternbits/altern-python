from setuptools import setup, find_packages

setup(
    name="altern",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Dariush Abbasi",
    author_email="poshtehani@gmail.com",
    description="Altern API Package for python",
    url="https://github.com/alternbits/altern-python",  
)