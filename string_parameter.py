from generic_parameter import GenericParameter

class StringParameter(GenericParameter)):
        """A subclass of generic parameter that accepts string only.
        
        .. versionadded:: 2.2
        """
        
        def __init__(self):
            """Constructor."""
            self.set_expected_type(str)