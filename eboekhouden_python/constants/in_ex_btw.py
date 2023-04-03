"""Including or excluding BTW type used by E-boekhouden.nl."""
from .string_enum import StringEnum


class InExBTW(StringEnum):
    """Including or excluding BTW type used by E-boekhouden.nl."""

    inclusief = "IN"  # Inclusief BTW
    exclusief = "EX"  # Exclusief BTW
