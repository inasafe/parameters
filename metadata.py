# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'metadata.py'
__date__ = '8/25/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''
# constants
small_number = 2 ** -53  # I think this is small enough

# units
unit_feet_depth = {
    'id': 'feet_depth',
    'name': 'feet',
    'help_text': 'Feet are an imperial unit of measure.',
    'description': (
        '<b>Feet</b> are an imperial unit of measure. There are 12 '
        'inches in 1 foot and 3 feet in 1 yard. '
        'In this case <b>feet</b> are used to describe the water depth.'),
    'constraint': 'continuous',
    'default_attribute': 'depth'  # applies to vector only
}
unit_metres_depth = {
    'id': 'metres_depth',
    'name': 'metres',
    'help_text': 'Metres are an metric unit of measure.',
    'description': (
        '<b>metres</b> are a metric unit of measure. There are 100 '
        'centimetres in 1 metre. In this case <b>metres</b> are used to '
        'describe the water depth.'),
    'constraint': 'continuous',
    'default_attribute': 'depth'  # applies to vector only
}
unit_mmi = {
    'id': 'mmi',
    'name': 'MMI',
    'help_text': 'MMI describe the intensity of ground shaking.',
    'description': (
        'The <b>Modified Mercalli Intensity (MMI)</b> scale describes '
        'the intensity of ground shaking from a earthquake based on the '
        'effects observed by people at the surface.'),
    'constraint': 'continuous',
    'default_attribute': 'mmi'  # applies to vector only
}
