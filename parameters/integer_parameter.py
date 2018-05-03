# coding=utf-8

"""Integer Parameter."""
import sys

from parameters.numeric_parameter import NumericParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class IntegerParameter(NumericParameter):
    """A subclass of numeric parameter that accepts integer only.

    .. note:: By default the min and max allowed values will be
        the platform specific largest and smallest int numbers.

    .. versionadded:: 2.2
    """

    def __init__(self, guid=None):
        """Constructor.

        :param guid: Optional unique identifier for this parameter. If none
            is specified one will be generated using python hash. This guid
            will be used when storing parameters in the registry.
        :type guid: str
        """
        super().__init__(guid)
        self.expected_type = int
        self._minimum_allowed_value = - sys.maxsize - 1
        self._maximum_allowed_value = sys.maxsize
        self._unit = ''
