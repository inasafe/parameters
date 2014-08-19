# coding=utf-8
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'boolean_parameter_widget'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


from PyQt4.QtGui import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox


class BooleanParameterWidget(QWidget, object):
    """Widget class for boolean parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A BooleanParameter object.
        :type parameter: BooleanParameter

        """
        QWidget.__init__(self, parent)
        self._parameter = parameter

        # create objects
        self._label = QLabel(self._parameter.name)
        self._label.setToolTip(self._parameter.help_text)
        self._input = QCheckBox()
        self._input.setChecked(self._parameter.value)
        self._description = QLabel(self._parameter.description)

        # put to input layout
        self._input_row = QHBoxLayout()
        self._input_row.addStretch(1)
        self._input_row.addWidget(self._label)
        self._input_row.addWidget(self._input)
        self._input_row.addWidget(self._description)

        # put to main layout
        self._layout = QVBoxLayout()
        self._layout.addStretch(1)
        self._layout.addLayout(self._input_row)

        self.setLayout(self._layout)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._input.isChecked()
        return self._parameter
