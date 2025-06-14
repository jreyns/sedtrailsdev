"""
Custom exceptions for the Sedtrails package.
This module defines custom exceptions that can be raised during the execution of the Sedtrails package.
"""


class SedtrailsException(Exception):
    """
    Base class for all exceptions in the Sedtrails package.
    This class inherits from the built-in Exception class.
    """

    pass


class YamlParsingError(SedtrailsException):
    """
    Exception raised when there is an error parsing a YAML file.
    """

    pass


class YamlValidationError(SedtrailsException):
    """
    Exception raised when a YAML file does not conform to the expected schema.
    """

    pass


class YamlOutputError(SedtrailsException):
    """
    Exception raised when there is an error writing to a YAML file.
    """

    pass


class DateFormatError(ValueError):
    """
    Exception raised when the date string does not match the required 
    format 'YYYY-MM-DD 00:00:00'.
    """

class DurationFormatError(ValueError):
    """
    Exception raised when the duration string does not match the required format '3D 2H1M3S'.
    """
    pass    