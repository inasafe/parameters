# coding=utf-8
"""Tests for boolean parameter."""
from unittest import TestCase
from boolean_parameter import BooleanParameter


class TestBooleanParameter(TestCase):

    def test_boolean(self):
        """Test a bool parameter works properly.

        .. versionadded:: 2.2

        """
        parameter = BooleanParameter()
        parameter.name = 'Boolean'
        parameter.guid = '1234567'
        #parameter.set_expected_type(bool)
        parameter.help_text = 'A boolean parameter'
        parameter.description = 'A test _description'
        parameter.is_required = True

        parameter.value = True
        self.assertEqual(True, parameter.value)


