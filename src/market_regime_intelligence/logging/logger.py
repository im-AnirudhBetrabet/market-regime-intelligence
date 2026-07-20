"""
Logging configuration.
"""

from __future__ import annotations

import logging
import sys

def configure_logging(level: str = "INFO") -> None:
    """
    Configure application logging.
    Args:
        level:
            Logging level
    """

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True
    )

def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.
    Args:
        name:
            Logger name.

    Returns:
        Logger instance.
    """
    return logging.getLogger()