import os
from setuptools import setup

def readfile(*names):
    """
Helper utility. Read text from file to help keep setup.py DRY.
    """
    thisfile = os.path.abspath(__file__)
    thisfile = os.path.join(os.path.dirname(thisfile), *names)
    with open(thisfile) as fp:
        return fp.read()

setup(
    name='wordsearch',
    version='0.0.1',
    packages=['wordsearch',],
    author='Scott Keller',
    author_email='scottjameskeller@gmail.com',
    url='https://github.com/scottkeller/wordsearch',
    description="Solves a word search puzzle given a file of words and a word search grid.",
    license='MIT',
    long_description=readfile('README'),
    install_requires=['fire'],
    entry_points={
        'console_scripts': [
            'wordsearch = wordsearch.cli.cli:_main',
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)