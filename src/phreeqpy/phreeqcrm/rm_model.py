"""
PhreeqcRM from Python.

Based on `phreeqcrm`
"""

import numpy as np
import pandas as pd

import phreeqcrm


class BMIPhreeqcRM(phreeqcrm.BMIPhreeqcRM):
    """BMIPhreeqcRM."""

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class RMVariable:
    """PhreecRM variable."""

    def __init__(
            self,
            rm_inst,
            name,
            is_input=False,
            is_output=False,
            is_read_only=False,
            is_pointable=False,
            is_in_only=False,
            ):
        self._rm_inst = rm_inst
        self.name = name
        self.is_input = is_input
        self.is_output = is_output
        self.is_read_only = is_read_only
        self.is_pointable = is_pointable
        self._is_in_only = is_in_only
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
        if self._is_in_only:
            return None
        if self.is_pointable:
            self._value = self._rm_inst.get_value_ptr(self.name)
        else:
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
                  self.unit,
                  self.is_input,
                  self.is_output,
                  self.is_read_only,
                  self.is_pointable,
                  ]},
            index=['name', 'value', 'unit', 'is_input', 'is_output',
                   'is_read_only', 'is_pointable'])
        df.index.name = self.__class__.__name__
        return df._repr_html_()


class RMVariables:
    """All PhreecRMvariables."""

    def __init__(self, rm_inst):
        self._rm_inst = rm_inst
        self._input_var_names = set(self._rm_inst.get_input_var_names())
        self._output_var_names = set(self._rm_inst.get_output_var_names())
        self._readonly_var_names = set(self._rm_inst.get_readonly_var_names())
        self._pointable_var_names = set(self._rm_inst.get_pointable_var_names())
        self._in_only_names = self._input_var_names - self._output_var_names
        self.names = (
            self._input_var_names |
            self._output_var_names |
            self._readonly_var_names |
            self._pointable_var_names
            )
        self._variables = {}

    def __getattr__(self, name):
        try:
            return self[name]
        except NameError as err:
            raise AttributeError(err.args[0])

    def __getitem__(self, name):
        if name not in self.names:
            msg = '\n'.join(
                [f'variable name {name} not available',
                 'see `self.names` for available names'])
            raise NameError(msg)
        variable = RMVariable(
            self._rm_inst,
            name,
            is_input=name in self._input_var_names,
            is_output=name in self._output_var_names,
            is_read_only=name in self._readonly_var_names,
            is_pointable=name in self._pointable_var_names,
            is_in_only=name in self._in_only_names,
            )
        return self._variables.setdefault(name, variable)

    def _repr_html_(self):
        names = sorted(self.names)
        objects = [getattr(self, name) for name in names]
        df = pd.DataFrame(
            {
                'unit': [obj.unit for obj in objects],
                'value': _make_value_repr(obj=self, names=names),
                'is_input': [obj.is_input for obj in objects],
                'is_output': [obj.is_output for obj in objects],
                'is_read_only': [obj.is_read_only for obj in objects],
                'is_pointable': [obj.is_pointable for obj in objects],
            }
        )
        df.index = names
        df.index.name = 'Name'
        return df._repr_html_()

    def __repr__(self):
        return f'{self.__class__.__name__}({self._rm_inst})'

class Concentrations:
    """All concentrations."""

    def __init__(self, model):
        self._model = model
        self.names = self._model.component_names
        self.values_1d = self._model.rm_variables['Concentrations'].value
        self.values_2d = self.values_1d.reshape(
            len(self._model.component_names), self._model.number_of_cells)
        self._indices = {name: index for index, name in enumerate(self.names)}

    def __getitem__(self, name):
        return self.values_2d[self._indices[name]]

    def __setitem__(self, name, values):
        assert self[name].shape == values.shape
        self.values_2d[self._indices[name]] = values

    def to_dataframe(self):
        """Concentrations."""
        return pd.DataFrame(
            data=self.values_2d.T,
            columns=self._model.component_names)

    def _repr_html_(self):
        return self.to_dataframe()._repr_html_()


class PhreeqcRMModel:
    """Wrapper around BMIPhreeqcRM."""

    _exclude_from_molalities = ['Charge']

    def __init__(self, yaml_file_name, auto_update=True):
        self.yaml_file_name = yaml_file_name
        self._rm = BMIPhreeqcRM()
        self._rm.initialize(yaml_file_name)
        self.rm_variables = RMVariables(self._rm)
        self.component_names = self._rm.GetComponents()
        assert len(self.component_names) == self._rm.get_value_ptr("ComponentCount")[0]
        self._molality_names = set(name for name in self.component_names
                                   if name not in self._exclude_from_molalities)
        self.number_of_cells = self._rm.get_value_ptr("GridCellCount")[0]
        self._molalities = {name: np.empty(self.number_of_cells)
                            for name in self._molality_names}
        self.concentrations = Concentrations(self)
        if auto_update:
            self.update()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.yaml_file_name!r})'

    @property
    def molalities(self):
        """All molalities as pandas DataFrame."""
        for name in self._molality_names:
            self.get_molality(name)
        return pd.DataFrame(self._molalities)

    def get_molality(self, component_name):
        """Get one molality."""
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
        """Run one time step."""
        self._rm.update()

    def write_conc_back(self):
        """Write modified concentration back."""
        self._rm.set_value("Concentrations", self.concentrations.values_1d)


def _make_value_repr(obj, names):
    values = []
    for name in names:
        try:
            value = getattr(obj, name).value
        except AttributeError:
            value = getattr(obj, name)
        if value is None:
            values.append(value)
        elif len(value.shape) == 0:
            values.append(value)
        else:
            values.append(f'{value.shape}, {value.dtype}')
    return values
