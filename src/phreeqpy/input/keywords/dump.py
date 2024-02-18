# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Dump.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'DUMP',
    'keyword_DUMP':
"""
This keyword data block is used to write complete definitions of reactants to a
specified file. The reactants are written in a “raw” format that saves the
exact chemical state of each specified reactant. The raw data blocks are
intended to be used intact to reinitialize simulations at the current state of
the calculations or to transfer reactants from one IPhreeqc module (Charlton
and Parkhurst, 2011) to another.
""",

    'identifier_file':
"""
Identifier is used to specify the name of the file to which the dump data are
written. Optionally, file or -f[ile].
""",

    'entry_file_name':
"""
Name of file where dump data are written. File names must conform to operating
system conventions. Default is dump.out.
""",

    'identifier_append':
"""
Identifier is used to specify whether the dump data will overwrite existing
data or will be appended to the end of the file, if the file exists. Default is
false, any data in the dump file are overwritten. Optionally, append or
-a[ppend].
""",

    'entry_(True or False)':
"""
A value of true indicates that the dump data will be appended to the end of the
dump file. A value of false indicates that any data in the dump file will be
overwritten. If neither true nor false is entered on the line, true is assumed.
Optionally, t[rue] or f[alse].
""", 

    'identifier_equilibrium_phases':
"""
Identifier indicates that equilibrium-phase assemblages will be dumped.
Optionally, -e[quilibrium_phases]; note that the hyphen is necessary to
distinguish the identifier from the keyword EQUILIBRIUM_PHASES.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Equilibrium-phase assemblages identified by any of the numbers in the list will
be dumped.
""", 

    'identifier_exchange':
"""
Identifier indicates that exchange assemblages will be dumped. Optionally,
-ex[change]; note that the hyphen is necessary to distinguish the identifier
from the keyword EXCHANGE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Exchange assemblages identified by any of the numbers in the list will be
dumped.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Line 5 can be used to begin a list of ranges or to continue a list of ranges.
""",
    
    'identifier_gas_phase':
"""
Identifier indicates that gas phases will be dumped. Optionally, -g[as_phase];
note that the hyphen is necessary to distinguish the identifier from the
keyword GAS_PHASE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Gas phases identified by any of the numbers in the list will be dumped.
""", 

    'identifier_kinetics':
"""
Identifier indicates that kinetic reactants will be dumped. Optionally,
-k[inetics]; note that the hyphen is necessary to distinguish the identifier
from the keyword KINETICS.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Kinetic reactants identified by any of the numbers in the list will be dumped.
""", 

    'identifier_mix':
"""
Identifier indicates that solution mix definitions (defined by MIX or COPY data
blocks) will be dumped. Optionally, -m[ix]; note that the hyphen is necessary
to distinguish the identifier from the keyword MIX.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Mix definitions identified by any of the numbers in the list will be dumped.
""", 

    'identifier_reaction':
"""
Identifier indicates that reactions (defined by a REACTION, REACTION_RAW, or
COPY data block) will be dumped. Optionally, -r[eaction]; note that the hyphen
is necessary to distinguish the identifier from the keyword REACTION.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reactions identified by any of the numbers in the list will be dumped.
""",

    'identifier_reaction_temperature':
"""
Identifier indicates that reaction-temperature definitions (as defined by
a REACTION_TEMPERATURE, REACTION_TEMPERATURE_RAW, or COPY data block) will be
dumped. Optionally, -reaction_[temperatures], temperature, or -t[emperature];
note that the hyphen is necessary to distinguish the identifier from the
keyword REACTION_TEMPERATURE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reaction-temperature definitions identified by any of the numbers in the list
will be dumped.
""",

    'identifier_solid_solution':
"""
Identifier indicates that solid-solution assemblages will be dumped.
Optionally, -soli[d_solutions]; note that the hyphen is necessary to
distinguish the identifier from the keyword SOLID_SOLUTIONS.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Solid-solution assemblages identified by any of the numbers in the list will be
dumped.
""",

    'identifier_solution':
"""
Identifier indicates that solutions will be dumped. Optionally, -s[olution];
note that the hyphen is necessary to distinguish the identifier from the
keyword SOLUTION.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Solutions identified by any of the numbers in the list will be dumped.
""",

    'identifier_surface':
"""
Identifier indicates that surface assemblages will be dumped. Optionally,
-su[rfaces]; note that the hyphen is necessary to distinguish the identifier
from the keyword SURFACE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Surface assemblages identified by any of the numbers in the list will be
dumped.
""",

    'identifier_cells':
"""
Identifier indicates that all reactants identified by a specified number will
be dumped, including equilibrium-phase assemblages, exchanger assemblages, gas
phases, kinetic reactants, mix definitions, reaction definitions, reaction
temperature definitions, solid-solution assemblages, solutions, and surface
assemblages. Optionally, cell, cells, or -c[ells].
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reactants of any type that are identified by any of the numbers in the list
will be dumped.
""",

    'identifier_all':
"""
Identifier indicates that all reactants will be dumped, including
equilibrium-phase assemblages, exchanger assemblages, gas phases, kinetic
reactants, mix definitions, reaction definitions, reaction temperature
definitions, solid-solution assemblages, solutions, and surface assemblages.
Optionally, all or -al[l].
"""
 
}    



class Dump(Keyword):
    """Keyword Dump."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_DUMP']
    __phreeqpy_allowed_identifiers__ = [file, append, equilibrium_phases,
                                        exchange, gas_phase, kinetics, mix,
                                        reaction, reaction_temperature,
                                        solid_solution, solution, surface,
                                        cells, all]
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    __phreeqpy_data_definition__ = [line5]
    
    file = Identifier('file', ptype=None,
                      doc=DOC['identifier_file'], default=True)

    append = Identifier('equilibrium_append', ptype=None,
                      doc=DOC['identifier_append'], default=True)

    equilibrium_phases = Identifier('equilibrium_phases', ptype=None,
                      doc=DOC['identifier_equilibrium_phases'], default=True)
    
    exchange = Identifier('exchange', ptype=None,
                      doc=DOC['identifier_exchange'], default=True)
    
    gas_phase = Identifier('gas_phase', ptype=None,
                      doc=DOC['identifier_gas_phase'], default=True)

    kinetics = Identifier('kinetics', ptype=None,
                      doc=DOC['identifier_kinetics'], default=True)
    
    mix = Identifier('mix', ptype=None,
                      doc=DOC['identifier_mix'], default=True)

    reaction = Identifier('reaction', ptype=None,
                      doc=DOC['identifier_reaction'], default=True)
    
    reaction_temperature = Identifier('temperature', ptype=None,
                      doc=DOC['identifier_temperature'], default=True)

    solid_solution = Identifier('solid_solution', ptype=None,
                      doc=DOC['identifier_solid_solution'], default=True)

    solution = Identifier('solution', ptype=None,
                      doc=DOC['identifier_solution'], default=True)

    surface = Identifier('surface', ptype=None,
                      doc=DOC['identifier_surface'], default=True)

    cells = Identifier('cells', ptype=None,
                      doc=DOC['identifier_cells'], default=True)

    cells = Identifier('cells', ptype=None,
                      doc=DOC['identifier_cells'], default=True)
    
