"""OpenPosten types used by E-boekhouden.nl."""
from .string_enum import StringEnum


class OpenPostSoort(StringEnum):
    """OpenPostSoort types used by E-boekhouden.nl."""

    debiteuren = "Debiteuren"
    crediteuren = "Crediteuren"
