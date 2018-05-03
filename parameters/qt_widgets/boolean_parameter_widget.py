# coding=utf-8

from PyQt5.QtWidgets import QCheckBox

from parameters.qt_widgets.generic_parameter_widget import (
    GenericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class BooleanParameterWidget(GenericParameterWidget):
    """Widget class for boolean parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A BooleanParameter object.
        :type parameter: BooleanParameter

        """
        super().__init__(parameter, parent)

        # Get the parameter label and use its value as the checkbox text
        label_item = self.input_layout.itemAt(0)
        label_widget = label_item.widget()
        text = label_widget.text()

        self._check_box_input = QCheckBox(text)
        # Tooltips
        self.setToolTip('Tick here to enable ' + self._parameter.name)
        self._check_box_input.setChecked(self._parameter.value)

        self.inner_input_layout.insertWidget(0, self._check_box_input)
        self.input_layout.removeItem(label_item)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._check_box_input.isChecked()
        return self._parameter
