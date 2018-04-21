# coding=utf-8
"""Test class for string_parameter_widget."""

import unittest

from PyQt5.QtWidgets import QApplication

from parameters.qt_widgets.string_parameter_widget import StringParameterWidget
from parameters.string_parameter import StringParameter

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestBooleanParameterWidget(unittest.TestCase):
    application = QApplication([])

    def test_init(self):
        string_parameter = StringParameter('28082014')
        string_parameter.name = 'Province Name'
        string_parameter.help_text = 'Name of province.'
        string_parameter.description = (
            'A <b>test _description</b> that is very long so that you need to '
            'read it for one minute and you will be tired after read this '
            'description. You are the best user so far. Even better if you '
            'read this description loudly so that all of your friends will '
            'be able to hear you')
        string_parameter.is_required = True
        string_parameter.value = 'Daerah Istimewa Yogyakarta'

        widget = StringParameterWidget(string_parameter)

        expected_value = string_parameter.name
        real_value = widget.label.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        expected_value = string_parameter.value
        real_value = widget._line_edit_input.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

        # change value
        widget._line_edit_input.setText('Nusa Tenggara Barat')

        expected_value = 'Nusa Tenggara Barat'
        real_value = widget._line_edit_input.text()
        message = 'Expected %s get %s' % (expected_value, real_value)
        self.assertEqual(expected_value, real_value, message)

if __name__ == '__main__':
    unittest.main()
