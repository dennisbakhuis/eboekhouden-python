"""Model for GetMutaties filter in e-Boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd.const import SkipValue as ZeepXsdSkipValue


@dataclass
class MutatieFilter:
    """Filter for GetMutaties in e-Boekhouden."""

    mutatie_nummer: Optional[str] = None
    mutatie_nummer_van: Optional[str] = None
    mutatie_nummer_totmet: Optional[str] = None
    factuur_nummer: Optional[str] = None
    datum_van: Optional[str] = None
    datum_totmet: Optional[str] = None

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            MutatieNr=self.mutatie_nummer or ZeepXsdSkipValue,
            MutatieNrVan=self.mutatie_nummer_van or ZeepXsdSkipValue,
            MutatieNrTm=self.mutatie_nummer_totmet or ZeepXsdSkipValue,
            Factuurnummer=self.factuur_nummer or ZeepXsdSkipValue,
            DatumVan=self.datum_van or ZeepXsdSkipValue,
            DatumTm=self.datum_totmet or ZeepXsdSkipValue,
        )

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation of this object."""
        return (
            f"MutatieFilter: {self.mutatie_nummer} -> "
            f"{self.mutatie_nummer_van} / {self.mutatie_nummer_totmet}"
            f" {self.factuur_nummer} -> {self.datum_van} / {self.datum_totmet}"
        )
