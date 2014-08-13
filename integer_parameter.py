# coding=utf-8

"""Integer Parameter."""

from generic_parameter import GenericParameter


class IntegerParameter(GenericParameter):
        """A subclass of generic parameter that accepts integer only.

        .. versionadded:: 2.2
        """

        def __init__(self):
            """Constructor.
            :rtype : object
            """
            super(IntegerParameter, self).__init__()
            self.set_expected_type(int)
            self.minimum_allowed_value = None
            self.maximum_allowed_value = None

        def set_minimum_allowed_value(self, value):
            """Define the minimum allowed _value for the parameter.

            :param value: The minimum allowed _value.
            :type value: int
            """
            self.minimum_allowed_value = value

        def set_maximum_allowed_value(self, value):
            """Define the maximum allowed _value for the parameter.

            :param value: The maximum allowed _value.
            :type value: int
            """
            self.maximum_allowed_value = value
