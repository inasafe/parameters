# coding=utf-8
"""Docstring for this test file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'test_integer_parameter_widget'
__date__ = '8/21/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import unittest
import sys

from PyQt4.QtGui import QApplication

from integer_parameter import IntegerParameter
from qt_widgets.integer_parameter_widget import IntegerParameterWidget


application = QApplication(sys.argv)


class TestFloatParameterWidget(unittest.TestCase):
    def test_init(self):
        parameter = IntegerParameter()
        parameter.name = 'Integer  Parameter'
        parameter.is_required = True
        parameter.minimum_allowed_value = 1
        parameter.maximum_allowed_value = 5
        parameter.help_text = 'Short help.'
        parameter.description = 'Long description for parameter.'
        parameter.unit = 'kilo'
        parameter.value = 3

        widget = IntegerParameterWidget(parameter)

        expected_value = parameter.name
        real_value = widget._label.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        expected_value = parameter.value
        real_value = widget.get_parameter().value
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(1.5)

        expected_value = 1
        real_value = widget.get_parameter().value
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(1.55555)

        expected_value = 1
        real_value = widget.get_parameter().value
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(7)

        expected_value = 5
        real_value = widget.get_parameter().value
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)


if __name__ == '__main__':
    unittest.main()
