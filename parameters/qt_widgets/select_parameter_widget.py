# coding=utf-8
"""Select Parameter Widget"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox

from parameters.qt_widgets.generic_parameter_widget import (
    GenericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class SelectParameterWidget(GenericParameterWidget):
    """Widget class for List parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        :param parameter: A ListParameter object.
        :type parameter: ListParameter

        """
        super().__init__(parameter, parent)

        self.input = QComboBox()

        index = -1
        current_index = -1
        for opt in self._parameter.options_list:
            index += 1
            if opt == self._parameter.value:
                current_index = index
            self.input.addItem(opt)
            self.input.setItemData(index, opt, Qt.UserRole)

        self.input.setCurrentIndex(current_index)

        self.inner_input_layout.addWidget(self.input)

    def raise_invalid_type_exception(self):
        message = 'Expecting element type of %s' % (
            self._parameter.element_type.__name__)
        err = ValueError(message)
        return err

    def get_parameter(self):
        """Obtain list parameter object from the current widget state.

        :returns: A ListParameter from the current state of widget

        """
        current_index = self.input.currentIndex()
        selected_value = self.input.itemData(current_index, Qt.UserRole)
        if hasattr(selected_value, 'toPyObject'):
            selected_value = selected_value.toPyObject()

        try:
            self._parameter.value = selected_value
        except ValueError:
            err = self.raise_invalid_type_exception()
            raise err

        return self._parameter

    def set_choice(self, choice):
        """Set choice value by item's string.

        :param choice: The choice.
        :type choice: str

        :returns: True if success, else False.
        :rtype: bool
        """
        # Find index of choice
        choice_index = self._parameter.options_list.index(choice)
        if choice_index < 0:
            return False
        else:
            self.input.setCurrentIndex(choice_index)
            return True
