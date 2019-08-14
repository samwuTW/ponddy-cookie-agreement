import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='ponddy-cookie-agreement',
    version=os.environ['CIRCLE_TAG'],
    description='The cookie agreement API for logging user agreement',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='Ponddy cookie GDPR',
    url='https://github.com/samwuTW/ponddy-cookie-agreement',
    author='lambdaTW',
    author_email='lambda@lambda.tw',
    license='MIT',
    packages=find_packages(exclude=("tests*",)),
    install_requires=[
        'Django', 'djangorestframework',
    ],
    zip_safe=False
)
