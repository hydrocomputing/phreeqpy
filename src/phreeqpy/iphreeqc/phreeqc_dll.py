# -*- coding: utf-8 -*-*

"""Access PHREEQC-DLL via ctypes.

This is exchangeable with the COM interface.
"""

import ctypes
import os
import sys


class IPhreeqc(object):
    """Wrapper for the IPhreeqc DLL.
    """
    # All methods in `method_mapping` are added dynamically.
    # Therefore, pylint complains.
    #pylint: disable-msg=E1101
    def __init__(self, dll_path=None):
        """Connect to DLL and create IPhreeqc.

        The optional `dll_path` takes a path to the IPhreeqc shared library.
        If not provided it tries to select an appropriate library.
        Make sure you have the right library for your operating system.
        You may download one from here:
        ftp://brrftp.cr.usgs.gov/pub/charlton/iphreeqc/

        See the PhreeqPy documentation for help on compiling a IPhreeqc shared
        library.
        """
        if not dll_path:
            if sys.platform == 'win32':
                dll_name = 'phreeqc3/IPhreeqc-3.7.3.dll'
            elif sys.platform.startswith('linux'):
                dll_name = 'phreeqc3/libiphreeqc-3.7.3.so'
            elif sys.platform == 'darwin':
                machine = os.uname()[-1]
                if machine == 'x86_64':
                    dll_name = 'phreeqc3/libiphreeqc-3.7.3.dylib'
                elif machine == 'arm64':
                    dll_name = 'phreeqc3/libiphreeqc-3.7.3-m1.dylib'
                else:
                    msg = 'Processor {machine} not suppported'.format(
                        machine=machine)
                    raise NotImplementedError(msg)
            else:
                msg = 'Platform {platform} is not supported.'.format(
                    platform=sys.platform)
                raise NotImplementedError(msg)
            dll_path = os.path.join(os.path.dirname(__file__), dll_name)
        phreeqc = ctypes.cdll.LoadLibrary(dll_path)
        c_int = ctypes.c_int
        method_mapping = [('_accumulate_line', phreeqc.AccumulateLine,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_add_error', phreeqc.AddError,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_add_error', phreeqc.AddWarning,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_clear_accumlated_lines',
                            phreeqc.ClearAccumulatedLines, [c_int], c_int),
                          ('_create_iphreeqc', phreeqc.CreateIPhreeqc,
                           [ctypes.c_void_p], c_int),
                          ('_destroy_iphreeqc', phreeqc.DestroyIPhreeqc,
                           [c_int], c_int),
                          ('_get_component', phreeqc.GetComponent,
                           [c_int, c_int], ctypes.c_char_p),
                          ('_get_component_count', phreeqc.GetComponentCount,
                           [c_int], c_int),
                          ('_get_error_string', phreeqc.GetErrorString,
                           [c_int], ctypes.c_char_p),
                          ('_get_selected_output_column_count',
                           phreeqc.GetSelectedOutputColumnCount, [c_int],
                           c_int),
                          ('_get_selected_output_row_count',
                           phreeqc.GetSelectedOutputRowCount, [c_int], c_int),
                          ('_get_value', phreeqc.GetSelectedOutputValue,
                           [c_int, c_int, c_int, ctypes.POINTER(VAR)], c_int),
                          ('_load_database', phreeqc.LoadDatabase,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_load_database_string', phreeqc.LoadDatabaseString,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_run_string', phreeqc.RunString,
                           [c_int, ctypes.c_char_p], c_int),
                          ('_set_selected_output_file_on',
                           phreeqc.SetSelectedOutputFileOn, [c_int, c_int],
                           c_int),
                           ('_set_output_file_on',
                           phreeqc.SetOutputFileOn, [c_int, c_int],
                           c_int),
                           ]
        for name, com_obj, argtypes, restype in method_mapping:
            com_obj.argtypes = argtypes
            com_obj.restype = restype
            setattr(self, name, com_obj)
        self.var = VAR()
        self.phc_error_count = 0
        self.phc_warning_count = 0
        self.phc_database_error_count = 0
        self.id_ = self.create_iphreeqc()

    @staticmethod
    def raise_ipq_error(error_code):
        """There was an error, raise an exception.
        """
        error_types = {0: 'ok', -1: 'out of memory', -2: 'bad value',
                       -3: 'invalid argument type', -4: 'invalid row',
                       -5: 'invalid_column', -6: 'invalid instance id'}
        error_type = error_types[error_code]
        if error_type:
            raise PhreeqcException(error_type)

    def raise_string_error(self, errors):
        """Raise an exception with message from IPhreeqc error.
        """
        if errors > 1:
            msg = '%s errors occured.\n' % errors
        elif errors == 1:
            msg = 'An error occured.\n'
        else:
            msg = 'Wrong error number.'
        raise Exception(msg + self.get_error_string())

    def accumulate_line(self, line):
        """Put line in input buffer.
        """
        errors = self._accumulate_line(self.id_, line.encode('utf-8'))
        if errors != 0:
            self.raise_string_error(errors)

    def add_error(self, phc_error_msg):
        """Add an error message to Phreeqc.
        """
        errors = self._add_error(self.id_, phc_error_msg.encode('utf-8'))
        if errors < 0:
            self.raise_string_error(errors)
        else:
            self.phc_error_count = errors

    def add_warning(self, phc_warn_msg):
        """Add an warning message to Phreeqc.
        """
        errors = self._add_warning(self.id_, phc_warn_msg.encode('utf-8'))
        if errors < 0:
            self.raise_string_error(errors)
        else:
            self.phc_warning_count = errors

    def clear_accumlated_lines(self):
        """Clear the input buffer.
        """
        errors = self._clear_accumlated_lines(self.id_)
        if errors != 0:
            self.raise_string_error(errors)

    @property
    def column_count(self):
        """Get number of columns in selected output.
        """
        return self._get_selected_output_column_count(self.id_)

    def create_iphreeqc(self):
        """Create a IPhreeqc object.
        """
        error_code = self._create_iphreeqc(ctypes.c_void_p())
        if error_code < 0:
            self.raise_ipq_error(error_code)
        id_ = error_code
        return id_

    def destroy_iphreeqc(self):
        """Delete the current instance of IPhreeqc.
        """
        error_code = self._destroy_iphreeqc(self.id_)
        if error_code < 0:
            self.raise_ipq_error(error_code)

    def get_component(self, index):
        """Get one component.
        """
        component = self._get_component(self.id_, index).decode('utf-8')
        if not component:
            raise IndexError('No component for index %s' % index)
        return component

    @property
    def component_count(self):
        """Return the number of components.
        """
        return self._get_component_count(self.id_)

    def get_component_list(self):
        """Return all component names.
        """
        get_component = self.get_component
        return [get_component(index) for index in range(self.component_count)]

    def get_error_string(self):
        """Retrieves the error messages.
        """
        return self._get_error_string(self.id_).decode('utf-8')

    def get_selected_output_value(self, row, col):
        """Get one value from selected output at given row and column.
        """
        error_code = self._get_value(self.id_, row, col, self.var)
        if error_code != 0:
            self.raise_ipq_error(error_code)
        type_ = self.var.type
        value = self.var.value
        if type_ == 3:
            val = value.double_value
        elif type_ == 2:
            val = value.long_value
        elif type_ == 4:
            val = value.string_value.decode('utf-8')
        elif type_ == 0:
            val = None
        if type_ == 1:
            self.raise_error(value.error_code)
        return val

    def get_selected_output_array(self):
        """Get all values from selected output.
        """
        nrows = self.row_count
        ncols = self.column_count
        results = []
        for row in range(nrows):
            result_row = []
            for col in range(ncols):
                result_row.append(self.get_selected_output_value(row, col))
            results.append(result_row)
        return results

    def get_selected_output_row(self, row):
        """Get all values for one from selected output.
        """
        if row < 0:
            row = self.row_count + row
        ncols = self.column_count
        results = []
        for col in range(ncols):
            results.append(self.get_selected_output_value(row, col))
        return results

    def get_selected_output_column(self, col):
        """Get all values for one column from selected output.
        """
        if col < 0:
            col = self.column_count + col
        nrows = self.row_count
        results = []
        for row in range(nrows):
            results.append(self.get_selected_output_value(row, col))
        return results

    def set_selected_output_file_off(self):
        """Turn on writing to selected output file.
        """
        self._set_selected_output_file_on(self.id_, 0)

    def set_selected_output_file_on(self):
        """Turn on writing to selected output file.
        """
        self._set_selected_output_file_on(self.id_, 1)

    def set_output_file_off(self):
        """Turn on writing to selected output file.
        """
        self._set_output_file_on(self.id_, 0)

    def set_output_file_on(self):
        """Turn on writing to selected output file.
        """
        self._set_output_file_on(self.id_, 1)

    def load_database(self, database_name):
        """Load a database with given file_name.
        """
        self.phc_database_error_count = self._load_database(
            self.id_, database_name.encode('utf-8'))

    def load_database_string(self, input_string):
        """Load a database from a string.
        """
        self.phc_database_error_count = self._load_database_string(
            self.id_, ctypes.c_char_p(input_string.encode('utf-8')))

    @property
    def row_count(self):
        """Get number of rows in selected output.
        """
        return self._get_selected_output_row_count(self.id_)

    def run_string(self, cmd_string):
        """Run PHREEQC input from string.
        """
        errors = self._run_string(self.id_,
                                  ctypes.c_char_p(cmd_string.encode('utf-8')))
        if errors != 0:
            self.raise_string_error(errors)


class VARUNION(ctypes.Union):
    # pylint: disable-msg=R0903
    # no methods
    """Union with types.

    See Var.h in PHREEQC source.
    """
    _fields_ = [('long_value', ctypes.c_long),
                ('double_value', ctypes.c_double),
                ('string_value', ctypes.c_char_p),
                ('error_code', ctypes.c_int)]


class VAR(ctypes.Structure):
    # pylint: disable-msg=R0903
    # no methods
    """Struct with data type and data values.

    See Var.h in PHREEQC source.
    """
    _fields_ = [('type', ctypes.c_int),
                ('value', VARUNION)]


class PhreeqcException(Exception):
    """Error in Phreeqc call.
    """
    pass
