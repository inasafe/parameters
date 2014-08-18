# coding=utf-8
"""Float Parameter."""
import sys
from generic_parameter import GenericParameter
from parameter_exceptions import (
    InvalidMaximumError, InvalidMinimumError, ValueOutOfBounds)


class FloatParameter(GenericParameter):
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
        self.expected_type = float
        self._minimum_allowed_value = sys.float_info.min
        self._maximum_allowed_value = sys.float_info.max

    @property
    def minimum_allowed_value(self):
        """Property for the minimum allowed value for the parameter.

        :returns: The minimum allowed value.
        :rtype: float
        """
        return self._minimum_allowed_value

    @minimum_allowed_value.setter
    def minimum_allowed_value(self, value):
        """Getter for the minimum allowed value for the parameter.

        :param value: The minimum allowed value.
        :type value: float

        :raises: InvalidMinimumError, TypeError
        """
        self._check_type(value)
        # If maximum is not set, we can set minimum regardless
        if self._maximum_allowed_value is None:
            self._minimum_allowed_value = value
            return
        # Otherwise it must be less than maximum
        if value < self._maximum_allowed_value:
            self._minimum_allowed_value = value
            return

        raise InvalidMinimumError('Minimum must be less than maximum')

    @property
    def maximum_allowed_value(self):
        """Property for the maximum allowed value for the parameter.

        :returns: The maximum allowed value.
        :rtype: float
        """
        return self._maximum_allowed_value

    @maximum_allowed_value.setter
    def maximum_allowed_value(self, value):
        """Getter for the maximum allowed value for the parameter.

        :param value: The maximum allowed value.
        :type value: float

        :raises: InvalidMaximumError, TypeError
        """
        self._check_type(value)
        # If maximum is not set, we can set minimum regardless
        if self._maximum_allowed_value is None:
            self._maximum_allowed_value = value
            return
        # Otherwise it must be less than maximum
        if value > self._minimum_allowed_value:
            self._maximum_allowed_value = value
            return

        raise InvalidMaximumError('Maximum must be greater than minimum')

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
