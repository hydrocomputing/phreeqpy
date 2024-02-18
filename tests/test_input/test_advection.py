# -*- coding: utf-8 -*-

import py.test

import helpers
from phreeqpy.input import keywords

def test_advection_all():
    code = helpers.cut_code("""
    ADVECTION
        -cells 5
        -shifts 30
        -time_step 10000000.0
        -initial_time 1.0
        -print_cells 1-3 5
        -print_frequency 5
        -punch_cells 3-5
        -punch_frequency 5
        -warnings True""")
    adv = keywords.Advection()
    adv.cells = 5
    adv.shifts = 30
    adv.time_step = 1e7
    adv.initial_time = 1.0
    adv.print_cells = '1-3 5'
    adv.warnings = True
    adv.print_frequency = 5
    adv.punch_cells = '3-5'
    adv.punch_frequency = 5
    helpers.show_code(code, adv, whitespace_fill='.')
    assert str(adv) == code


def test_advection_wrong_identifier():
    adv = keywords.Advection()
    py.test.raises(NameError, setattr, adv, 'wrong', 5)
