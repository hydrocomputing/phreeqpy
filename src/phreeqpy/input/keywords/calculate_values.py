# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Calculate_Values.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'CALCULATE_VALUES',
    'keyword_CALCULATE_VALUES':
"""
This keyword data block is used to define Basic functions that can be used in
other PHREEQC Basic programs or to display isotopic compositions as defined in
the ISOTOPE_ALPHAS and ISOTOPE_RATIOS data blocks. Isotope ratios are the ratio
of moles of a minor isotope to moles of a major isotope in a aqueous, gas, or
mineral or mineral species. Isotope alphas are the ratio of two isotope ratios,
which is the fractionation factor between two species. The data block is used
primarily to display results from the isotopic simulations, but also can be
used to write Basic functions to simplify Basic programming for RATES, USER_
GRAPH, USER_PRINT, and USER_PUNCH.
""",

    'entry_name_of_Basic_function':
"""
Alphanumeric character string that defines the name of the Basic
function; no spaces are allowed.
""",

    'identifier_start':

"""
Identifier marks the beginning of a Basic program. Optional.
""",
    
    'entry_numbered_Basic_statement':

"""
A valid Basic language statement that must be numbered. The
statements are evaluated in numerical order. The statement “SAVE expression”
must be included in the list of statements, where the value of expression is
the result that is returned from the Basic function. Statements and functions
that are available through the Basic interpreter are listed in The Basic
Interpreter (tables 7 and 8 in the Input mannual version 3, 2010).
""",   

    'identifier_end':
"""
Identifier marks the end of a Basic function. Note the hyphen is required to
avoid a conflict with the keyword END.
"""

}    


name_of_Basic_function = DataEntry('name_of_Basic_function', ptype=String,
                               doc=DOC['name_of_Basic_function'],
                               default=None)

numbered_Basic_statement = DataEntry('numbered_Basic_statement', ptype=String,
                               doc=DOC['numbered_Basic_statement'],
                               default=None)




line1 = DataLine(name_of_Basic_function)
line3 = DataLine(numbered_Basic_statement)

class Calculat_Values(Keyword):
    """Keyword Calculate_Values."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_CALCULATE_VALUES']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    start = Identifier('start', ptype=None,
                      doc=DOC['identifier_start'], default=True)
    end = Identifier('end', ptype=None,
                      doc=DOC['identifier_end'], default=True)
    __phreeqpy_data_definition__ = [line1, start, line3, end]

