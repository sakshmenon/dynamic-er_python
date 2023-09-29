from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect

class DynamicScope(abc.Mapping):                        # initializing dictionary object methods below
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):                         # Modifying getitem to raise a NameError if a key that is not in the list is referenced
        if key not in self.keys():
            raise NameError
        elif key in self.keys():
            return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def keys(self):
        return self.__dict__.keys()

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self, c = 0):
        return iter(self.__dict__)
    
def get_dynamic_re() -> DynamicScope:
    var_list = []                               # A list to hold all the local variables in the given frame
    free_var_list = []                          # A list to hold all the free variables in the given frame
    dre = DynamicScope()                        # Dictionary object to hold all the dynamically resolved variables
    frame_stack = inspect.stack()                    # A list containing frame info objects
    for i in range(1, len(frame_stack)):
        argument_names = list(frame_stack[i][0].f_code.co_varnames)          # Creates a list of argument names in a function frame
        temp_local_variables = frame_stack[i][0].f_locals.keys()             # Creates a temporary list for the local variables referenced in the function
        for k in argument_names:
            if k in frame_stack[i][0].f_locals.keys():
                break
            elif argument_names.index(k) == len(argument_names)-1:      # Raises an UnbondedLocalError if the referenced variable is referred before assignment
                raise UnboundLocalError

        free_var_list = (frame_stack[i][0].f_code.co_freevars)                   # initializing all the free variables in the given frame object
        var_list = (frame_stack[i][0].f_locals)                                  # initializing all the local variables in the given frame object
        for j in var_list:
            if (j not in free_var_list) and (j not in dre):                 # adding the variables to the dictionary object 
                dre[j] = var_list[j]
            else:
                continue
    return dre