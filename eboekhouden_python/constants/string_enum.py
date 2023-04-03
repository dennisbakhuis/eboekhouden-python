"""Simple string enum class."""
from enum import Enum


class StringEnum(str, Enum):
    """String enum class."""

    def __str__(self) -> str:  # pragma: no cover
        """Return the value of the enum."""
        return self.value
