Pandas Time Indexing
====================

:date: 2015-05-05
:category: Blog
:tags: python, pandas, datetime 

The Python library `pandas <http://pandas.pydata.org/>`_ provides a wealth of time and data functionality that make a Python developer's life much easier, including 

* Conversion between a variety of time formats, see ``pandas.to_datetime()``
* Creation of a datetime index over a specified period and having a speified
  frequency, see ``pandas.date_range()``
* Use of datetime indexes as the primary index for a ``Series`` or ``DataFrame``
* Resampling of timeseries data using a new datetime index

.. code:: python

    import pandas as pd
    ts = pd.date_range('05-05-2015 16:00', periods=30, freq='S')
    ts[:5]

with output::

    <class 'pandas.tseries.index.DatetimeIndex'>
    [2015-05-05 16:00:00, ..., 2015-05-05 16:00:04]
    Length: 5, Freq: S, Timezone: None

Note the timezone is not specified so these timestamps are *naive*, they don't know their timezone, this information must be added separately using `pytz <http://pytz.sourceforge.net/>`_

Using DatetimeIndex
-------------------

A ``DatetimeIndex`` can be used as the index of a ``DataFrame`` or ``Series`` object:

.. code:: python

    import pandas as pd
    ts = pd.date_range('05-05-2015 16:00', periods=30, freq='S')

    df = pd.DataFrame(np.random.randn(30), index=ts)

The advantage of this is you can select the data ``df`` using a human readable
timestamp or one that is constructed programmatically.

.. code:: python

    df['2015-05-05 16:00:09':'2015-05-05 16:00:15']

which outputs this (or something like it)::

    2015-05-05 16:00:09 -0.358329
    2015-05-05 16:00:10 -1.253738
    2015-05-05 16:00:11 -0.070274
    2015-05-05 16:00:12  1.384043
    2015-05-05 16:00:13  2.049855
    2015-05-05 16:00:14  0.377063
    2015-05-05 16:00:15 -0.346427





