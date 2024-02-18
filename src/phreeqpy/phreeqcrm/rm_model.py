"""
PhreeqcRM from Python.

Based on `phreeqcrm`
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import phreeqcrm


class BMIPhreeqcRM(phreeqcrm.BMIPhreeqcRM):
    """BMIPhreeqcRM."""

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class RMOutputVariable:
    """PhreecRM out variable."""

    def __init__(self, rm_inst, name):
        self._rm_inst = rm_inst
        self.name = name
        self._value = []


    @property
    def unit(self):
        """Unit."""
        return self._rm_inst.get_var_units(self.name)

    @property
    def value(self):
        """
        Value.

        Either scalar or 1d NumPy array.
        """
        self.name
        self._value
        self._value = self._rm_inst.get_value(self.name, self._value)
        if isinstance(self._value, list):
            self._value = np.array(self._value)
        if len(self._value) == 1:
            return self._value[0]
        return self._value

    def __repr__(self):
        return f'{self.__class__.__name__}({self._rm_inst, self.name})'

    def _repr_html_(self):
        df = pd.DataFrame(
            {'': [
                self.name,
                _make_value_repr(obj=self, names=['value'])[0],
                  self.unit]},
            index=['name', 'value', 'unit'])
        df.index.name = self.__class__.__name__
        return df._repr_html_()


class RMOutputVariables:
    """All PhreecRM out variables."""

    def __init__(self, rm_inst):
        self._rm_inst = rm_inst
        self.names = set(self._rm_inst.get_output_var_names())
        self._variables = {}

    def __getattr__(self, name):
        try:
            return self[name]
        except NameError as err:
            raise AttributeError(err.message)

    def __getitem__(self, name):
        if name not in self.names:
            msg = '\n'.join(
                [f'variable name {name} not available',
                 'see `self.names` for available names'])
            raise NameError(msg)
        return self._variables.setdefault(
            name, RMOutputVariable(self._rm_inst, name))

    def _repr_html_(self):
        names = list(self.names)
        units = [getattr(self, name).unit for name in names]

        df = pd.DataFrame(
            {'unit': units, 'value': _make_value_repr(obj=self, names=names)})
        df.index = names
        df.index.name = 'Name'
        return df._repr_html_()

    def __repr__(self):
        return f'{self.__class__.__name__}({self._rm_inst})'

class PhreeqcRMModel:

    _exclude_from_molalities = ['Charge']

    def __init__(self, yaml_file_name):
        self.yaml_file_name = yaml_file_name
        self._rm = BMIPhreeqcRM()
        self._rm.initialize(yaml_file_name)
        self.rm_output_variables = RMOutputVariables(self._rm)
        self.component_names = self._rm.GetComponents()
        assert len(self.component_names) == self._rm.get_value_ptr("ComponentCount")[0]
        self._molality_names = set(name for name in self.component_names
                                   if name not in self._exclude_from_molalities)
        self.number_of_cells = self._rm.get_value_ptr("GridCellCount")[0]
        self._molalities = {name: np.empty(self.number_of_cells)
                            for name in self._molality_names}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.yaml_file_name!r})'


    @property
    def charge(self):
        return self._rm.get_value('solution_charge_balance',
                                  self._molalities[component_name])

    @property
    def molalities(self):
        for name in self._molality_names:
            self.get_molality(name)
        return self._molalities

    def get_molality(self, component_name):
        if component_name not in self._molality_names:
            msg = '\n'.join(
                [
                    f'no such component "{component_name}"',
                    'allowed components are:',
                    ', '.join(self._molality_names),
                ]
            )
            raise NameError(msg)
        return self._rm.get_value(f'solution_total_molality_{component_name}',
                                  self._molalities[component_name])

    def update(self):
        self._rm.update()

def _make_value_repr(obj, names):
    values = []
    for name in names:
        try:
            value = getattr(obj, name).value
        except AttributeError:
            value = getattr(obj, name)
        try:
            length = len(value)
        except TypeError:
            values.append(value)
        else:
            values.append(f'array with {length = }')
    return values
