# coding=utf-8
"""Tests for select parameter."""

from unittest import TestCase

from parameters.parameter_exceptions import ValueNotAllowedException
from parameters.select_parameter import SelectParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'

selected = 'one'

options = ['one', 'two', 'three', 'four', 'five']


class TestSelectParameter(TestCase):
    """Test For Select Parameter."""

    def setUp(self):
        self.parameter = SelectParameter()
        self.parameter.is_required = True
        self.parameter.element_type = str

        self.parameter.options_list = options
        self.parameter.value = selected

    def test_set_value(self):
        self.parameter.value = selected
        self.assertEqual(selected, self.parameter.value)

    def test_not_allowed_value(self):
        with self.assertRaises(ValueNotAllowedException):
            self.parameter.value = 1
