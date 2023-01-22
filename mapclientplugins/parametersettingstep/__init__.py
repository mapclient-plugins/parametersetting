'''
MAP Client Plugin
'''

__version__ = '0.1.2'
__author__ = 'Hugh Sorby'
__stepname__ = 'Parameter Setting'
__location__ = 'https://github.com/mapclient-plugins/parametersetting/archive/v0.1.1.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.parametersettingstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
