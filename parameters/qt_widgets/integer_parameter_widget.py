# coding=utf-8
"""Docstring for this file."""

from PyQt5.QtWidgets import QSpinBox

from parameters.qt_widgets.numeric_parameter_widget import (
    NumericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class IntegerParameterWidget(NumericParameterWidget):
    """Widget class for Integer parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A IntegerParameter object.
        :type parameter: IntegerParameter

        """
        super().__init__(parameter, parent)

        self._input = QSpinBox()
        self._input.setValue(self._parameter.value)
        self._input.setMinimum(self._parameter.minimum_allowed_value)
        self._input.setMaximum(self._parameter.maximum_allowed_value)
        tool_tip = 'Choose a number between %d and %d' % (
            self._parameter.minimum_allowed_value,
            self._parameter.maximum_allowed_value)
        self._input.setToolTip(tool_tip)

        self._input.setSizePolicy(self._spin_box_size_policy)

        self.inner_input_layout.addWidget(self._input)
        self.inner_input_layout.addWidget(self._unit_widget)
