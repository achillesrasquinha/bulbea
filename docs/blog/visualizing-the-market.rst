Vizualizing the Market
======================

Global Statistics
+++++++++++++++++

Global Mean
-----------

Rolling Statistics
++++++++++++++++++

Bollinger Bands (R)
-------------------

Bollinger Bands (R) measure the "highness" and "lowness" of share price relative to its previous trades. We call the days to look back for its previous trades as `window` or `period`.

Bollinger Bands (R) consists of:

* An N-period Moving Average (MA) band.
* An upper band K (bandwidth) times the standard deviation above the MA 

.. math:: 
	
	(MA + K\sigma)

* A lower band K (bandwidth) times the standard deviation below the MA

.. math:: 

	(MA - K\sigma)

**bulbea** helps you with calculating as well as visualizing these bands. Let's consider GOOGL shares. Create a share object as follows:

.. code:: python

	>>> import bulbea as bb
	>>> share = bb.Share('YAHOO', 'GOOGL')

Next, to determine the Bollinger Bands (R) for a given share, simply use the :py:meth:`bollinger_bands <bulbea.Share.bollinger_bands>` method as follows:

.. code:: python

	>>> bollinger = share.bollinger_bands()
	>>> bollinger.tail()
	            Lower (Close)  Mean (Close)  Upper (Close)
	Date
	2017-03-07     815.145883    831.694803     848.243724
	2017-03-08     816.050821    832.574004     849.097187
	2017-03-09     817.067353    833.574805     850.082257
	...

Plotting Bollinger Bands (R) is simple. Just use the :py:meth:`plot <bulbea.Share.plot>` API as follows:

.. code:: python

    >>> share.plot(bollinger_bands = True, period = 100, bandwidth = 2)

.. image:: ../_static/google_bollinger_bands.png

