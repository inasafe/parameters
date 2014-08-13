from generic_parameter import GenericParameter

class IntegerParameter(GenericParameter)):
        """A subclass of generic parameter that accepts integer only.
        
        .. versionadded:: 2.2
        """
        
        def __init__(self):
            """Constructor."""
            self.set_expected_type(int)
            self.minimum_allowed_value = None
            self.maximum_allowed_value = None
            
        def set_minimum_allowed_value(self, value):
            """Define the minimum allowed value for the parameter.
            
            :param value: The minimum allowed value.
            :type value: int
            """
            self.minimum_allowed_value = value
            
        def set_maximum_allowed_value(self, value):
            """Define the maximum allowed value for the parameter.
    
            :param value: The maximum allowed value.
            :type value: int
            """
            self.maximum_allowed_value = value
        