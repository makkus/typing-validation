"""
    Runtime validation using type hints.
"""

__version__ = "0.0.1"

from .validation import validate
from .validation_failure import get_validation_failure, latest_validation_failure

# re-export all encodings and functions.
__all__ = [
    "validate",
    "get_validation_failure",
    "latest_validation_failure"
]
