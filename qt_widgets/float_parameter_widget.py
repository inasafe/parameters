# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'float_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QDoubleSpinBox, QLabel, QSizePolicy

from qt_widgets.generic_parameter_widget import GenericParameterWidget


class FloatParameterWidget(GenericParameterWidget):
    """Widget class for Float parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A FloatParameter object.
        :type parameter: FloatParameter

        """
        super(FloatParameterWidget, self).__init__(parameter, parent)

        self._double_spin_box_input = QDoubleSpinBox()
        self._double_spin_box_input.setDecimals(self._parameter.precision)
        self._double_spin_box_input.setValue(self._parameter.value)
        self._double_spin_box_input.setMinimum(
            self._parameter.minimum_allowed_value)
        self._double_spin_box_input.setMaximum(
            self._parameter.maximum_allowed_value)
        self._double_spin_box_input.setSingleStep(
            10 ** -self._parameter.precision)

        self._label_unit = QLabel(self._parameter.unit)

        # Size policy
        double_spin_box_size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        self._double_spin_box_input.setSizePolicy(double_spin_box_size_policy)

        label_policy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Fixed)
        self._label_unit.setSizePolicy(label_policy)

        self._inner_input_layout.addWidget(self._double_spin_box_input)
        self._inner_input_layout.addWidget(self._label_unit)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._double_spin_box_input.value()
        return self._parameter
