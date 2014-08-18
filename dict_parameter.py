# coding=utf-8
"""Dictionary Parameter."""
from generic_parameter import GenericParameter


class DictParameter(GenericParameter):
    """A subclass of parameter that allows the user to select from a dict.

    .. versionadded:: 2.2
    """

    def __init__(self, guid=None):
        """Constructor.

        :param guid: Optional unique identifier for this parameter. If none
            is specified one will be generated using python hash. This guid
            will be used when storing parameters in the registry.
        :type guid: str
        """
        super(DictParameter, self).__init__(guid)
        self.expected_type = dict
