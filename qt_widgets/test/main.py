# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'main'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QApplication, QWidget, QPushButton

import sys
from boolean_parameter import BooleanParameter
from qt_widgets.boolean_parameter_widget import BooleanParameterWidget


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

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()