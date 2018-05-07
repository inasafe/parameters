# coding=utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QListWidget,
    QAbstractItemView,
    QListWidgetItem,
    QVBoxLayout
)

from parameters.qt_widgets.generic_parameter_widget import (
    GenericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class ListParameterWidget(GenericParameterWidget):
    """Widget class for List parameter."""

    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A ListParameter object.
        :type parameter: ListParameter

        """
        super().__init__(parameter, parent)

        self._input = QListWidget()

        self._input.setSelectionMode(QAbstractItemView.MultiSelection)

        if self._parameter.maximum_item_count != \
                self._parameter.minimum_item_count:
            tool_tip = 'Select between %d and %d items' % (
                self._parameter.minimum_item_count,
                self._parameter.maximum_item_count)
        else:
            tool_tip = 'Select exactly %d items' % (
                       self._parameter.maximum_item_count)

        self._input.setToolTip(tool_tip)

        for opt in self._parameter.options_list:
            item = QListWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            item.setText(str(opt))
            self._input.addItem(item)
            if opt in self._parameter.value:
                item.setSelected(True)

        self.inner_input_layout.addWidget(self._input)

        # override self._input_layout arrangement to make the label at the top
        # reset the layout
        self.input_layout.setParent(None)
        self.help_layout.setParent(None)

        self.label.setParent(None)
        self.inner_input_layout.setParent(None)

        self.input_layout = QVBoxLayout()
        self.input_layout.setSpacing(0)

        # put element into layout
        self.input_layout.addWidget(self.label)
        self.input_layout.addLayout(self.inner_input_layout)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.help_layout)

    def raise_invalid_type_exception(self):
        message = 'Expecting element type of %s' % (
            self._parameter.element_type.__name__)
        err = ValueError(message)
        return err

    def get_parameter(self):
        """Obtain list parameter object from the current widget state.

        :returns: A ListParameter from the current state of widget

        """
        selected_value = []
        for opt in self._input.selectedItems():
            index = self._input.indexFromItem(opt)
            selected_value.append(self._parameter.options_list[index.row()])

        try:
            self._parameter.value = selected_value
        except ValueError:
            err = self.raise_invalid_type_exception()
            raise err

        return self._parameter
