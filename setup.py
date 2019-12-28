from os import path
import codecs
from setuptools import setup, find_packages

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


setup(
    name='django-ip-geolocation',
    version='0.0.5',
    author='Skander Ben Mahmoud',
    author_email='skander.bmahmoud@gmail.com',
    packages=find_packages(exclude=("tests", "docs")),
    url='https://github.com/rednaks/django-ip-geolocation',
    license='MIT',
    description="Django Framework (Middleware and Decorator) to geolocate visitors using their IP address",
    long_description=read(path.join(path.dirname(__file__), 'README.md')),
    install_requires=[
        'requests>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 1 - Dev',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
