"""
Validation exceptions
"""

class ValidationError(Exception):
    """
    Base validation exceptions
    """

class DatasetValidationError(ValidationError):
    """
    Raised when a dataset fails validation
    """