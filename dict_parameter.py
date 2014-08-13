# coding=utf-8
"""Dictionary Parameter."""
from generic_parameter import GenericParameter


class DictParameter(GenericParameter):
    """A subclass of parameter that allows the user to select from a dict.

    .. versionadded:: 2.2
    """

    def __init__(self):
        """Constructor.
        :rtype : object
        """
        super(DictParameter, self).__init__()
        self.set_expected_type(dict)
