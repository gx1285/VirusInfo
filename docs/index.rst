VirusInfo Docs
==============

Getting started
---------------

.. _prerequisite:

Prerequisite.
~~~~~~~~~~~~~
| VirusInfo supports Python 3.8 or later.
| Therefore, it can also be used on Windows 7.

Installing
~~~~~~~~~~
This library is available from pypi. ::

    python3 -m pip install -U VirusInfo
    
Installation on Windows is as follows ::

    py -3 -m pip install -U VirusInfo

Congratulations. You have now completed the installation.    

Manuals
------------
`API Reference`_

.. _API Reference: api.rst
Quickstart
------------
| For example, let's get the number of new Covid-19 cases in Japan on March 9, 2022.
| (v0.3.0)
.. code:: py

   import VirusInfo
   print(VirusInfo.covid_19_ja(20220309))
   # 25478
