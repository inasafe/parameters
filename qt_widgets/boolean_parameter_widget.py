# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'boolean_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


from PyQt4.QtGui import QCheckBox

from qt_widgets.generic_parameter_widget import GenericParameterWidget


class BooleanParameterWidget(GenericParameterWidget):
    """Widget class for boolean parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A BooleanParameter object.
        :type parameter: BooleanParameter

        """
        super(BooleanParameterWidget, self).__init__(parameter, parent)

        self._check_box_input = QCheckBox('Check if true')
        self._check_box_input.setChecked(self._parameter.value)

        self._inner_input_layout.addWidget(self._check_box_input)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._check_box_input.value()
        return self._parameter

