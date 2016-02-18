pytest-ipynb
============

Plugin for ``pytest`` to run IPython notebooks as unit tests, relies on `runipy` to interface with the Notebook.

Define unit tests in IPython notebook cells (`see example on
nbviewer <http://nbviewer.ipython.org/github/zonca/pytest-ipynb/blob/master/examples/test_series_plots.ipynb>`_):

.. figure:: https://github.com/zonca/pytest-ipynb/raw/master/img/pytest-ipynb_notebook.png
   :alt: Example notebook

Run ``py.test`` to execute them:

.. figure:: https://github.com/zonca/pytest-ipynb/raw/master/img/pytest-ipynb_output.png
   :alt: Example output

Example
-------

See the ``examples/`` folder or `a preview on
nbviewer <http://nbviewer.ipython.org/github/zonca/pytest-ipynb/blob/master/examples/test_series_plots.ipynb>`_.

Features
--------

-  Discover files named ``test*.ipynb``
-  Run each cell of the notebook as a unit test (just use ``assert``)
-  First line of each cell is the test name, either as docstring,
   comment or function name
-  A cell named ``fixture*`` or ``setup*`` is run before each of the
   following unit tests as a fixture
-  Add `SKIPCI` to a cell description to skip the test on Travis-CI (checks if the `CI` environment variable is defined)
-  IPython notebook kernel is restarted after each test
-  Each notebook is executed in the folder where the ``.ipynb`` file is located

Requirements
------------

-  Python 2.7+, Python 3.2+
-  ``pytest``
-  IPython Notebook 2.0+

Install
-------

::

    $ pip install pytest-ipynb

Author
------

`Andrea Zonca <http://github.com/zonca>`__

Credits
-------

-  `<https://gist.github.com/timo/2621679>`__
- Thomas Kluyver for help on the IPython mailing list
