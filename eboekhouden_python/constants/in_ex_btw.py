"""Including or excluding BTW type used by E-boekhouden.nl."""
from enum import Enum


class InExBTW(Enum):
    """Including or excluding BTW type used by E-boekhouden.nl."""

    inclusief = "IN"  # Inclusief BTW
    exclusief = "EX"  # Exclusief BTW
