# coding=utf-8
"""Parameter Container."""

from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QGridLayout,
    QSizePolicy,
    QLabel,
    QFrame,
    QHBoxLayout
)

from parameters.parameter_exceptions import InvalidValidationException
from parameters.qt_widgets.qt5_parameter_factory import Qt5ParameterFactory

__copyright__ = "Copyright 2014, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class ParameterContainer(QWidget, object):
    """Container to hold Parameter Widgets."""

    def __init__(
            self,
            parameters=None,
            description_text='',
            extra_parameters=None,
            parent=None,
            vertical=True):
        """Constructor

        .. versionadded:: 2.2

        :param parameters: List of Parameter Widget
        :type parameters: list

        :param description_text: Text for description of the parameter
            container.
        :type description_text: str

        """
        super().__init__(parent)
        # attributes
        if not parameters:
            self.parameters = []
        else:
            self.parameters = parameters
        self.description_text = description_text
        self.extra_parameters = extra_parameters
        self.parent = parent
        self.validators = []
        self.validators_kwargs = []

        # UI
        if vertical:
            self.vertical_layout = QVBoxLayout()
        else:
            self.vertical_layout = QHBoxLayout()
        self.widget = QWidget()
        self.description_label = QLabel()
        self.description_label.setWordWrap(True)
        self.scroll_area = QScrollArea()
        self.group_frame = QFrame()
        self.qt5_parameter_factory = Qt5ParameterFactory()
        self.main_layout = QGridLayout()

# NOTES(IS) : These functions are commented since the architecture is not
    #  ready yet.
    # def register_widget(self, parameter, parameter_widget):
    #     """Register new custom widget.
    #
    #     :param parameter:
    #     :type parameter: GenericParameter
    #
    #     :param parameter_widget:
    #     :type parameter_widget: GenericParameterWidget
    #     """
    #     self.qt5_parameter_factory.register_widget(
    # parameter, parameter_widget)
    #
    # def remove_widget(self, parameter):
    #     """Register new custom widget.
    #
    #     :param parameter:
    #     :type parameter: GenericParameter
    #     """
    #     if parameter.__name__ in self.dict_widget.keys():
    #         self.dict_widget.pop(parameter.__name__)

    def get_parameters(self, validate=True):
        """Return list of parameters from the current state of widget.

        :param validate: If true, run validator, else no.
        :type validate: bool

        :returns: List of parameter
        :rtype: list
        """
        if validate:
            validation_result = self.validate()
            if not validation_result['valid']:
                raise InvalidValidationException(validation_result['message'])

        parameter_widgets = self.get_parameter_widgets()

        parameters = []

        for widget_item in parameter_widgets:
            parameter_widget = widget_item.widget()

            parameter = parameter_widget.get_parameter()
            parameters.append(parameter)

        # returns based on the object type of self.parameters
        if isinstance(self.parameters, list):
            return parameters
        else:
            # just return single parameter
            return parameters[0]

    def get_parameter_widgets(self):
        """Return list of parameter widgets from the current state of widget.

        :returns: List of parameter widget
        :rtype: list
        """

        parameter_widgets = [self.vertical_layout.itemAt(i) for i in range(
            self.vertical_layout.count())]

        return parameter_widgets

    def setup_ui(self, must_scroll=True):
        """Setup the UI of this parameter container.
        """
        # Vertical layout to place the parameter widgets
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)

        # Widget to hold the vertical layout
        self.widget = QWidget()
        self.widget.setLayout(self.vertical_layout)

        # Label for description
        self.description_label.setText(self.description_text)

        self.group_frame.setLineWidth(0)
        self.group_frame.setFrameStyle(QFrame.NoFrame)
        vlayout = QVBoxLayout()
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)
        self.group_frame.setLayout(vlayout)

        if must_scroll:
            vlayout.addWidget(self.scroll_area)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setWidget(self.widget)
        else:
            vlayout.addWidget(self.widget)

        # Main layout of the container
        if self.description_text:
            self.main_layout.addWidget(self.description_label)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        if not isinstance(self.parameters, list):
            parameters = [self.parameters]
        else:
            parameters = self.parameters

        if len(parameters) == 0:
            self.set_empty_parameters()
            return

        self.main_layout.addWidget(self.group_frame)

        self.qt5_parameter_factory = Qt5ParameterFactory()
        if self.extra_parameters is not None:
            for extra_parameter in self.extra_parameters:
                if (type(extra_parameter) == tuple and
                        len(extra_parameter) == 2):
                    self.qt5_parameter_factory.register_widget(
                        extra_parameter[0], extra_parameter[1])

        for parameter in parameters:
            parameter_widget = self.qt5_parameter_factory.get_widget(parameter)
            parameter_widget.setAutoFillBackground(True)
            self.vertical_layout.addWidget(parameter_widget)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def set_description(self, description):
        """Set description of the parameter container.

        :param description: A new description fot the parameter container.
        :type description: str
        """
        self.description_text = description
        self.description_label.setText(self.description_text)

    def set_empty_parameters(self):
        """Update UI if there is no parameters in the container.
        """
        new_description = self.description_text
        new_description += '\n'
        new_description += 'But, currently there is no parameters available.'
        self.description_label.setText(new_description)

    def add_validator(self, validator, **kwargs):
        """Add validator for this parameter container.

        :param validator: validator function for this parameter container.
        :type validator: function
        """
        validator.parent = self
        self.validators.append(validator)
        if kwargs:
            self.validators_kwargs.append(kwargs)
        else:
            self.validators_kwargs.append({})

    def validate(self):
        """Validate of all rule for all parameter in this container.

        :return: True if all valid, False
        :rtype: dict
        """
        for i in range(len(self.validators)):
            validator = self.validators[i]
            validator_kwargs = self.validators_kwargs[i]
            validation_result = validator(self, **validator_kwargs)
            if not validation_result['valid']:
                return validation_result

        return {
            'valid': True,
            'message': ''
        }

    def get_parameter_by_guid(self, parameter_guid):
        """Return a parameter based on its uuid

        :param parameter_guid: The parameter uuid
        :type parameter_guid: str

        :returns: The parameter or None if not exist
        :rtype: GenericParameter, None
        """
        parameters = self.get_parameters(validate=False)
        for parameter in parameters:
            if parameter.guid == parameter_guid:
                return parameter
        return None

    def get_parameter_widget_by_guid(self, parameter_guid):
        """Return a parameter widget based on its uuid

        :param parameter_guid: The parameter uuid
        :type parameter_guid: str

        :returns: The parameter widget or None if not exist
        :rtype: GenericParameterWidget, None
        """
        parameter_widgets = self.get_parameter_widgets()
        for parameter_widget in parameter_widgets:
            if (parameter_widget.widget().get_parameter().guid ==
                    parameter_guid):
                return parameter_widget.widget()
        return None
