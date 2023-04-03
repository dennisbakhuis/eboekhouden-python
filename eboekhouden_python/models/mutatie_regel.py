"""Row in a Mutatie of E-boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd import SkipValue as ZeepXsdSkipValue


@dataclass
class MutatieRegel:
    """Row in a Mutatie of E-boekhouden.nl."""

    bedrag_invoer: str  # Decimal
    bedrag_exclusief_btw: str  # Decimal
    bedrag_btw: str  # Decimal
    bedrag_inclusief_btw: str  # Decimal
    btw_code: str  # String
    btw_percentage: str  # Decimal
    tegenrekening_code: str  # String
    kostenplaats_id: Optional[str] = None  # Int

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            BedragInvoer=self.bedrag_invoer,
            BedragExclBTW=self.bedrag_exclusief_btw,
            BedragBTW=self.bedrag_btw,
            BedragInclBTW=self.bedrag_inclusief_btw,
            BTWCode=self.btw_code,
            BTWPercentage=self.btw_percentage,
            TegenrekeningCode=self.tegenrekening_code,
            KostenplaatsID=self.kostenplaats_id or ZeepXsdSkipValue,
        )
