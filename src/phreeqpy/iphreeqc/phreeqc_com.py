"""New Interface for PHREEQC-COM-Server.

Make it exchangeable with ctypes interface.
"""

from win32com.client import Dispatch


class IPhreeqc(object):
    """Wrapper for IPhreeqc COM server.

    Provides the same API as phreeqc_dll
    """

    def __init__(self):
        """Connect with COM server.
        """
        phreeqc = Dispatch('IPhreeqcCOM.Object')
        self.phreeqc = phreeqc
        method_mapping = [('load_database', phreeqc.LoadDatabase,
                            'Load a database with given file_name.'),
                          ('run_string', phreeqc.RunString,
                            'Run PHREEQC input from string.'),
                          ('get_selected_output_value',
                           phreeqc.GetSelectedOutputValue,
                          'Get one value from selected output at given row and'
                           ' column.'),
                          ('get_selected_output_array',
                           phreeqc.GetSelectedOutputArray,
                           'Get all values from selected output.'),
                          ('get_component_list', phreeqc.GetComponentList,
                          'Return all component names.')]
        for name, com_obj, doc in method_mapping:
            setattr(self, name, com_obj)

    @property
    def row_count(self):
        """Get number of rows in selected output.
        """
        return self.phreeqc.RowCount()

    @property
    def column_count(self):
        """Get number of columns in selected output.
        """
        return self.phreeqc.ColumnCount()
