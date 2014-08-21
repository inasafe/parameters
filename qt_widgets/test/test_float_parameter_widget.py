# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'test_float_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import unittest
from float_parameter import FloatParameter
from qt_widgets.float_parameter_widget import FloatParameterWidget

from PyQt4.QtGui import QApplication
import sys

application = QApplication(sys.argv)


class TestFloatParameterWidget(unittest.TestCase):
    def test_init(self):
        parameter = FloatParameter()
        parameter.name = 'Float Parameter'
        parameter.is_required = True
        parameter.precision = 3
        parameter.minimum_allowed_value = 1.0
        parameter.maximum_allowed_value = 2.0
        parameter.help_text = 'Short help.'
        parameter.description = 'Long description for parameter.'
        parameter.unit = 'metres'
        parameter.value = 1.12

        widget = FloatParameterWidget(parameter)

        expected_value = parameter.name
        real_value = widget._label.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        expected_value = parameter.value
        real_value = widget._input.value()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(1.5)

        expected_value = 1.5
        real_value = widget._input.value()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(1.55555)

        expected_value = 1.556
        real_value = widget._input.value()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        widget._input.setValue(7)

        expected_value = 2
        real_value = widget._input.value()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)


if __name__ == '__main__':
    unittest.main()
