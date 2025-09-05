"""Mutatie model."""
from dataclasses import dataclass
from typing import Optional, Any
from collections import OrderedDict

from zeep.helpers import serialize_object
from ..constants import OpenPostSoort
from zeep.xsd.const import SkipValue as ZeepXsdSkipValue


@dataclass
class OpenPost:
    """Open post model."""

    mutatie_datum: str  # String format example: "2023-01-01"
    factuur_nummer: Optional[str] = None  # String
    relatie_code: Optional[str] = None  # String
    relatie_bedrijf: Optional[str] = None  # String
    factuur_bedrag: Optional[str] = None
    bedrag_voldaan: Optional[str] = None
    bedrag_openstaand: Optional[str] = None
    soort: Optional[OpenPostSoort] = None

    @classmethod
    def from_zeep(
        cls,
        zeep_open_post_object: Any,
        soort: Optional[OpenPostSoort] = None,
    ) -> "OpenPost":  # pragma: no cover
        """Create an OpenPost object from a Zeep object."""
        serialized_open_post: OrderedDict = serialize_object(zeep_open_post_object)  # type: ignore
        return cls(
            mutatie_datum=serialized_open_post["MutDatum"].strftime("%Y-%m-%d"),
            factuur_nummer=serialized_open_post["MutFactuur"],
            relatie_code=serialized_open_post["RelCode"],
            relatie_bedrijf=serialized_open_post["RelBedrijf"],
            factuur_bedrag=serialized_open_post["Bedrag"],
            bedrag_voldaan=serialized_open_post["Voldaan"],
            bedrag_openstaand=serialized_open_post["Openstaand"],
            soort=soort,
        )

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            MutDatum=self.mutatie_datum,
            MutFactuur=self.factuur_nummer or ZeepXsdSkipValue,
            RelCode=self.relatie_code or ZeepXsdSkipValue,
            RelBedrijf=self.relatie_bedrijf or ZeepXsdSkipValue,
            Bedrag=self.factuur_bedrag or ZeepXsdSkipValue,
            Voldaan=self.bedrag_voldaan or ZeepXsdSkipValue,
            Openstaand=self.bedrag_openstaand or ZeepXsdSkipValue,
        )

    def to_string(self):
        """Return string representation of this object."""
        return f"OpenPost(factuur_nummer={self.factuur_nummer}, bedrag_voldaan={self.bedrag_voldaan}, bedrag_openstaand={self.bedrag_openstaand})"
