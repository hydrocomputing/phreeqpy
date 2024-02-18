PhreeqPy - Python Tools for PHREEQC
====================================


Introduction
------------

PhreeqPy is Open Source software and provides Python tools to work with
PHREEQC_.

Currently it provides access to the new IPhreeqc_ interface without the need to
run a COM server and therefore also works on non-Windows systems.
IPhreeqc is described in more detail in this publication_.

`Please let us know`_ what you do with PhreeqPy or if things do not work
as expected. There is a
`mailing list for PhreeqPy <https://groups.google.com/forum/#!forum/phreeqpy-users>`_.
Please subscribe_ to get your questions about PhreeqPy answered.


`Download latest version of this documentation as PDF <phreeqpy.pdf>`_


**License**: BSD

.. _installation:

Installation
------------

**Pythons (tested)**: Python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6, 3.8, 3.7, 3.9, 3.10 PyPy

**Pythons (untested but should work since using ctypes)**: IronPython, Jython 2.7

**Platforms**: Unix/Posix and Windows

**PyPI package name**: `phreeqpy <http://pypi.python.org/pypi/phreeqpy>`_


Installation with `pip`::

    pip install -U phreeqpy


You need an IPhreeqc shared libray for your operating system.
PhreeqPy comes with shared libraries for 32-bit Windows, 32-bit Linux and
64-bit Mac OS X.
To use the COMM server, please install the `Windows COM 64-bit`_ module
of IPhreeqc and use
``phreeqpy.iphreeqc.phreeqc_com as phreeqc_mod`` instead of
``import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod`` as shown in the example.
If you use Anaconda or Miniconda make sure to:

    conda install pywin32

before you install PhreeqPy.

.. _`Windows COM 64-bit`: https://water.usgs.gov/water-resources/software/PHREEQC/index.html

You may download an appropriate library from here:
https://www.usgs.gov/software/phreeqc-version-3

For example for Linux::

    wget https://water.usgs.gov/water-resources/software/PHREEQC/iphreeqc-3.7.3-15968.tar.gz
    tar -xzvf iphreeqc-3.7.3-15968.tar.gz
    cd iphreeqc-3.7.3-15968
    ./configure
    make
    make check
    sudo make install


Then either use the full path to the shared libray when making an instance of
``phreeqc_dll.IPhreeqc``

.. code-block:: python

    phreeqc = phreeqpy.iphreeqc.phreeqc_dll.IPhreeqc('/full/path/to/libiphreeqc.so')


or copy the shared object into ``phreeqpy/iphreeqc`` replacing the existing
one. For example::

    sudo cp /usr/local/lib/libiphreeqc.so  /path/to/site-packages/phreeqpy/iphreeqc/libiphreeqc.so.0.0.0


Benchmark Test Comparing PhreeqPy to External Processes, COM and C++
--------------------------------------------------------------------

This publication demonstrates how PhreeqPy can be used for reactive transport
modeling.

Müller M., Parkhurst D.L., Charlton S.R. (2011)
`Programming PHREEQC Calculations with C++ and Python - A Comparative Study`_ ,
In: Maxwell R., Poeter E., Hill M., Zheng C. (2011) MODFLOW and More 2011 -
Integrated Hydrological Modeling, Proceedings, pp. 632 - 636.


.. _`Programming PHREEQC Calculations with C++ and Python - A Comparative Study`: Mueller_etal_MODFLOWandMORE2011_Proceedings.pdf



.. _PHREEQC: http://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/index.html
.. _IPhreeqc: ftp://brrftp.cr.usgs.gov/pub/charlton/iphreeqc/IPhreeqc.pdf
.. _publication: http://www.sciencedirect.com/science/article/pii/S0098300411000653
.. _`MODFLOW and More 2011`: http://igwmc.mines.edu/conference/schedule.html
.. _`Please let us know`: contact.html
.. _`sent us you email address`: contact.html
.. _subscribe: phreeqpy-users+subscribe@googlegroups.com?subject=Subscribe
