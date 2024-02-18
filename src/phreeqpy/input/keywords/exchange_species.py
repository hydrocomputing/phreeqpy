# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# EquilibriumPhases doesn't have any public methods.
# pylint: disable-msg=W0232
# EquilibriumPhases doesn't have an _init__ method either.
# This is all intended.

"""Keyword Exchange_Species.
"""

from phreeqpy.input.base import DataEntry, DataLine, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, Float,
                                      PositiveFloat, String)



DOC = {
    'keyword': 'EXCHANGE_SPECIES',
    'keyword_EXCHANGE_SPECIES':
"""
This keyword data block is used to define a half-reaction and relative log K
for each exchange species. Normally, this data block is included in the
database file and only additions and modifications are included in the input
file.
""",

    'entry_association_reaction':
"""
Association reaction for exchange species. The defined species must be the
first species to the right of the equal sign. The association reaction must
precede any identifiers related to the exchange species. Master species have an
identity reaction.
""",

    'identifier_log_k':
"""
Identifier for log K at 25oC. Optionally, -log_k, logk, -l[og_k], or -l[ogk].
""",

    'entry_log K':
"""
Log K at 25oC for the reaction. Unlike log K for aqueous species, the log K for
exchange species is implicitly relative to a reference exchange species. In the
default database file, sodium (NaX) is used as the reference and the reaction
X- + Na+ = NaX is given a log K of 0.0. The identity reaction for a master
species has log K of 0.0 ; reactions for reference species
also have log K of 0.0. Default is 0.0.
""",

    'identifier_gamma':
"""
Indicates WATEQ Debye-Hückel equation will be used to calculate an activity
coefficient for the exchange species if the aqueous model is an ion-association
model (see -exchange_gammas in the EXCHANGE data block for information about
activity coefficients when using the Pitzer or SIT aqueous models). If -gamma
or -davies is not input for an exchange species, the activity of the species is
equal to its equivalent fraction. For further explanation, please refer to the
input mannual version 3, 2010, p66. Optionally, gamma or -g[amma].
""",
    
    'parameter_Debye-Hückel_a':
"""
Parameter ao in the WATEQ activity-coefficient equation.
""",

    'parameter_Debye-Hückel_b':
"""
Parameter b in the WATEQ activity-coefficient equation.
""",
    
    'parameter_active_fraction_coefficient':
"""
Parameter for changing log_k as a function of the exchange sites
occupied (Appelo, 1994). The active-fraction model is useful for modeling
sigmoidal exchange isotherms and proton exchange on organic matter (see
http://www.xs4all.nl/~appt/exmpls/a_f.html, accessed January 3, 2011).
""",  

    'identifier_davies':
"""
Indicates the Davies equation will be used to calculate an activity
coefficient. If -gamma or -davies is not input for an exchange species, the
activity of the species is equal to its equivalent fraction. If -davies is
entered, then an activity coefficient of the form of the Davies equation,
Optionally, davies or -d[avies].
"""

}    


association_reaction = DataEntry('association_reaction', ptype=String,
                               doc=DOC['entry_association_reaction'],
                               default=None)

log_K = DataEntry('log_K', ptype=Float, doc=DOC['entry_log_K'],
                   default=0.0)

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

class Exchange_Species(Keyword):
    """Keyword Exchange_Species."""
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_Exchange_Species']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    __phreeqpy_data_definition__ = [line1, line2]
    exchange_gammas = Identifier('exchange_gammas', ptype=Bool,
                      doc=DOC['identifier_exchange_gammas'], default=True)
