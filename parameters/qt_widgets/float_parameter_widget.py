# coding=utf-8
"""Docstring for this file."""

from PyQt5.QtWidgets import QDoubleSpinBox

from parameters.qt_widgets.numeric_parameter_widget import (
    NumericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class FloatParameterWidget(NumericParameterWidget):
    """Widget class for Float parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A FloatParameter object.
        :type parameter: FloatParameter

        """
        super().__init__(parameter, parent)

        self._input = QDoubleSpinBox()
        self._input.setDecimals(self._parameter.precision)
        self._input.setMinimum(self._parameter.minimum_allowed_value)
        self._input.setMaximum(self._parameter.maximum_allowed_value)
        self._input.setValue(self._parameter.value)
        self._input.setSingleStep(
            10 ** -self._parameter.precision)
        # is it possible to use dynamic precision ?
        string_min_value = '%.*f' % (
            self._parameter.precision, self._parameter.minimum_allowed_value)
        string_max_value = '%.*f' % (
            self._parameter.precision, self._parameter.maximum_allowed_value)
        tool_tip = 'Choose a number between %s and %s' % (
            string_min_value, string_max_value)
        self._input.setToolTip(tool_tip)

        self._input.setSizePolicy(self._spin_box_size_policy)

        self.inner_input_layout.addWidget(self._input)
        self.inner_input_layout.addWidget(self._unit_widget)
