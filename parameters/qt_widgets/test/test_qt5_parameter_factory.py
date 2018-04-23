# coding=utf-8
"""Test class for qt5_parameter_factory."""

import unittest

from PyQt5.QtWidgets import QApplication

from parameters.boolean_parameter import BooleanParameter
from parameters.float_parameter import FloatParameter
from parameters.qt_widgets.boolean_parameter_widget import (
    BooleanParameterWidget)
from parameters.qt_widgets.float_parameter_widget import FloatParameterWidget
from parameters.qt_widgets.qt5_parameter_factory import Qt5ParameterFactory
from parameters.qt_widgets.test.custom_parameter.point_parameter import (
    PointParameter)
from parameters.qt_widgets.test.custom_parameter. \
    point_parameter_widget import PointParameterWidget

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestQt5ParameterFactory(unittest.TestCase):
    application = QApplication([])

    def setUp(self):
        """SetUp for unit test."""
        self.boolean_parameter = BooleanParameter('1231231')
        self.boolean_parameter.name = 'Boolean'
        self.boolean_parameter.help_text = 'A boolean parameter'
        self.boolean_parameter.description = 'A test _description'
        self.boolean_parameter.is_required = True
        self.boolean_parameter.value = True

        self.float_parameter = FloatParameter()
        self.float_parameter.name = 'Float Parameter'
        self.float_parameter.is_required = True
        self.float_parameter.precision = 3
        self.float_parameter.minimum_allowed_value = 1.0
        self.float_parameter.maximum_allowed_value = 2.0
        self.float_parameter.help_text = 'Short help.'
        self.float_parameter.description = 'Long description for parameter.'
        self.float_parameter.unit = 'metres'
        self.float_parameter.value = 1.1

        self.point_parameter = PointParameter()
        self.point_parameter.name = 'Point Parameter'
        self.point_parameter.is_required = True
        self.point_parameter.help_text = 'Short help.'
        self.point_parameter.description = 'Long description for parameter.'
        self.point_parameter.value = (0, 1)

    def test_init(self):
        """Test initialize qt5 parameter factory."""
        parameters = [self.boolean_parameter, self.float_parameter]

        qt5_parameter_factory = Qt5ParameterFactory()
        widgets = []
        widget_classes = []

        for parameter in parameters:
            widget = qt5_parameter_factory.get_widget(parameter)
            widgets.append(widget)
            widget_classes.append(widget.__class__)

        expected_classes = [BooleanParameterWidget, FloatParameterWidget]
        message = 'Expected %s got %s' % (expected_classes, widget_classes)
        self.assertListEqual(widget_classes, expected_classes, message)

    def test_custom_parameter(self):
        """Test adding new custom parameter to the factory"""
        qt5_parameter_factory = Qt5ParameterFactory()
        qt5_parameter_factory.register_widget(
            PointParameter, PointParameterWidget)

        parameters = [
            self.boolean_parameter, self.float_parameter, self.point_parameter]

        widgets = []
        widget_classes = []

        for parameter in parameters:
            widget = qt5_parameter_factory.get_widget(parameter)
            widgets.append(widget)
            widget_classes.append(widget.__class__)

        expected_classes = [
            BooleanParameterWidget, FloatParameterWidget, PointParameterWidget]
        message = 'Expected %s got %s' % (expected_classes, widget_classes)
        self.assertListEqual(widget_classes, expected_classes, message)

if __name__ == '__main__':
    unittest.main()
