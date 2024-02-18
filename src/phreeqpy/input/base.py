# -*- coding: utf-8 -*-

# pylint: disable-msg=R0903
# Keyword and Identifier don't have any public methods.
# This is intended.

"""Some tests to see if we can comfortably generate PHRREQC input code
with Python.
"""

import string
import textwrap
import types

from phreeqpy.input.datatypes import DataType, NumberRange

UPPERCASE = set(string.ascii_uppercase)


def phreeqpy_help(thing=None, verbose=False):
    """Replacement for the builtin help function.

    We don't want the typical help for the keyword and
    identifier classes. Just call `__phreeqpy_help__`,
    which typically returns `__doc__`.
    """
    if thing is None:
        help_message = """
        This module provides access to all PHREEQC keywords such ADVECTION,
        SOLUTION ...
        """
        print '\n' + '#' * 70
        print textwrap.dedent(help_message).strip()
    elif isinstance(thing, Keyword):
        print '\n' + '#' * 70
        help_text = thing.__phreeqpy_all_docs__['keyword'] + '\n'
        help_text += textwrap.fill(thing.__doc__)
        if verbose:
            for name in thing.__phreeqpy_allowed_identifiers__ :
                help_text += '\n\n  ' + name + ':\n'
                text = thing.__phreeqpy_all_docs__['identifier_' + name]
                help_text += textwrap.fill(text, initial_indent='    ',
                                           subsequent_indent='    ')
        print help_text
    elif hasattr(thing, '__phreeqpy_help__'):
        print '\n' + '#' * 70
        print 'Name:\n     ', thing.__name__
        print 'Type:\n     ', thing.__class__.__name__
        print 'Help:'
        print textwrap.fill(thing.__phreeqpy_help__(),
                            initial_indent='      ',
                            subsequent_indent='      ')
        print
    else:
        help(thing)

def add_data_line(self, **line):
    data_line = self.__phreeqpy_data_definition__[0]
    clean_line = data_line.validate(line)
    self.__phreeqpy_data_lines__.append('    ' + clean_line)

class Keyword(object):
    """Base class for all keywords.

    We allow only a few specified attributes.
    """
    __phreeqpy_allowed_attr__ = ['__phreeqpy_allowed_attr__',
                                 '__phreeqpy_has_number__',
                                 '__phreeqpy_has_description__',
                                 '__phreeqpy_data_lines__',
                                 'keyword']
    __phreeqpy_allowed_identifiers__ = []
    __phreeqpy_has_number__ = False
    __phreeqpy_has_description__ = False
    __phreeqpy_data_definition__ = []
    __phreeqpy_data_lines__ = []

    def __init__(self):
        for name in self.__phreeqpy_allowed_identifiers__:
            self.__phreeqpy_allowed_attr__ .append(name)
            self.__phreeqpy_allowed_attr__ .append('_' + name)
        if self.__phreeqpy_has_number__:
            self.__phreeqpy_allowed_attr__ .append('number')
            self.number = '1'
        if self.__phreeqpy_has_description__:
            self.__phreeqpy_allowed_attr__ .append('description')
            self.description = ''
        self.keyword = self._make_keyword()
        if self.__phreeqpy_data_definition__:
            self.__phreeqpy_allowed_attr__.append('add_data_line')
            self.add_data_line = types.MethodType(add_data_line, self, Keyword)

    def __phreeqpy_help__(self):
        """Will be called by `help` replacement."""
        return self.__doc__

    def _make_keyword(self):
        """Make all upper case keyword from own class name.
        """
        class_name = self.__class__.__name__
        keyword = class_name[0]
        for letter in class_name[1:]:
            if letter in UPPERCASE:
                keyword += '_' + letter
            else:
                keyword += letter.upper()
        return keyword

    def __str__(self):
        """Build string with PHREEQC code.
        """
        code = self.keyword
        if self.__phreeqpy_has_number__:
            code += ' %s' % self.number
        if self.__phreeqpy_has_description__:
            code += (' %s' % self.description).rstrip()
        code = [code]
        for name in self.__phreeqpy_allowed_identifiers__:
            identifier =  getattr(self, name)
            if isinstance(identifier, DataType):
                code.append('    -%s %s' % (name, identifier))
        for line in self.__phreeqpy_data_lines__:
            code.append(line)
        return '\n'.join(code)

    def __setattr__(self, name, value):
        """Allow only setting of attributes in positive list.
        """
        if name not in self.__phreeqpy_allowed_attr__:
            allowed_names = '\n'.join(self.__phreeqpy_allowed_identifiers__)
            raise NameError('The identifier "%s" is not allowed.\n' % name +
                            'Only the following identifiers are allowed:\n'
                            '%s' % allowed_names)
        if name == 'number':
            NumberRange(value, '', name)
        if name == 'keyword' and hasattr(self, 'keyword'):
            raise AttributeError('Keyword cannot be changed.')
        object.__setattr__(self, name, value)


