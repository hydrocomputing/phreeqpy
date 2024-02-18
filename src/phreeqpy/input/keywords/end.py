# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword End.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'END',
    'keyword_END':
"""
This keyword has no associated data. It ends the data input for a simulation.
After this keyword is read by the program, the calculations described by the
input for the simulation are performed and the results printed. Additional
simulations may follow in the input data set, each in turn will be terminated
with an END keyword or the end of the file.
"""
