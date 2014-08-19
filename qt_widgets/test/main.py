# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'main'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QApplication

import sys
from boolean_parameter import BooleanParameter
from float_parameter import FloatParameter
from qt_widgets.boolean_parameter_widget import BooleanParameterWidget
from qt_widgets.float_parameter_widget import FloatParameterWidget


def main():
    """Main function"""
    app = QApplication([])
    parameter = BooleanParameter('1231231')
    parameter.name = 'Boolean'
    parameter.help_text = 'A boolean parameter'
    parameter.description = 'A test _description'
    parameter.is_required = True
    parameter.value = True

    boolean_parameter_widget = BooleanParameterWidget(parameter)
    boolean_parameter_widget.setGeometry(300, 300, 300, 150)
    boolean_parameter_widget.show()

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
    widget.setGeometry(300, 300, 300, 150)
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()