# -*- coding: utf-8 -*-

# pylint: disable-msg=W0622
# We want help to have the same as the builtin function.
# pylint: disable-msg=C0103
# Globals with no all upper case are allowed.
# This is just a namespace flattening thing.


"""Phreeqpy input tools for PHREEQC.

This is just a namespace beautifier.
The code is in sibling package `input`.
"""


from phreeqpy.input.base import phreeqpy_help
from phreeqpy.input.keywords.advection import Advection
from phreeqpy.input.keywords.equilibrium_phases import EquilibriumPhases

class Keywords(object):
    """Manage how the user can access keywords. 
    """

    def __init__(self):
        self.keyword_list = ['Advection', 'EquilibriumPhases']
        self.helpers = ['help', 'keyword_list']
        self.Advection = Advection
        self.EquilibriumPhases = EquilibriumPhases

    def __dir__(self):
        return self.keyword_list + self.helpers
    
    def help(self, obj=None, verbose=False):
        return phreeqpy_help(obj, verbose)
