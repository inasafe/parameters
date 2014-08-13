# coding=utf-8
"""Generic Parameter."""


class GenericParameter(object):
    """A generic base class for all parameters."""

    def __init__(self):
        """Constructor."""
        self.guid = None
        self.name = None
        self.expected_type = None
        self.required = None
        self.help_text = None
        self.description = None
        self.value = None

    def set_guid(self, guid):
        """Assign a unique identifier to the parameter instance.

        :param guid: A globally unique identified (never translated).
        :type guid: str

        Perhaps it should set the guid itself?
        """
        self.guid = guid

    def set_name(self, name):
        """Set the name for the parameter.

        :param name: The name for the parameters. This will be used in the UI,
            and can be translated)
        :type name: str
        """
        self.name = name

    def set_expected_type(self, expected_type):
        """Define what type of input is required.

        :param expected_type: ?????
        :type expected_type: ????

        """
        # TODO some validation here...
        # I think validation should be in set_value
        self.expected_type = expected_type


    def set_is_required(self, required):
        """Define if this is a required parameter or not.

        :param required: A required to indicate if a parameter is required.
        :type required: bool
        """
        self.is_required = required

    def set_help_text(self, help_text):
        """Define the help help_text for this parameter.

        :param help_text: A short (i.e. one line) explanation of the parameter.
        :type help_text: str
        """
        self.help_text = help_text

    def set_description(self, description):
        """Define the description for this parameter.

        :param description: A detailed description of the parameter
        :type description: str
        """
        self.description = description

    def set_value(self, value):
        """Define the current value for the parameter.

        :param value: The value of the parameter itself.
        :type value: str, bool, integer, float, list, dict
        """
        # Checking that the type of value is the same as the expected value
        if type(value) is not self.expected_type:
            message = (
                'The type of the value [%s] does match with the expected '
                'type of the parameter [%s].' % (
                    str(type(value), str(self.expected_type))))
            raise TypeError(message)

        self.value = value
