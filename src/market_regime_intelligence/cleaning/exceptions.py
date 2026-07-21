"""
Custom exceptions for data cleaning.
"""

class CleaningError(Exception):
    """
    Base exception for cleaning.
    """

class InvalidSchemaError(CleaningError):
    """
    Raised when required columns are missing.
    """

class InvalidOHLCError(CleaningError):
    """
    Raised when OHLC values are invalid.
    """

class CleaningWriteError(CleaningError):
    """
    Raised when cleaned data cannot be written.
    """