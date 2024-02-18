# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Exchange.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)

DOC_EQUI_KIN = """
If equilibrium_phase is used, the name on the line is a phase defined in an
EQUILIBRIUM_PHASES data block. If kinetic_reactant is used, the name on the
line is the rate name for a kinetic reactant defined in a KINETICS data block.
Optionally, e or k, only the first letter is checked. Default is
equilibrium_phase.
"""

DOC = {
    'keyword': 'EXCHANGE',
    'keyword_EXCHANGE':
"""
This keyword data block is used to define the amount and composition of an
assemblage of exchangers. The initial composition of the exchange assemblage
can be defined in two ways, (1) explicitly by listing the
composition of each exchange component or (2) implicitly, by specifying that
each exchanger is in equilibrium with a solution of fixed composition. The
exchange master species, stoichiometries, and log Ks for the exchange reactions
are defined with the keywords EXCHANGE_MASTER_SPECIES and EXCHANGE_SPECIES. The
number of exchange sites can be fixed; can be related to the amount of a phase
in a phase assemblage; or can be related to the amount of a kinetic reactant.
""",

    'entry_exchange_formula_1':
"""
Exchange species including stoichiometry of exchange ion and exchanger.
""",

    'entry_amount':
"""
Quantity of exchange species, in moles
""",

    'entry_exchange_formula_2':
"""
Exchange species including stoichiometry of exchange ion and exchange
site(s). The exchange formula must be charge balanced; if no exchange ions are
included in the formula, then the exchange site must be uncharged.
""",

    'entry_name':
"""
Name of the pure phase or kinetic reactant that has this kind of exchange site.
If name is a phase, the amount of the phase in an EQUILIBRIUM_PHASES data block
with the same number as this exchange number 
will be used to determine the number of exchange sites. If name is a kinetic
reactant, the amount of the reactant in a KINETICS data block with the same
number as this exchange number will be used to
determine the number of exchange sites. Some care is needed in defining the
stoichiometry of the exchange species if the exchangeable ions are related to a
phase or kinetic reactant. The assumption is that some of the ions in the pure
phase or kinetic reactant are available for exchange and these ions are defined
through one or more entries of Line 2. The stoichiometry of the phase (defined
in a PHASES data block) or kinetic reactant (defined in a KINETICS data block)
must contain sufficient amounts of the exchangeable ions. 
""",
    
    'qualifier_equilibrium_phase': DOC_EQUI_KIN,

    'qualifier_kinetic_reactant': DOC_EQUI_KIN,
    
    'entry_exchange_per_mole':
"""
Number of moles of the exchange species per mole of phase or kinetic reactant,
unitless (mol/mol).
""",  

    'identifier_exchange_gammas':
"""
This identifier selects whether exchange activity coefficients are assumed
to be equal to aqueous activity coefficients when using the Pitzer or SIT
aqueous model. The option has no effect when using ion-association aqueous
models. Default is True. Optionally, exchange_gammas or -ex[change_gammas].
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
