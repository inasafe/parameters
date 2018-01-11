# coding=utf-8
"""Tests for string parameter."""

from unittest import TestCase

from parameters.string_parameter import StringParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestStringParameter(TestCase):
    def test_boolean(self):
        """Test a bool parameter works properly.

        ..versionadded:: 2.2

        """
        parameter = StringParameter('1231231')
        parameter.name = 'String parameter'
        parameter.help_text = 'A string parameter'
        parameter.description = 'A test description'
        parameter.is_required = True

        parameter.value = 'Yogyakarta'
        self.assertEqual('Yogyakarta', parameter.value)

        with self.assertRaises(TypeError):
            parameter.value = 1
