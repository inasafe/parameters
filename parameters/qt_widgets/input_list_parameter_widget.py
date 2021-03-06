from builtins import str
# coding=utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QListWidget,
    QAbstractItemView,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidgetItem
)

from parameters.input_list_parameter import InputListParameter
from parameters.qt_widgets.generic_parameter_widget import (
    GenericParameterWidget)

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class InputListParameterWidget(GenericParameterWidget):
    """Widget class for List parameter."""

    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A ListParameter object.
        :type parameter: InputListParameter

        """
        super().__init__(parameter, parent)

        # value cache for self._parameter.value
        # copy the list so the original is unaffected
        self._value_cache = list(self._parameter.value)

        self.input = QListWidget()

        self.input.setSelectionMode(QAbstractItemView.SingleSelection)

        if self._parameter.maximum_item_count != \
                self._parameter.minimum_item_count:
            tool_tip = 'Select between %d and %d items' % (
                self._parameter.minimum_item_count,
                self._parameter.maximum_item_count)
        else:
            tool_tip = 'Select exactly %d items' % (
                self._parameter.maximum_item_count)

        self.input.setToolTip(tool_tip)

        # arrange widget

        self.insert_item_input = QLineEdit()

        vbox_layout = QVBoxLayout()
        hbox_layout = QHBoxLayout()
        self.input_add_button = QPushButton('Add')
        self.input_remove_button = QPushButton('Remove')
        # arrange line edit, add button, remove button in horizontal layout
        hbox_layout.addWidget(self.insert_item_input)
        hbox_layout.addWidget(self.input_add_button)
        hbox_layout.addWidget(self.input_remove_button)
        # arrange vertical layout
        vbox_layout.addLayout(hbox_layout)
        vbox_layout.addWidget(self.input)
        self.inner_input_layout.addLayout(vbox_layout)

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

        # connect handler
        # noinspection PyUnresolvedReferences
        self.input_add_button.clicked.connect(self.on_add_button_click)
        # noinspection PyUnresolvedReferences
        self.input_remove_button.clicked.connect(self.on_remove_button_click)
        # noinspection PyUnresolvedReferences
        self.insert_item_input.returnPressed.connect(
            self.input_add_button.click)
        # noinspection PyUnresolvedReferences
        self.input.itemChanged.connect(self.on_row_changed)

        self.refresh_list()

        # init row add error handler
        self._add_row_error_handler = None

    @property
    def add_row_error_handler(self):
        """return error handler if user mistakenly add row of unexpected type
        :return: a function handler
        :rtype: () -> None
        """
        return self._add_row_error_handler

    @add_row_error_handler.setter
    def add_row_error_handler(self, value):
        """Set error handler to handle user mistakenly add row of unexpected
        type
        """
        self._add_row_error_handler = value

    def refresh_list(self):
        self.input.clear()
        if not self._parameter.ordering == InputListParameter.NotOrdered:
            self._value_cache.sort()
        if self._parameter.ordering == InputListParameter.DescendingOrder:
            self._value_cache.reverse()
        for opt in self._value_cache:
            item = QListWidgetItem()
            item.setText(str(opt))
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.input.addItem(item)

    def on_add_button_click(self):
        try:
            value = self._parameter.element_type(
                self.insert_item_input.text())
            self._value_cache.append(value)
            self.refresh_list()
        except ValueError:
            err = self.raise_invalid_type_exception()
            if self.add_row_error_handler is not None:
                self.add_row_error_handler(err)
            else:
                raise err

    def on_remove_button_click(self):
        for opt in self.input.selectedItems():
            index = self.input.indexFromItem(opt)
            del self._value_cache[index.row()]
        self.refresh_list()

    def on_row_changed(self, item):
        try:
            index = self.input.indexFromItem(item).row()
            prev_value = self._value_cache[index]
            self._value_cache[index] = self._parameter.element_type(
                item.text())
            self.refresh_list()
        except ValueError:
            item.setText(str(prev_value))
            self.raise_invalid_type_exception()

    def raise_invalid_type_exception(self):
        message = 'Expecting element type of %s' % (
            self._parameter.element_type.__name__)
        err = ValueError(message)
        return err

    def get_parameter(self):
        """Obtain list parameter object from the current widget state.

        :returns: A ListParameter from the current state of widget

        """

        try:
            self._parameter.value = self._value_cache
        except ValueError:
            err = self.raise_invalid_type_exception()
            raise err

        return self._parameter
