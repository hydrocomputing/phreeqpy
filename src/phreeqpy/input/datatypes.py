# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# All datatypes don't have any public methods.

"""Phreeqc datatypes.

These types are
"""


class DataType(object):
    """Parent class for all datatypes
    """

    def __init__(self, doc, name):
        object.__setattr__(self, 'initialized', False)
        self.__doc__ = doc
        self.__name__ = name
        self.value = None
        self.initialized = False

    def __str__(self):
        return str(self.value)

    def __phreeqpy_help__(self):
        return self.__doc__

    def __setattr__(self, name, value):
        if self.initialized:
            raise AttributeError('No changes allowed after initialization.')
        object.__setattr__(self, name, value)


class PositiveInteger(DataType):
    """Make sure value is a positive integer.
    """

    def __init__(self, value, doc, name):
        super(PositiveInteger, self).__init__(doc, name)
        if not isinstance(value, int) or value < 0:
            raise ValueError('Excpected positive integer for "%s". %s found.'
                             % (name, value))
        self.value = value
        self.initialized = True


class PositiveFloat(DataType):
    """Make sure value is a positive float.
    """

    def __init__(self, value, doc, name):
        super(PositiveFloat, self).__init__(doc, name)
        do_raise = False
        try:
            value = float(value)
        except TypeError:
            do_raise = True
        if do_raise or value < 0:
            raise ValueError('Excpected positive float for %s. %s found.'
                             % (name, value))
        self.value = value
        self.initialized = True

class Float(DataType):
    """Make sure value is a positive float.
    """

    def __init__(self, value, doc, name):
        super(Float, self).__init__(doc, name)
        if not isinstance(value, float):
            raise ValueError('Excpected positive float for %s. %s found.'
                             % (name, value))
        self.value = value
        self.initialized = True
        


class NumberRange(DataType):
    """Make sure we got a range of numbers.
    """

    def __init__(self, value, doc, name):
        super(NumberRange, self).__init__(doc, name)
        msg = ('Only a single positive integer or a string with a single'
               'positive integer or a string with a range in the form "3-6" is'
               'allowed. Got %s.' % value)
        value = str(value)
        number_range = value.split()
        if len(number_range) !=1:
            raise ValueError(msg)
        try:
            numbers = value.split('-')
        except AttributeError:
            raise ValueError(msg)
        split_numbers = [int(number) for number in numbers]
        if len(split_numbers) > 1:
            start = int(split_numbers[0])
            end = int(split_numbers[1])
            if start >= end:
                raise ValueError(('Start value %d must be smaller than end'
                                  'value %d for %s.') % (start, end, name))
        self.value = value
        self.initialized = True


class CellNumberList(DataType):
    """Make sure we got a lis of numbers and ranges.
    """

    def __init__(self, value, doc, name):
        super(CellNumberList, self).__init__(doc, name)
        msg = ('Only a single positive integer or a string with a list of'
               'positive integers or a string with a list of ranges in the'
               'form "3-6 9-12" is allowed. Got %s.' % value)
        value = str(value)
        numbers = value.split()
        if len(numbers) < 1:
            raise ValueError(msg)
        [NumberRange(number, doc, name) for number in numbers]
        self.value = value
        self.initialized = True


class Bool(DataType):
    """Make sure we got True or False.
    """

    def __init__(self, value, doc, name):
        super(Bool, self).__init__(doc, name)
        allowed = ['True', 'False']
        if str(value) not in allowed:
            raise ValueError('%s must be either True or False' % name)
        self.value = value
        self.initialized = True

class String(DataType):
    """Make sure we got a string.
    """

    def __init__(self, value, doc, name):
        super(String, self).__init__(doc, name)
        self.value = str(value)
        self.initialized = True
