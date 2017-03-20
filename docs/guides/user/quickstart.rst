Quickstart
==========

Waiting to make some money? We introduce you to a quick way of building your first prediction model.

Create a :py:class:`Share <bulbea.Share>` object
++++++++++++++++++++++++++++++++++++++++++++++++

The canonical way of importing bulbea as follows:

.. code:: python

    >>> import bulbea as bb

Go ahead and create a share object.

.. code:: python

    >>> share = bb.Share(source = 'YAHOO', ticker = 'GOOGL')
