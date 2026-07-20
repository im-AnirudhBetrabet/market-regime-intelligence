"""
Logging formatters
"""
from __future__ import annotations
import logging

class ColoredFormatter(logging.Formatter):
    """
    Custom log formatter.
    """

    FORMAT = (
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    )

    def __init__(self) -> None:
        super().__init__(
            fmt=self.FORMAT,
            datefmt="%Y-%m-%d %H:%M:%S"
        )