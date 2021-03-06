from distutils.core import setup
import os
from setuptools import find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    name='cursy',
    # Packages to include into the distribution
    packages=find_packages('.'),
    # Start with a small number and increase it with
    # every change you make https://semver.org
    version='1.0.1',
    # Chose a license from here: https: //
    # help.github.com / articles / licensing - a -
    # repository. For example: MIT
    license='MIT',
    # Short description of your library
    description='Little and simple wrapper for curses application.',
    # Long description of your library
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name
    author='voilalex',
    # Your email
    author_email='ilya.vouk@gmail.com',
    # Either the link to your github or to your website
    url='https://github.com/VoIlAlex/cursy',
    # Link from which the project can be downloaded
    download_url='https://github.com/VoIlAlex/archive/v1.0.1.tar.gz',
    # List of keywords
    keywords=[
        'wrapper', 'console', 'curses', 'utility'
    ],
    # List of packages to install with this one
    install_requires=[],
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
