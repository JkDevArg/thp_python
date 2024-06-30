from setuptools import setup, find_packages

setup(
    name='thp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'thp=thp.cli:main',
        ],
    },
    author='Joaquin Centurion',
    author_email='joaqhoc@gmail.com',
    description='THP CLI tool for network analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JkDevArg/thp_python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
