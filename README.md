pytest-ipynb
============

Plugin for `pytest` to run IPython notebooks as unit tests

Define unit tests in IPython notebook cells ([see example on nbviewer]():

[Example notebook](https://github.com/zonca/pytest-ipynb/raw/master/img/pytest-ipynb_notebook.png)

Run `py.test` to execute them:

[Example output](https://github.com/zonca/pytest-ipynb/raw/master/img/pytest-ipynb_output.png)

## Features

* Discover files named `test*.ipynb`
* Run each cell of the notebook as a unit test (just use `assert`)
* First line of each cell is the test name, either as docstring, comment or function name
* A cell named `fixture*` is run before each of the following unit tests as a fixture
* IPython notebook kernel is restarted after each test

## Requirements

* Python 2.7+, Python 3.2+
* `pytest`
* IPython Notebook 2.0+

## Install

    $ pip install pytest-ipynb

## Author

[Andrea Zonca](http://github.com/zonca)

## Credits

* <https://gist.github.com/timo/2621679>
