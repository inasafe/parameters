# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'qt4_parameter_factory'
__date__ = '8/19/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from qt_widgets.boolean_parameter_widget import BooleanParameterWidget
from qt_widgets.float_parameter_widget import FloatParameterWidget
from qt_widgets.integer_parameter_widget import IntegerParameterWidget


class Qt4ParameterFactory(object):
    """A factory class that will generate a widget given a parameter."""

    def __init__(self):
        """Constructor."""
        pass


    @staticmethod
    def get_widget(parameter):
        """Create parameter widget from current
        :param parameter: Parameter object.
        :type parameter: BooleanParameter, FloatParameter, IntegerParameter

        :returns: Widget of given parameter.
        :rtype: BooleanParameterWidget, FloatParameterWidget
        """
        class_name = parameter.__class__.__name__

        if class_name == 'BooleanParameter':
            return BooleanParameterWidget(parameter)
        elif class_name == 'FloatParameter':
            return FloatParameterWidget(parameter)
        elif class_name == 'IntegerParameter':
            return IntegerParameterWidget(parameter)
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
