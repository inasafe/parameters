# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'generic_parameter_widget'
__date__ = '8/21/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextBrowser)


class GenericParameterWidget(QWidget, object):
    """Widget class for generic parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A Generic object.
        :type parameter: GenericParameter

        """
        QWidget.__init__(self, parent)
        self._parameter = parameter

        # Create elements
        # Label (name)
        self._label = QLabel(self._parameter.name)
        self._label.setToolTip(self._parameter.description)

        # Help text (shorter one)
        self._short_help = (
            self._parameter.help_text + ' <a href=#>Show more.</a>')
        self._long_help = (
            self._parameter.description + ' <a href=#>Show less.</a>')
        self._help = QTextBrowser()
        self._help.setText(self._short_help)
        self._help.setMinimumHeight(50)
        self._help.sourceChanged.connect(self.switch_help)
        self._help_less = True

        # Layouts
        self._main_layout = QVBoxLayout()
        self._input_layout = QHBoxLayout()
        self._help_layout = QHBoxLayout()
        # _inner_input_layout must be filled with widget in the child class
        self._inner_input_layout = QHBoxLayout()

        # Tooltips
        self.setToolTip(self._long_help)

        # Put elements into layouts
        self._input_layout.addWidget(self._label)
        self._input_layout.addLayout(self._inner_input_layout)

        self._main_layout.addLayout(self._input_layout)
        self._main_layout.addWidget(self._help)

        self.setLayout(self._main_layout)

    def get_parameter(self):
        """Interface for returning parameter object.

        This must be implemented in child class.

        :raises: NotImplementedError

        """
        raise NotImplementedError('Must be implemented in child class')

    def switch_help(self):
        """Switch help from the long one to the short one, and vice versa."""
        if self._help_less:
            self._help.setText(self._long_help)
            self._help_less = False
        else:
            self._help.setText(self._short_help)
            self._help_less = True
