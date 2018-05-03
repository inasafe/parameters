# coding=utf-8
"""Boolean Parameter."""
from parameters.generic_parameter import GenericParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class BooleanParameter(GenericParameter):
    """A subclass of generic parameter that accepts boolean only.

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
        self.expected_type = bool
