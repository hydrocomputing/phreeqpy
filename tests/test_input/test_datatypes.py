# -*- coding: utf-8 -*-

import py.test

from phreeqpy.input import datatypes


def test_positive_integer_right():
    value = 1
    doc = 'Test text.'
    name = 'number'
    for value in [0, 1]:
        pos_int = datatypes.PositiveInteger(value, doc, name)
        assert str(pos_int) == str(value)
    assert pos_int.__doc__ == doc


def test_positive_integer_wrong():
    for value in [-1, 'a', 1.0, int(1e100)]:
                  py.test.raises(ValueError, datatypes.PositiveInteger, value,
                                 doc='', name='')


def test_positive_float_right():
    value = 1.0
    doc = 'Test text.'
    name = 'number'
    for value in [0.0, 1.0]:
        pos_float = datatypes.PositiveFloat(value, doc, name)
        assert str(pos_float) == str(value)
    assert pos_float.__doc__ == doc


def test_positive_float_wrong():
     for value in [(1, 2), 'a', -1.0]:
         py.test.raises(ValueError, datatypes.PositiveFloat, value, doc='',
                        name='')

def test_number_range_right():
    doc = 'Test text.'
    name = 'range'
    for value in ['1', '1-3', 1]:
        number_range = datatypes.NumberRange(value, doc, name)
        assert str(number_range) == str(value)
    assert number_range.__doc__ == doc


def test_number_range_wrong():
     for value in [-1, 'a', '-1', '1 -2', '', ' ', '1 2 3', '1 2 4-8 5', 1.0]:
         py.test.raises(ValueError, datatypes.NumberRange, value, doc='',
                        name='')


def test_cell_number_list_right():
    doc = 'Test text.'
    name = 'lis'
    for value in ['1', '1-3', '1 2 3', '1 2 4-8 5', '1 2 4-8 6 12-14', 1]:
        cell_number_list = datatypes.CellNumberList(value, doc, name)
        assert str(cell_number_list) == str(value)
    assert cell_number_list.__doc__ == doc


def test_cell_number_list_wrong():
     for value in [-1, 'a', '-1', '1 -2', '', ' ', 1.0]:
         py.test.raises(ValueError, datatypes.CellNumberList, value, doc='',
                        name='')


def test_bool_right():
    doc = 'Test text.'
    name = 'bool'
    for value in [True, False]:
        bool_value = datatypes.Bool(value, doc, name)
        assert str(bool_value) == str(value)
    assert bool_value.__doc__ == doc


def test_cell_bool_wrong():
     for value in [0, 1, 'a', 1.0, []]:
         py.test.raises(ValueError, datatypes.Bool, value, doc='',
                        name='')    
         
