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
from qt_widgets.boolean_parameter_widget import BooleanParameterWidget
from qt_widgets.float_parameter_widget import FloatParameterWidget


def main():
    """Main function"""
    app = QApplication([])
    boolean_parameter = BooleanParameter('1231231')
    boolean_parameter.name = 'Boolean'
    boolean_parameter.help_text = 'A boolean parameter'
    boolean_parameter.description = (
        'A <b>test _description</b> that is very long so that you need to read '
        'it for one minute and you will be tired after read this description. '
        'You are the best user so far. Even better if you read this '
        'description loudly so that all of your friends will be able to hear '
        'you')
    boolean_parameter.is_required = True
    boolean_parameter.value = True

    boolean_parameter_widget = BooleanParameterWidget(boolean_parameter)
    # boolean_parameter_widget.setGeometry(300, 300, 300, 150)
    # boolean_parameter_widget.show()

    float_parameter = FloatParameter()
    float_parameter.name = 'Float Parameter'
    float_parameter.is_required = True
    float_parameter.precision = 3
    float_parameter.minimum_allowed_value = 1.0
    float_parameter.maximum_allowed_value = 2.0
    float_parameter.help_text = 'Short help.'
    float_parameter.description = 'Long description for parameter.'
    float_parameter.unit = 'metres'
    float_parameter.value = 1.12

    float_parameter_widget = FloatParameterWidget(float_parameter)
    # float_parameter_widget.setGeometry(300, 300, 300, 150)
    # float_parameter_widget.show()

    layout = QVBoxLayout()
    layout.addStretch(1)
    layout.addWidget(boolean_parameter_widget)
    layout.addWidget(float_parameter_widget)

    widget = QWidget()
    widget.setLayout(layout)

    widget.setGeometry(300, 300, 300, 300)
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()