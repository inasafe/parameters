from generic_parameter import GenericParameter

class ListParameter(GenericParameter):
    """A subclass of paramter that allows the user to select from a list.
    
    .. versionadded:: 2.2
    """
    
    def __init__(self):
        """Constructor."""
        self.set_expected_type(list)
        self.minimum_count = None
        self.maximum_count = None
        self.element_type = None
        
    def set_minimum_item_count(self, minimum_count):
        """Define the minimum number of item in the parameter.
        
        :param maximum_count: Minimum number of items that may be 
            selected. Defaults to 1.
        :type minimum_count: int
        """
        self.maximum_count = minimum_count


    def set_maximum_item_count(self, maximum_count):
        """Define the maximum allowed number of items that can be selected.
        
        :param maximum_count: Maximum number of items that may be selected. 
            Defaults to 1.
        :type maximum_count: int
        """
        self.maximum_count = maximum_count
    
    def count(self):
        """Obtain the number of element in the list.
        
        :returns: The number of elements.
        :rtype: int
        """
        return len(self.value)
        
    def set_element_type(element_type):
        """Define the type of the element of the list.
        
        :param element_type: Maximum number of items that may be selected. 
            Defaults to 1.
        :type element_type: ??????
        """
        self.element_type = element_type
    
    def set_value(value):
        """Define the current value for the parameter.
        
        Need to check the type of each element.
        
        :param value: The value of the parameter itself.
        :type value: str, bool, integer, float, list, dict
        """
        # Checking that the type of value is the same as the expected value
        if type(value) is not self.expected_type:
            message = (
                'The type of the value [%s] is not match with the expected '
                'type of the parameter [%s].' % (
                    str(type(value), str(self.expected_type))
            raise TypeError(message)
        
        for element in value:
            if type(element) is not self.element_type:
                message = (
                'The type of the element [%s] is not match with the expected '
                'type of the parameter [%s].' % (
                    str(type(value), str(self.element_type))
                raise TypeError(message)
        
        self.value = value
            
        