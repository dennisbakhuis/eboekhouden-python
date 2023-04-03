"""Including or excluding BTW type used by E-boekhouden.nl."""
from .string_enum import StringEnum


class BedrijfParticulier(StringEnum):
    """Indicator if company of private used by E-boekhouden.nl."""

    bedrijf = "B"
    particulier = "P"
