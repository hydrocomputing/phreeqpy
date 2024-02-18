# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword EquilibriumPhases.
"""

__all_ = ['EquilibriumPhases']
from phreeqpy.input.base import Identifier, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'EQUILIBRIUM_PHASES',
    'keyword_EQUILIBRIUM_PHASES':
"""
This keyword data block is used to define the amounts of an assemblage of pure
phases that can react reversibly with the aqueous phase. When the phases
included in this keyword data block are brought into contact with an aqueous
solution, each phase will dissolve or precipitate to achieve equilibrium or
will dissolve completely. Pure phases include minerals with fixed composition
and gases with fixed partial pressures. Two types of input are available: in
one type, the phase itself reacts to equilibrium (or a specified saturation
index or gas partial pressure); in the other type, an alternative reaction
occurs to the extent necessary to reach equilibrium (or a specified saturation
index or gas partial pressure) with the specified pure phase.""",

    'entry_phase name':
"""
Name of a phase. The phase must be defined with PHASES input, either in the
database file or in the current or previous simulations of the run. The name
must be spelled identically to the name used in PHASES input (except for case).
""",

    'entry_saturation_index':

"""
Target saturation index for the pure phase in the aqueous phase (line 1a); for
gases, this number is the log of the partial pressure (line 1b). The target
saturation index (partial pressure) may not be attained if the amount of the
phase in the assemblage is insufficient.
""",

    'entry_alternative_formula':

"""
Chemical formula that is added (or removed) to attain the target saturation
index (or log partial pressure). By default, the mineral defined by phase name
dissolves or precipitates to attain the target saturation index. If alternative
formula is entered, phase name does not react; the stoichiometry of alternative
formula is added or removed from the aqueous phase to attain the target
saturation index. Alternative formula must be a legitimate chemical formula
composed of elements defined to the program. Line 1c indicates that the
stoichiometry given by alternative formula, KAlSi3O8 (potassium feldspar), will
be added or removed from the aqueous phase until gibbsite equilibrium is
attained. The alternative formula and alternative phase are mutually exclusive
fields.
""",

    'entry_alternative_phase':

"""
The chemical formula defined for alternative phase is added (or removed) to
attain the target saturation index (or log partial pressure). By default, the
mineral defined by phase name dissolves or precipitates to attain the target
saturation index. If alternative phase is entered, phase name does not react;
the stoichiometry of the alternative phase is added or removed from the
aqueous phase to attain the target saturation index. Alternative phase must be
defined through PHASES input (either in the database file or in the present or
previous simulations). Line 1d indicates that the phase gypsum will be added to
or removed from the aqueous phase until calcite equilibrium is attained. The
alternative formula and alternative phase are mutually exclusive fields.
""",

    'entry_amount':

"""
Moles of the phase in the phase assemblage or moles of the alternative
reaction. This number of moles defines the maximum amount of the mineral or
gas that can dissolve. It may be possible to dissolve the entire amount
without reaching the target saturation index, in which case the solution will
have a smaller saturation index for this phase than the target saturation
index. If amount is equal to zero, then the phase can not dissolve, but will
precipitate if the solution becomes supersaturated with the phase.
"""

}


class EquilibriumPhases(Keyword):
    """Keyword EquilibriumPhases."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_EQUILIBRIUM_PHASES']
    __phreeqpy_allowed_identifiers__ = ['phase_name', 'saturation_index',
                                        'alternative_formula',
                                        'alternative_phase', 'amount']
    __phreeqpy_has_number__ = True
    __phreeqpy_has_description__ = True
    phase_name = Identifier('phase_name', ptype=String, doc=DOC['entry_phase name'],
                       default=None)
    sat_index = Identifier('saturation_index', ptype=Float,
                          doc=DOC['entry_saturation_index'], default=0.0)
    alt_formula = Identifier('alternative_formula', ptype=String,
                            doc=DOC['entry_alternative_formula'], default=None)
    alt_phase = Identifier('alternative_phase', ptype=String,
                          doc=DOC['entry_alternative_phase'], default=None)
    amount = Identifier('amount', ptype=PositiveFloat, doc=DOC['entry_amount'],
                       default=10.0)
    line1 = DataLine(phase_name,[sat_index, [(alt_formula, alt_phase), [amount]]])
    __phreeqpy_data_definition__ = [line1]

    
