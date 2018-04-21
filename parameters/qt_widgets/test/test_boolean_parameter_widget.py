# coding=utf-8
"""Test class for boolean_parameter_widget."""

import unittest

from PyQt5.QtWidgets import QApplication

from parameters.boolean_parameter import BooleanParameter
from parameters.qt_widgets.boolean_parameter_widget import (
    BooleanParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestBooleanParameterWidget(unittest.TestCase):
    application = QApplication([])

    def test_init(self):
        parameter = BooleanParameter('1231231')
        parameter.name = 'Boolean'
        parameter.help_text = 'A boolean parameter'
        parameter.description = 'A test _description'
        parameter.is_required = True

        parameter.value = True

        widget = BooleanParameterWidget(parameter)

        expected_value = parameter.name
        real_value = widget.label.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        expected_value = parameter.value
        real_value = widget._check_box_input.isChecked()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        # change value
        widget._check_box_input.setChecked(False)

        expected_value = False
        real_value = widget._check_box_input.isChecked()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

if __name__ == '__main__':
    unittest.main()
