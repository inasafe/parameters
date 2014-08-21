# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'numeric_parameter_widget'
__date__ = '8/21/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QDoubleSpinBox, QLabel, QSizePolicy ,QWidget

from qt_widgets.generic_parameter_widget import GenericParameterWidget


class NumericParameterWidget(GenericParameterWidget):
    """Widget class for Numeric parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A NumericParameter object.
        :type parameter: NumericParameter

        """
        super(NumericParameterWidget, self).__init__(parameter, parent)

        self._input = QWidget()

        self._label_unit = QLabel(self._parameter.unit)

        # Size policy
        self._spin_box_size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)

        label_policy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Fixed)
        self._label_unit.setSizePolicy(label_policy)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._input.value()
        return self._parameter
