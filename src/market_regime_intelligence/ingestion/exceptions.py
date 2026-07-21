"""
Custom exceptions for data ingestion
"""

class IngestionError(Exception):
    """
    Base ingestion exception
    """

class DataDownloadError(IngestionError):
    """
    Raised when data download fails.
    """

class DataWriteError(IngestionError):
    """
    Raised when writing data fails
    """