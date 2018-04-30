========================
Fuel Capacity Calculator
========================

This software will calculate the most economic routes for an aircraft as per the fuel consumption. Please note that
the pdf document has a more comprehensive How to Use? information.

This project was created in a Python 3.6 environment. It will be easier to set up the project if you install [Anaconda](https://conda.io/docs/user-guide/install/download.html) or [Miniconda](https://conda.io/miniconda.html). Other options, such as [PyEnv](https://github.com/pyenv/pyenv) and classic virtual environment (i.e. `venv`), will also work.

* Free software: MIT license
* Documentation: https://FC2.readthedocs.io.


Features
--------

* Generation of Adjacency Matrix of Airports with distances using Linked list
* Calculating and evaluating a round trip shortes route
* Calculating most economic route
* Printing the Locations graph
* Generating evaluated cost
* Handling user input errors

Prerequisites
--------------

1. Python3.6 Preferably Anaconda
2. Conda environment with Python 3.6

Installation
-------------

1. Create a Python environment::

    >> $ conda create -n myenv Python=3.6

2. Install the project [Note: all the dependencies will be installed]::

    >> $ pip install git+https://github.com/harshrpg/FC2

OR

1. Clone this repository::

    >> $ git clone https://github.com/harshrpg/FC2
    
2. Move in the Repository folder. Make sure you have the file ``setup.py``::

    >> cd FC2 

3. Create environment from the provided environment file::

    >> conda env create -f=environment.yml

4. Install the project::

    >> pip install -e .

Execution
----------
1. Run the following command to execute::

    >> $ FC2 './pathto/testfile.csv'
    
The execution creates an outputs folder in your current working directory. 

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
