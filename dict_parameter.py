from generic_parameter import GenericParameter

class DictParameter(GenericParameter):
    """A subclass of paramter that allows the user to select from a dict.
    
    .. versionadded:: 2.2
    """
    
    def __init__(self):
        """Constructor."""
        self.set_expected_type(dict)