class Identifier(object):
    """Base class for all identifiers.
    """

    def __init__(self, name, ptype, doc=None, default=None):
        """Important set `initialized` to False.
        """
        self.initialized = False
        self.name = '_' + name
        self.ptype = ptype
        self.__doc__ = doc
        self.default = ptype(default, self.__doc__, self.name[1:])

    def __set__(self, instance, value):
        """Can only be called once, because we set `initialized` to True
        after first call.
        """
        if self.initialized:
            raise AttributeError('No changes allowed after initialization.')
        typed_value = self.ptype(value, self.__doc__, self.name[1:])
        setattr(instance, self.name, typed_value)
        self.initialized = True

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __phreeqpy_help__(self):
        """Will be called by `help` replacement."""
        return self.__doc__

class DataEntry(object):
    def __init__(self, name, ptype, doc, default):
        self.name = name
        self.ptype = ptype
        self.__doc__ = doc
        self.default = default
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return self.__str__()

class DataLine(object):
    def __init__(self, *entries):
        self.entries = entries
        self.make_order()

    def make_order(self):
        def flatten(entries, istuple=False):
            for entry in entries:
                if isinstance(entry, list):
                    optional.append([])
                    flatten(entry)
                elif isinstance(entry, tuple):
                    exlusive.append((entry[0].name, entry[1].name))
                    optional[-1].append((entry[0].name, entry[1].name))
                    flatten(entry, istuple=True)
                else:
                    if not istuple:
                        optional[-1].append(entry)
                    order.append(entry)
                    
        order = []
        exlusive = []
        optional = [[]]
        flatten(self.entries)
        optional = [set(entries) for entries in optional]
        number_optional = [len(entries) for entries in optional]
        print optional
        print number_optional
        cum_numbers = [number_optional[0]]
        for number in number_optional[1:]:
            cum_numbers.append(cum_numbers[-1] + number)
        print cum_numbers
        #raise
        self.order = order
        self.names = [entry.name for entry in self.order]
        self.allowed = set(self.names)
        self.required = optional[1]
        self.exlusive = exlusive
        self.optional = optional[1:]

    def validate(self, line):
        available = set(entry.name[1:] for entry in line.keys())
        missing = self.required - available
        if missing:
            robj = self.required.pop()
            aobj = available.pop()
            print aobj, robj.name
            print id(aobj), id(robj)
            raise NameError('The following names must be specifed:\n'
                            '\n'.join(missing))
        for pair in self.exlusive:
            if pair[0] in line and pair[1] in line:
                raise NameError('Only "%s" or %s" can be used at a time.'
                                % pair + ' Both found')
        for name in line:
            if name not in self.allowed:
                raise NameError('Name "%s" is not allowed' % name +
                                'Allowed are only the following names:\n' + 
                                '\n'.join(self.names))
        clean_line = []
        for entry in self.order:
            try:
                value = line[entry.name]
                typed_value = entry.ptype(value, self.__doc__, entry.name)
                clean_line.append(str(typed_value))
            except KeyError:
                pass
        return ' '.join(clean_line)

    def __str__(self):
        return str(self.entries)[1:-1]


