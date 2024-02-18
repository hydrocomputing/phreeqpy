# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Copy.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'COPY',
    'keyword_COPY':
"""
This keyword data block is used to make copies of any of the numbered
reactants, which include equilibrium-phase assemblages, exchange assemblages,
gas phases, kinetic reactions, mix definitions, reactions, reaction-temperature
definitions, solid-solution assemblages, solutions, or surface assemblages.
These reactants are often defined by the EQUILIBRIUM_PHASES, EXCHANGE,
GAS_PHASE, KINETICS, MIX, REACTION, REACTION_TEMPERATURE, SOLID_SOLUTIONS,
SOLUTION, and SURFACE data blocks, but may be defined or modified with the
SAVE, _RAW, or _MODIFY (see Appendix A in the input mannal Version 3, 2010)
data blocks.
""",

    'qualifier_reactant':
"""
The word “cell”, or one of the 10 reactants that can be identified by an
integer--equilibrium_phases, exchange, gas_phase, kinetics, mix, reaction,
reaction_temperature, solid_solution, solution, or surface.
""",

    'entry_source_number':

"""
An integer designating the reactant to be copied. If reactant is cell, all
reactants identified by source_number will be copied.
""",

    'entry_destination_number_range':

"""
A single number or a range of numbers designated by an integer
followed by a hyphen, followed by a integer, with no intevening spaces. A copy
of the source reactant will be made for each of the numbers in the range. If
reactant is cell, all reactants identified by source_number will be copied for
each of the numbers in the range.
""",

}    


source_number = DataEntry('source_number', ptype=String,
                               doc=DOC['source_number'],
                               default=None)

destination_number_range = DataEntry('destination_number_range',
                                     ptype=PositiveFloat,
                                     doc=DOC['entry_destination_number_range'],
                                     default=None)

                                                
exchange_per_mole = DataEntry('exchange_per_mole', ptype=PositiveFloat,
                      doc=DOC['entry_exchange_per_mole'], default=None)


class Copy(Keyword):
    """Keyword Copy."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_COPY']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = True
    __phreeqpy_has_description__ = True
    __phreeqpy_data_definition__ = []
    