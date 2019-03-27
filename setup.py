import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-italia',
    version='0.1',
    packages=['agid_template',],
    package_data = {'agid_template': ['agid_template/*']},
    include_package_data=True,
    license='BSD License',
    description="AGID Bootstrap Italia template for Django",
    long_description=README,
    url='https://github.com/francesco-filicetti/django-bootstrap-italia',
    author='Francesco Filicetti',
    author_email='francesco.filicetti@unical.it',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=2.0',
    ]
)
