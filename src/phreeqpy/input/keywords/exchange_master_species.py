# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Exchange_Master_Species.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'EXCHANGE_MASTER_SPECIES',
    'keyword_EXCHANGE_MASTER_SPECIES':
"""
This keyword data block is used to define the correspondence between the name
of an exchange site and an exchange species that is used as the master species
in calculations. Normally, this data block is included in the database file and
only additions and modifications are included in the input file.
""",

    'entry_exchange_name':
"""
Name of an exchange site, X and Xa, for example . It must begin with a capital
letter, followed by zero or more lower case letters or underscores (“_”).
""",

    'entry_exchange_master_species':
"""
Formula for the master exchange species, X- and Xa-, for example.
"""

}    

exchange_name = DataEntry('exchange_name', ptype=String,
                               doc=DOC['entry_exchange_name'],
                               default=None)

exchange_master_species = DataEntry('exchange_master_species',
                                ptype=String,
                                doc=DOC['entry_exchange_master_species'],
                                default=None)


class Exchange_Master_Species(Keyword):
    """Keyword Exchange_Master_Species."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_EXCHANGE_MASTER_SPECIES']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    __phreeqpy_data_definition__ = []
    