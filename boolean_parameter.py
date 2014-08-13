from generic_parameter import GenericParameter

class BooleanParameter(GenericParameter)):
        """A subclass of generic parameter that accepts boolean only.
        
        .. versionadded:: 2.2
        """
        
        def __init__(self):
            """Constructor."""
            self.set_expected_type(bool)
            