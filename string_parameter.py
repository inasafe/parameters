# coding=utf-8
"""String Parameter."""

from generic_parameter import GenericParameter


class StringParameter(GenericParameter):
        """A subclass of generic parameter that accepts string only.

        .. versionadded:: 2.2
        """

        def __init__(self):
            """Constructor.
            :rtype : object
            """
            super(StringParameter, self).__init__()
            self.set_expected_type(str)
