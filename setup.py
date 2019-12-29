from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name='django-ip-geolocation',
    version='1.0.0',
    author='Skander Ben Mahmoud',
    author_email='skander.bmahmoud@gmail.com',
    packages=find_packages(exclude=("tests", "docs")),
    url='https://github.com/rednaks/django-ip-geolocation',
    license='MIT',
    description="Django request/response hook (Middleware and Decorator) to geolocate visitors using their IP address",
    long_description_content_type='text/markdown',
    long_description=readme(),
    install_requires=[
        'requests>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
