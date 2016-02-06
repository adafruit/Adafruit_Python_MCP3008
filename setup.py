from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Adafruit_MCP3008',
	  version 			= '1.0.0',
	  author			= 'Tony DiCola',
	  author_email		= 'tdicola@adafruit.com',
	  description		= 'Python code to use the MCP3008 analog to digital converter with a Raspberry Pi or BeagleBone black.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Python_MCP3008/',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
	  install_requires	= ['Adafruit-GPIO>=0.6.5'],
	  packages 			= find_packages())
