# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Gas_Phase.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)


DOC = {
    'keyword': 'GAS_PHASE',
    'keyword_GAS_PHASE':
"""
This keyword data block is used to define the composition of a fixed-total-
pressure or a fixed-volume multicomponent gas phase. A GAS_PHASE data block is
not needed if fixed partial pressures of gas components are desired; use
EQUILIBRIUM_PHASES instead. The gas phase defined with this keyword data block
subsequently may be equilibrated with an aqueous phase in combination with
pure-phase, surface, exchange, and solid-solution assemblages in batch-reaction
calculations. As a consequence of batch reactions, a fixed-pressure gas phase
may exist or not, depending on the sum of the partial pressures of the 
dissolved gases in solution. A fixed-volume gas phase always contains some
amount of each gas component that is present in solution. The initial
composition of a fixed-pressure gas phase is defined by the partial pressures
of each gas component. The initial composition of a fixed-volume gas may be
defined by the partial pressures of each gas component or may be defined to be
that which is in equilibrium with a fixed-composition aqueous phase. The
thermodynamic properties of the gas components are defined with PHASES input.
""",

    'identifier_fixed_pressure':
"""
Identifier defining the gas phase to have a fixed total pressure, that is a gas
bubble. A fixed-pressure gas phase is the default if neither the -fixed_
pressure nor the -fixed_volume identifier is used. Optionally fixed_pressure,
or -fixed_p[ressure].
""",

    'identifier_pressure':
"""
Identifier defining the fixed pressure of the gas phase that applies during all
batch-reaction and transport calculations. Optionally pressure, or -p[ressure].
""",

    'entry_pressure':
"""
The pressure of the gas phase, in atmospheres. Default is 1.0 atm.
""",

    'identifier_volume':
"""
Identifier defining the initial volume of the fixed-pressure gas phase.
Optionally, volume, or -v[olume].
""",    
        
    'entry_volume':
"""
The initial volume of the fixed-pressure gas phase, in liters. The ideal gas
law, n = PV / (RT), with volume V, temp T, partial pressures P, and the gas
constant R (0.08207 L K-1mol-1, liter per degree kelvin per mole), is used to
calculate the initial moles of each gas component in the fixed-pressure gas
phase. Default is 1.0 liter.
""",  

    'identifier_temperature':
"""
Identifier defining the initial temperature of the gas phase. Optionally,
temperature, or -t[emperature].
""",

    'entry_temp':
"""
The initial temperature of the gas phase, in Celsius. The temp along with
volume and partial pressure are used to calculate the initial moles of each gas
component in the fixed-pressure gas phase. Default is 25.0.
""",  

    'entry_phase_name':
"""
Name of a gas component. A phase with this name must be defined by PHASES
input in the database or input file.
""",

    'entry_partial_pressure':
"""
Initial partial pressure of this component in the gas phase, in atmospheres.
The partial pressure along with volume and temp are used to calculate the
initial moles of this gas component in the fixed-pressure gas phase.
"""


}    


exchange_formula_1 = DataEntry('exchange_formula', ptype=String,
                               doc=DOC['entry_exchange_formula_1'],
                               default=None)

amount = DataEntry('amount', ptype=PositiveFloat, doc=DOC['entry_amount'],
                   default=None)

exchange_formula_2 = DataEntry('exchange_formula', ptype=String,
                               doc=DOC['entry_exchange_formula_2'],
                               default=None)

name = DataEntry('name', ptype=String, doc=DOC['entry_name'],
                   default=None)

equilibrium_phase = DataEntry('equilibrium_phase', ptype=Float,
                              doc=DOC['qualifier_equilibrium_phase'],
                              default=0.0)                     
                                                 
kinetic_reactant = DataEntry('kinetic_reactant', ptype=Float,
                             doc=DOC['qualifier_kinetic_reactant'],
                             default=0.0)                       
                                                
exchange_per_mole = DataEntry('exchange_per_mole', ptype=PositiveFloat,
                      doc=DOC['entry_exchange_per_mole'], default=None)

line1 = DataLine(exchange_formula_1, amount)

line2 = DataLine(exchange_formula_2, name, [(equilibrium_phase,
                                             kinetic_reactant)],
                 exchange_per_mole)

class Exchange(Keyword):
    """Keyword Exchange."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_EXCHANGE']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = True
    __phreeqpy_has_description__ = True
    __phreeqpy_data_definition__ = [line1, line2]
    exchange_gammas = Identifier('exchange_gammas', ptype=Bool,
                      doc=DOC['identifier_exchange_gammas'], default=True)
