# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'float_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QDoubleSpinBox, QLabel, QSizePolicy

from qt_widgets.numeric_parameter_widget import NumericParameterWidget


class FloatParameterWidget(NumericParameterWidget):
    """Widget class for Float parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A FloatParameter object.
        :type parameter: FloatParameter

        """
        super(FloatParameterWidget, self).__init__(parameter, parent)

        self._input = QDoubleSpinBox()
        self._input.setDecimals(self._parameter.precision)
        self._input.setValue(self._parameter.value)
        self._input.setMinimum(
            self._parameter.minimum_allowed_value)
        self._input.setMaximum(
            self._parameter.maximum_allowed_value)
        self._input.setSingleStep(
            10 ** -self._parameter.precision)

        self._input.setSizePolicy(self._spin_box_size_policy)

        self._inner_input_layout.addWidget(self._input)
        self._inner_input_layout.addWidget(self._label_unit)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._input.value()
        return self._parameter
