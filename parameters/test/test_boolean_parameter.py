# coding=utf-8
"""Tests for boolean parameter."""
from unittest import TestCase

from parameters.boolean_parameter import BooleanParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestBooleanParameter(TestCase):

    def test_boolean(self):
        """Test a bool parameter works properly.

        .. versionadded:: 2.2

        """
        parameter = BooleanParameter('1231231')
        parameter.name = 'Boolean'
        parameter.help_text = 'A boolean parameter'
        parameter.description = 'A test _description'
        parameter.is_required = True

        parameter.value = True
        self.assertEqual(True, parameter.value)

        with self.assertRaises(TypeError):
            parameter.value = 'Test'
