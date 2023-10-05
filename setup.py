from setuptools import setup, find_packages

setup(
    name="altern",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Dariush Abbasi",
    author_email="poshtehani@gmail.com",
    description="A Python package to interact with the altern API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/alternbits/altern-python",  
)