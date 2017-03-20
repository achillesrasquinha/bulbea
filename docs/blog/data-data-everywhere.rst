Data, Data Everywhere
=====================
	*"In God we trust, all others must bring data."* - W. Edwards Deming

How data is stored
++++++++++++++++++

Data streams itself right from when the gates of a stock exchange open to when it closes. Such data contains vital information that is archived each day. Some of the many types of information recieved after trading hours are - *opening price*, *closing price*, *volumne of shares*, *highest price*, *lowest price*, etc. for each enterprise.

**bulbea** helps you access such information (both - archived and the latest). Simply create a :py:class:`Share <bulbea.Share>` with a known :code:`source` and :code:`ticker` as follows:

.. code:: python

	>>> import bulbea as bb
	>>> share = bb.Share(source = 'YAHOO', ticker = 'GOOGL')
	>>> share.data
	                  Open        High         Low       Close      Volume  Adjusted Close
	Date
	2004-08-19   99.999999  104.059999   95.959998  100.339998  44659000.0       50.220219
	2004-08-20  101.010005  109.079998  100.500002  108.310002  22834300.0       54.209210
	2004-08-23  110.750003  113.479998  109.049999  109.399998  18256100.0       54.754754
	...

Data is accessed through the :py:mod:`Quandl <quandl>` API stored remotely at sources in the form of CSV (Comma-Seperated Values) files. Information retrieved from such a CSV file is then wrapped around a :py:class:`pandas.DataFrame <pandas.DataFrame>` object.

Comma, Seperated, Value?
------------------------

CSV files store tabular data in simple plain text (well, fits the need). Each row containing values associated to each attribute of a table are stored in a single line, where each value is seperated by a delimiter, you guessed it right, a comma. For instance, a data set containing the weight (in kilograms) and height (in inches) of members of my family would look something like the following:

.. code:: raw

	weight,height
	87,6.2
	51,5.8
	68,5.9
	...

Almost always, the top-most line (also called as *the header*) should denote the attribute names seperated by the delimiter.

You can save a share object in a CSV format as follows:

.. code:: python

	>>> share.save()

By default, the :py:meth:`save <bulbea.Share.save>` method saves a share as a CSV file in the working directory with a file name of the format - :code:`<source>_<ticker>_<start>_<end>.csv`. You could also name the file anything you like as follows:

.. code:: python

	>>> share.save(filename = 'mycsvfile.csv')

:py:class:`pandas.DataFrame`
----------------------------