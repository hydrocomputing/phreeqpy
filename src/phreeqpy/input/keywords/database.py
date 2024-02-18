# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Database.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (CellNumberList, Float,
                                      PositiveFloat, String)



DOC = {
    'keyword': 'DATABASE',
    'keyword_DATABASE':
"""
This keyword data block is used to specify a database for the simulations.
""",

    'keyword_data_database_file_name':
"""
File name for the database. If the database is not in the working directory,
then a path name relative to the working directory or an absolute path name
must be given.
""",

}    


database = DataEntry('database', ptype=String,
                               doc=DOC['entry_database'],
                               default=None)

class Database(Keyword):
    """Keyword Database."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_DATABASE']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = True
    __phreeqpy_has_description__ = True
    __phreeqpy_data_definition__ = []
    