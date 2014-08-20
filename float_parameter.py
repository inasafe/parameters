# coding=utf-8
"""Float Parameter."""
import sys
from numeric_parameter import NumericParameter, GenericParameter
from parameter_exceptions import ValueOutOfBounds


class FloatParameter(NumericParameter):
    """A subclass of generic parameter that accepts float only.

    .. note:: By default the min and max allowed values will be
        the platform specific largest and smallest float numbers.

    .. versionadded:: 2.2
    """

    def __init__(self, guid=None):
        """Constructor.

        :param guid: Optional unique identifier for this parameter. If none
            is specified one will be generated using python hash. This guid
            will be used when storing parameters in the registry.
        :type guid: str
        """
        super(FloatParameter, self).__init__(guid)
        self.expected_type = [float, int]  # IS:because int is subset of float
        self._minimum_allowed_value = sys.float_info.min
        self._maximum_allowed_value = sys.float_info.max
        self._unit = ''
        # precision means the number of digit after comma that are considered
        self._precision = 2

    @property
    def precision(self):
        """Property for the precision for the parameter.

        :returns: The precision of the value of the parameter.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Setter for the precision for the parameter.

        # precision means the number of digit after comma that are considered

        :param precision: The precision of the value of the parameter.
        :type precision: int

        """
        self._precision = precision

    @GenericParameter.value.setter
    def value(self, value):
        """Define the current _value for the parameter.

        .. note:: Overloads the setting in GenericParameter

        :param value: The _value of the parameter itself.
        :type value: str, bool, integer, float, list, dict

        :raises: TypeError
        """
        self._check_type(value)
        if self._minimum_allowed_value <= value <= self._maximum_allowed_value:
            self._value = value
        else:
            raise ValueOutOfBounds(
                'Value must be greater than %s and less than %s' % (
                    self._minimum_allowed_value,
                    self._maximum_allowed_value))
