# coding=utf-8
"""Boolean Parameter."""
from generic_parameter import GenericParameter


class BooleanParameter(GenericParameter):
    """A subclass of generic parameter that accepts boolean only.

    .. versionadded:: 2.2
    """

    def __init__(self):
        """Constructor.
        :rtype : object
        """
        super(BooleanParameter, self).__init__()
        self.expected_type = bool
