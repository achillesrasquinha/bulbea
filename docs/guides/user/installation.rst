.. _installation:

Installation
============

Building from source
++++++++++++++++++++

**bulbea** is actively developed on GitHub_ and is always avaliable.

.. _GitHub: https://github.com/achillesrasquinha/bulbea

You can clone the base repository with :code:`git` as follows:

.. code-block:: console

    $ git clone git@github.com:achillesrasquinha/bulbea.git

Optionally, you could download the tarball_ or zipball_ as follows:

.. _tarball: https://github.com/achillesrasquinha/tarball/bulbea
.. _zipball: https://github.com/achillesrasquinha/zipball/bulbea

**For Linux Users**

.. code-block:: console

	$ curl -OL https://github.com/achillesrasquinha/tarball/bulbea

**For Windows Users**

.. code-block:: console

	$ curl -OL https://github.com/achillesrasquinha/zipball/bulbea

Install necessary dependencies

.. code-block:: console

    $ pip install -r requirements.txt

**bulbea** depends on Keras which thereby depends on TensorFlow as a backend. You may have to manually install TensorFlow as follows:

.. code-block:: console

    $ pip install tensorflow # CPU-only

OR

.. code-block:: console

    $ pip install tensorflow-gpu # GPU-only, requires NVIDIA CUDA and cuDNN

Then, go ahead and install **bulbea** in your site-packages  as follows:

.. code-block:: console

    $ python setup.py install

Check to see if you've installed **bulbea** correctly.

.. code-block:: python

	>>> import bulbea as bb
