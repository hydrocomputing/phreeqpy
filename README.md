# PhreeqPy: Python Tools for PHREEQC

PhreeqPy is a collection of Python tools to work with
[PHREEQC](https://www.usgs.gov/software/phreeqc-version-3).

It provides access to the
[IPhreeqc](https://www.usgs.gov/software/phreeqc-version-3)
interface without the need to run a COM server and therefore also works on
non-Windows systems.
IPhreeqc is described in more detail in this
[publication](http://www.sciencedirect.com/science/article/pii/S0098300411000653).
This
[publication at the conference MODFLOW and More 2011](http://igwmc.mines.edu/conference/schedule.html)
demonstrates with an example how PhreeqPy works.

Starting from version 0.6, PhreeqPy supports
[PhreeqcRM](https://water.usgs.gov/water-resources/software/PHREEQC/PhreeqcRM_AbstractAWR.pdf).
Due to missing dependencies on PyPi, PhreeqcRM is only available in the conda
package, not via PyPi.

Install with:

    conda install -c hydrocomputing phreeqpy

or

    mamba install -c hydrocomputing phreeqpy

For pixi add this to your `pixi.toml`:

    [dependencies]
    phreeqpy = { version = "*", channel = "hydrocomputing" }

See `examples/phreeqcrm/advect.py` for an usage example for PhreeqcRM.

The IPhreeqc interface, i.e. all functionality before version 0.6,
is still available via a `pip` install:

    pip install phreeqpy
