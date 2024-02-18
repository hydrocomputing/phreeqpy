# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# Advection doesn't have any public methods.
# pylint: disable-msg=W0232
# Advection doesn't have an _init__ method either.
# This is also intended.

"""Keyword ADVECTION.
"""

__all__ = ['Advection']

from phreeqpy.input.base import Identifier, Keyword
from phreeqpy.input.datatypes import (Bool, CellNumberList, PositiveInteger,
                                      PositiveFloat)

DOC = {
    'keyword': 'ADVECTION',
    'keyword_ADVECTION':
"""
This keyword data block is used to specify the number of cells and the number
of "shifts" for an advection simulation. Advection simulations are used to
model one dimensional advective or "plug" flow with reactions. No dispersion
or diffusion is simulated and no cells with immobile water are allowed.
However, all chemical processes modeled by PHREEQC may be included in an
advection simulation. The TRANSPORT data block may be used to model additional
physical processes, such as dispersion, diffusion, and connected cells with
immobile water.""",

    'identifier_cells':
"""
Number of cells in the one dimensional column to be used in the advection
simulation.
""",
    'identifier_shifts':
"""
Number of times the solution in each cell will be shifted to the next higher
numbered cell.
""",

    'identifier_time_step':
"""
Identifier for time step associated with each advective shift. The
identifier is required if kinetic reactions (KINETICS data blocks) are part of
the advection simulation and optional for other advection simulations. If
-time_step is defined, then the value for time printed to the selected-output
file will be initial_time + advection_shift_number x time_step, if -time_step
is not defined, the value of time printed to the selected-output file will be
the advection shift number. Once -time_step is defined, the time step will be
used for all subsequent advection simulations until it is redefined.

The time in seconds associated with each advective shift. Kinetic reactions
will be integrated for this period of time for each advective shift
""",

    'identifier_initial_time':
"""
Identifier to set the time at the beginning of an advection simulation. The
identifier -initial_time has effect only if -time_step has been set in this or
a previous ADVECTION data block. The identifier sets the initial value of the
variable controlled by -time in SELECTED_OUTPUT data block.

Time (seconds) at the beginning of the advection simulation. Default is the
cumulative time including all preceding ADVECTION simulations for which
-time_step has been defined and all preceding TRANSPORT simulations.
""",

    'identifier_print_cells':
"""
Identifier to select cells for which results will be written to the output
file. If -print_cells is not included, results for all cells will be written
to the output file. Once -print_cells is defined, the list of cells will be
used for all subsequent advection simulations until the list is redefined.
Note the hyphen is required in -print to avoid a conflict with the keyword
PRINT.

Printing to the output file will occur only for these cell numbers. The list of
cell numbers must be delimited by spaces or tabs and may be continued on the
ucceeding line(s). A range of cell numbers may be included in the list in the
form m-n, where m and n are positive integers, m is less than n, and the two
numbers are separated by a hyphen without intervening spaces.
""",

    'identifier_print_frequency':
"""
Identifier to select shifts for which results will be written to the output
file. Once defined, the print frequency will be used for all subsequent
advection simulations until it is redefined.

Printing to the output file will occur after every print_modulus advection
shifts.
""",

    'identifier_punch_cells':
"""
Identifier to select cells for which results will be written to the
selected-output file. If -punch_cells is not included, results for all cells
will be written to the selected-output file. Once defined, the list of cells
will be used for all subsequent advection simulations until the list is
redefined.

Printing to the selected-output file will occur only for these cell numbers.
The list of cell numbers must be delimited by spaces or tabs and may be
continued on the succeeding line(s). A range of cell numbers may be included
in the list in the form m-n, where m and n are positive integers, m is less
than n, and the two numbers are separated by a hyphen without intervening
spaces.
""",

    'identifier_punch_frequency':
"""
Identifier to select shifts for which results will be written to the
selected-output file. Once defined, the punch frequency will be used for all
subsequent advection simulations until it is redefined.

Printing to the selected-output file will occur after every punch_modulus
advection shifts.
""",

    'identifier_warnings':
"""
Identifier enables or disables printing of warning messages for advection
calculations. In some cases, advection calculations could produce many
warnings that are not errors. Once it is determined that the warnings are not
due to erroneous input, disabling the warning messages can avoid generating
large output files.

If value is true, warning messages are printed to the screen and the output
file; if value is false, warning messages are not printed to the screen or the
output file. The value set with -warnings is retained in all subsequent
advection simulations until changed. Default is true, value at beginning of
run is true.
"""
}

DOC = dict((key, value.strip()) for key, value in DOC.items())

class Advection(Keyword):
    """Keyword ADVECTION.
    """
    __phreeqpy_all_docs__ = DOC
    __doc__ = DOC['keyword_ADVECTION']
    __phreeqpy_allowed_identifiers__ = ['cells', 'shifts', 'time_step',
                                        'initial_time', 'print_cells',
                                        'print_frequency', 'punch_cells',
                                        'punch_frequency', 'warnings']
    cells = Identifier('cells', ptype=PositiveInteger,
                       doc=DOC['identifier_cells'], default=0)
    shifts = Identifier('shifts', ptype=PositiveInteger,
                        doc=DOC['identifier_shifts'], default=0)
    time_step = Identifier('time_step', ptype=PositiveFloat,
                           doc=DOC['identifier_time_step'], default=0)
    initial_time = Identifier('initial_time', ptype=PositiveFloat,
                              doc=DOC['identifier_initial_time'], default=1)
    print_cells = Identifier('print_cells', ptype=CellNumberList,
                             doc=DOC['identifier_print_cells'], default=1)
    print_frequency = Identifier('print_frequency', ptype=PositiveInteger,
                                 doc=DOC['identifier_print_frequency'],
                                 default=1)
    punch_cells = Identifier('punch_cells', ptype=CellNumberList,
                             doc=DOC['identifier_punch_cells'], default=1)
    punch_frequency = Identifier('punch_frequency', ptype=PositiveInteger,
                                 doc=DOC['identifier_punch_frequency'],
                                 default=1)
    warnings = Identifier('warnings', ptype=Bool,
                          doc=DOC['identifier_warnings'], default=True)
