# coding=utf-8
"""QT4 Parameter Factory."""

from parameters.qt_widgets.boolean_parameter_widget import (
    BooleanParameterWidget)
from parameters.qt_widgets.dict_parameter_widget import DictParameterWidget
from parameters.qt_widgets.float_parameter_widget import FloatParameterWidget
from parameters.qt_widgets.group_parameter_widget import GroupParameterWidget
from parameters.qt_widgets.input_list_parameter_widget import (
    InputListParameterWidget)
from parameters.qt_widgets.integer_parameter_widget import (
    IntegerParameterWidget)
from parameters.qt_widgets.list_parameter_widget import ListParameterWidget
from parameters.qt_widgets.select_parameter_widget import SelectParameterWidget
from parameters.qt_widgets.string_parameter_widget import StringParameterWidget
from parameters.qt_widgets.text_parameter_widget import TextParameterWidget

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class Qt4ParameterFactory():
    """A factory class that will generate a widget given a parameter."""

    def __init__(self):
        """Constructor."""
        self.dict_widget = {
            'BooleanParameter': BooleanParameterWidget,
            'FloatParameter': FloatParameterWidget,
            'IntegerParameter': IntegerParameterWidget,
            'StringParameter': StringParameterWidget,
            'ListParameter': ListParameterWidget,
            'InputListParameter': InputListParameterWidget,
            'DictParameter': DictParameterWidget,
            'TextParameter': TextParameterWidget,
            'GroupParameter': GroupParameterWidget,
            'SelectParameter': SelectParameterWidget
        }

    def register_widget(self, parameter, parameter_widget):
        """Register new custom widget.

        :param parameter:
        :type parameter: GenericParameter

        :param parameter_widget:
        :type parameter_widget: GenericParameterWidget
        """
        self.dict_widget[parameter.__name__] = parameter_widget

    def remove_widget(self, parameter):
        """Register new custom widget.

        :param parameter:
        :type parameter: GenericParameter
        """
        if parameter.__name__ in list(self.dict_widget.keys()):
            self.dict_widget.pop(parameter.__name__)

    def get_widget(self, parameter):
        """Create parameter widget from current
        :param parameter: Parameter object.
        :type parameter: BooleanParameter, FloatParameter, IntegerParameter,
            StringParameter

        :returns: Widget of given parameter.
        :rtype: BooleanParameterWidget, FloatParameterWidget,
            IntegerParameterWidget, StringParameterWidget
        """
        class_name = parameter.__class__.__name__

        if class_name in list(self.dict_widget.keys()):
            return self.dict_widget[class_name](parameter)
        else:
            raise TypeError(class_name)

    @staticmethod
    def get_parameter(widget):
        """Obtain parameter object from parameter widget current state.

        :param widget: An object of a ParameterWidget.
        :type widget: GenericParameterWidget

        :returns: Parameter object
        :rtype: GenericParameter

        """
        return widget.get_parameter()
