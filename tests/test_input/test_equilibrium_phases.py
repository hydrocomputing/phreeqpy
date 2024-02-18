# -*- coding: utf-8 -*-

import py.test

import helpers
from phreeqpy.input import keywords


def test_equilibrium_phases_header():
    code ="EQUILIBRIUM_PHASES 3-6 Define amounts of phases in assemblage"
    equi = keywords.EquilibriumPhases()
    equi.number = '3-6'
    equi.description = 'Define amounts of phases in assemblage'
    assert str(equi) == code


def test_equilibrium_phases_one_cell():
    code ="EQUILIBRIUM_PHASES 2"
    equi = keywords.EquilibriumPhases()
    equi.number = 2
    helpers.show_code(code, equi, whitespace_fill='.')
    assert str(equi) == code


def test_equilibrium_phases_all():
    code =helpers.cut_code("""
    EQUILIBRIUM_PHASES 3-6 Define amounts of phases in assemblage
        Chalcedony 0.0 0.0
        CO2(g) -3.5 1.0
        Gibbsite(c) 0.0 KAlSi3O8 1.0
        Calcite 1.0 Gypsum 1.0
        pH_Fix -5.0 HCl 10.0""")
    equi = keywords.EquilibriumPhases()
    equi.number = '3-6'
    equi.description = 'Define amounts of phases in assemblage'
    equi.add_data_line(phase_name='Chalcedony', saturation_index=0.0,
                       amount=0.0)
    equi.add_data_line(phase_name='CO2(g)', saturation_index=-3.5, amount=1.0)
    equi.add_data_line(phase_name='Gibbsite(c)',
                       alternative_formula='KAlSi3O8', saturation_index=0.0,
                       amount=1.0)
    equi.add_data_line(phase_name='Calcite', alternative_phase='Gypsum',
                       saturation_index=1.0, amount=1.0)
    equi.add_data_line(phase_name='pH_Fix',
                       alternative_formula='HCl', saturation_index=-5.0,
                       amount=10.0)
    helpers.show_code(code, equi)
    assert str(equi) == code    


def test_equilibrium_phases_wrong_name():
    equi = keywords.EquilibriumPhases()
    py.test.raises(NameError, equi.add_data_line, phase_name_aa='a')

def test_equilibrium_phases_required_missing():
    equi = keywords.EquilibriumPhases()
    py.test.raises(NameError, equi.add_data_line, amount=1.0)

def test_equilibrium_phases_exclusive():
    equi = keywords.EquilibriumPhases()
    py.test.raises(NameError, equi.add_data_line, phase_name='Gibbsite(c)',
                   alternative_formula='KAlSi3O8', saturation_index=0.0,
                   alternative_phase='Gypsum')
