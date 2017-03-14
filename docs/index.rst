bulbea
======
    *Deep Learning based Python Library for Stock Market Prediction and Modelling*

Release: v\ |release| (:ref:`Installation <installation>`)

.. image:: https://img.shields.io/gitter/room/bulbea/bulbea.svg
  :target: https://gitter.im/bulbea/bulbea

**bulbea** is an open source Python library that implements various tools (preprocessing, visualizations, modelling, etc.) for quantitative analysis and prediction using deep learning.

**bulbea** helps you with

**Statistical Vizualization**

.. code:: python

    >>> import bulbea as bb
    >>> share = bb.Share('YAHOO', 'GOOGL')
    >>> share.plot(bollinger_bands = True, period = 100, bandwidth = 2, figsize = (20, 15))

.. image:: _static/google_bollinger_bands.png

Guide - User
++++++++++++

.. toctree::
  :maxdepth: 2

  guides/user/installation
  guides/user/quickstart

Guide - API
+++++++++++

.. toctree::
  :maxdepth: 2

  guides/api
