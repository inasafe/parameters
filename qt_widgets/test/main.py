# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'main'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout

import sys
from boolean_parameter import BooleanParameter
from float_parameter import FloatParameter
from integer_parameter import IntegerParameter
from qt_widgets.boolean_parameter_widget import BooleanParameterWidget
from qt_widgets.float_parameter_widget import FloatParameterWidget
from qt_widgets.integer_parameter_widget import IntegerParameterWidget
from qt_widgets.parameter_container import ParameterContainer


def main():
    """Main function"""
    app = QApplication([])
    boolean_parameter = BooleanParameter('1231231')
    boolean_parameter.name = 'Post processor'
    boolean_parameter.help_text = 'This is post processor parameter.'
    boolean_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to read '
        'it for one minute and you will be tired after read this description. '
        'You are the best user so far. Even better if you read this '
        'description loudly so that all of your friends will be able to hear '
        'you')
    boolean_parameter.is_required = True
    boolean_parameter.value = True

    boolean_parameter_widget = BooleanParameterWidget(boolean_parameter)

    float_parameter = FloatParameter()
    float_parameter.name = 'Flood Depth'
    float_parameter.is_required = True
    float_parameter.precision = 3
    float_parameter.minimum_allowed_value = 1.0
    float_parameter.maximum_allowed_value = 2.0
    float_parameter.help_text = 'The depth of flood.'
    float_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to read '
        'it for one minute and you will be tired after read this description. '
        'You are the best user so far. Even better if you read this '
        'description loudly so that all of your friends will be able to hear '
        'you')
    float_parameter.unit = 'metres'
    float_parameter.value = 1.12

    float_parameter_widget = FloatParameterWidget(float_parameter)

    integer_parameter = IntegerParameter()
    integer_parameter.name = 'Paper'
    integer_parameter.is_required = True
    integer_parameter.minimum_allowed_value = 1
    integer_parameter.maximum_allowed_value = 5
    integer_parameter.help_text = 'Number of paper'
    integer_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to read '
        'it for one minute and you will be tired after read this description. '
        'You are the best user so far. Even better if you read this '
        'description loudly so that all of your friends will be able to hear '
        'you')
    integer_parameter.unit = 'Sheets'
    integer_parameter.value = 3

    integer_parameter_widget = IntegerParameterWidget(integer_parameter)

    layout = QVBoxLayout()
    layout.addStretch(1)
    layout.addWidget(boolean_parameter_widget)
    layout.addWidget(float_parameter_widget)
    layout.addWidget(integer_parameter_widget)

    widget = QWidget()
    widget.setLayout(layout)

    # parameters = [boolean_parameter, float_parameter]
    # parameter_container = ParameterContainer(parameters)
    #
    # new_layout = QVBoxLayout()
    # new_layout.addWidget(parameter_container)
    widget.setLayout(layout)

    widget.setGeometry(0, 0, 500, 500)
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()