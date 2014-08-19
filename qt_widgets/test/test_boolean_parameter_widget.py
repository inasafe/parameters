# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'test_boolean_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QApplication

import unittest
import sys
from boolean_parameter import BooleanParameter
from qt_widgets.boolean_parameter_widget import BooleanParameterWidget

application = QApplication(sys.argv)


class TestBooleanParameterWidget(unittest.TestCase):
    def test_init(self):
        parameter = BooleanParameter('1231231')
        parameter.name = 'Boolean'
        parameter.help_text = 'A boolean parameter'
        parameter.description = 'A test _description'
        parameter.is_required = True

        parameter.value = True

        boolean_parameter_widget = BooleanParameterWidget(parameter)

        expected_value = parameter.name
        real_value = boolean_parameter_widget._label.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        expected_value = parameter.value
        real_value = boolean_parameter_widget._input.isChecked()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        # change value
        boolean_parameter_widget._input.setChecked(False)

        expected_value = False
        real_value = boolean_parameter_widget._input.isChecked()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

if __name__ == '__main__':
    unittest.main()

