from setuptools import setup, find_packages
from os import path
from io import open
import logicqubit

# sudo pip3 install twine
# python setup.py sdist
# python setup.py bdist_wheel
# twine upload dist/*
# sudo python setup.py install

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='logicqubit',
    version=logicqubit.__version__,
    description='LogicQubit is a simple library for quantum computing simulation, with gpu acceleration.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/clnrp/logicqubit',
    author='Cleoner Pietralonga',
    author_email='cleonerp@gmail.com',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['sympy','cupy'],

)
