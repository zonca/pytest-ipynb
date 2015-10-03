from setuptools import setup
import os.path

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="pytest-ipynb",
    version="1.0.2",

    packages = ['pytest_ipynb'],
    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'ipynb = pytest_ipynb.plugin',
        ]
    },
    install_requires = ["pytest", "runipy"],

    # metadata for upload to PyPI
    author="Andrea Zonca",
    author_email="code@andreazonca.com",
    description="Use pytest's runner to discover and execute tests as cells of IPython notebooks",
    long_description=long_description,
    license="MIT",
    keywords="pytest test unittest ipython notebook",
    url="http://github.com/zonca/pytest-ipynb",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: C++',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
