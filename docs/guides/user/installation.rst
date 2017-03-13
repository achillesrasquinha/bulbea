.. _installation:

Installation
============

Building from source
++++++++++++++++++++

You can clone the repository with `git` as follows:

.. code-block:: console

    $ git clone https://github.com/achillesrasquinha/bulbea.git && cd bulbea

Install necessary dependencies

.. code-block:: console

    $ pip install -r requirements.txt

You may have to manually install TensorFlow

.. code-block:: console

    $ pip install tensorflow # CPU-only

OR

.. code-block:: console

    $ pip install tensorflow-gpu # GPU-only, requires CUDA and CuDNN

Then, go ahead and install as follows:

.. code-block:: console

    $ python setup.py install
