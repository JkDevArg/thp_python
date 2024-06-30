from setuptools import setup, find_packages

setup(
    name='thp',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'thp=thp.cli:main',
        ],
    },
)
