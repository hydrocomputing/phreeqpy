# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Delete.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'DELETE',
    'keyword_DELETE':
"""
This keyword data block is used to delete reactants. Any reactant that is
identified by an integer can be deleted, which includes reactants defined by
EQUILIBRIUM_PHASES, EXCHANGE, GAS_PHASE, KINETICS, MIX, REACTION,
REACTION_TEMPERATURE, SOLID_SOLUTIONS, SOLUTION, and SURFACE data blocks.
""",

    'identifier_equilibrium_phases':
"""
Identifier indicates that equilibrium-phase assemblages will be deleted.
Optionally, -e[quilibrium_phases]; note that the hyphen is necessary to
distinguish the identifier from the keyword EQUILIBRIUM_PHASES.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Equilibrium-phase assemblages identified by any of the numbers in the list will
be deleted.
""",

    'identifier_exchange':
"""
Identifier indicates that exchange assemblages will be deleted. Optionally,
-ex[change]; note that the hyphen is necessary to distinguish the identifier
from the keyword EXCHANGE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Exchange assemblages identified by any of the numbers in the list will be
deleted.
""", 

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Line 3 can be used to begin a list of ranges or to continue a list of ranges.
""",

    'identifier_gas_phase':
"""
Identifier indicates that gas phases will be deleted. Optionally, -g[as_phase];
note that the hyphen is necessary to distinguish the identifier from the
keyword GAS_PHASE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Gas phases identified by any of the numbers in the list will be deleted.
""", 

    'identifier_kinetics':
"""
Identifier indicates that kinetic reactants will be deleted. Optionally,
-k[inetics]; note that the hyphen is necessary to distinguish the identifier
from the keyword KINETICS.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Kinetics reactants identified by any of the numbers in the list will be
deleted.
""",
    
    'identifier_mix':
"""
Identifier indicates that solution mix definitions (defined by a MIX or COPY
data blocks) will be deleted. Optionally, -m[ix]; note that the hyphen is
necessary to distinguish the identifier from the keyword MIX.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Mix definitions identified by any of the numbers in the list will be deleted.
""", 

    'identifier_reaction':
"""
Identifier indicates that reactions (defined by a REACTION, REACTION_RAW,
or COPY data block) will be deleted. Optionally, -r[eaction]; note that the
hyphen is necessary to distinguish the identifier from the keyword REACTION.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reactions identified by any of the numbers in the list will be deleted.
""",

    'identifier_reaction_temperature':
"""
Identifier indicates that reaction-temperature definitions (as defined by
REACTION_TEMPERATURE, REACTION_TEMPERATURE_RAW, or COPY data blocks) will be
deleted. Optionally, -reaction_[temperature], temperature, or -t[emperature];
note that the hyphen is necessary to distinguish the identifier from the
keyword REACTION_TEMPERATURE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reaction-temperature definitions identified by any of the numbers in the list
will be deleted.
""",

    'identifier_solid_solution':
"""
Identifier indicates that solid-solution assemblages will be deleted.
Optionally, -soli[d_solutions]; note that the hyphen is necessary to
distinguish the identifier from the keyword SOLID_SOLUTIONS.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Solid-solution assemblages identified by any of the numbers in the list will be
deleted.
""",

    'identifier_solution':
"""
Identifier indicates that solutions will be deleted. Optionally, -s[olution];
note that the hyphen is necessary to distinguish the identifier from the
keyword SOLUTION.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Solutions identified by any of the numbers in the list will be deleted.
""",

    'identifier_surface':
"""
Identifier indicates that surface assemblages will be deleted. Optionally,
-su[rfaces]; note that the hyphen is necessary to distinguish the identifier
from the keyword SURFACE.
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Surface assemblages identified by any of the numbers in the list will be
deleted.
""",

    'identifier_cells':
"""
Identifier indicates that all reactants identified by a specified number will
be deleted, including equilibrium-phase assemblages, exchanger assemblages, gas
phases, kinetic reactants, mix definitions, reaction definitions, reaction
temperature definitions, solid-solution assemblages, solutions, and surface
assemblages. Optionally, -c[ells].
""",

    'entry_list_of_ranges':
"""
List of number ranges. The number ranges may be a single integer or a range
defined by an integer, a hyphen, and an integer, without intervening spaces.
Reactants of any type that are identified by any of the numbers in the list
will be deleted.
"""   
 
}    



class Delete(Keyword):
    """Keyword Delete."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_DELETE']
    __phreeqpy_allowed_identifiers__ = [equilibrium_phases, exchange,
                                        gas_phase, kinetics, mix, reaction,
                                        reaction_temperature, solid_solution,
                                        solution, surface, cells]
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    __phreeqpy_data_definition__ = [line3]
    
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
    
    reaction_temperature = Identifier('reaction_temperature', ptype=None,
                      doc=DOC['identifier_reaction_temperature'], default=True)

    solid_solution = Identifier('solid_solution', ptype=None,
                      doc=DOC['identifier_solid_solution'], default=True)

    solution = Identifier('solution', ptype=None,
                      doc=DOC['identifier_solution'], default=True)

    surface = Identifier('surface', ptype=None,
                      doc=DOC['identifier_surface'], default=True)

    cells = Identifier('cells', ptype=None,
                      doc=DOC['identifier_cells'], default=True)


    
