# coding=utf-8
"""Tests for dict parameter."""

from unittest import TestCase
from dict_parameter import DictParameter


class TestDictParameter(TestCase):
    """Test for dict parameter."""

    def test_dict(self):
        """Test a bool parameter works properly.

        .. versionadded:: 2.2

        """
        parameter = DictParameter(guid='1232141')
        parameter.name = 'Dict'
        #parameter.set_expected_type(bool)
        parameter.help_text = 'A dict parameter'
        parameter.description = 'A test _description'
        parameter.is_required = True

        parameter.value = {'foo': True, 'bar': False}
        self.assertEqual(True, parameter.value['foo'])

        with self.assertRaises(TypeError):
            parameter.value = 'Test'
