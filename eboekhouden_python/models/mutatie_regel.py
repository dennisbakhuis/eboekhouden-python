"""Row in a Mutatie of E-boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd import SkipValue as ZeepXsdSkipValue

from ..constants import BtwCode, btw_codes_hoog, btw_codes_laag, btw_codes_geen


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

    @classmethod
    def from_bedrag(
        cls,
        bedrag_invoer: float,
        btw_code: BtwCode,
        tegenrekening_code: str,
    ) -> "MutatieRegel":
        """Create a MutatieRegel from amount including vat using BtwCode."""
        if btw_code in btw_codes_hoog:
            btw_percentage = 21
        elif btw_code in btw_codes_laag:
            btw_percentage = 9
        elif btw_code in btw_codes_geen:
            btw_percentage = 0
        else:
            raise ValueError(f"Invalid BTW code: {btw_code}")

        bedrag_exclusief_btw = bedrag_invoer / (1 + btw_percentage / 100)
        bedrag_btw = bedrag_invoer - bedrag_exclusief_btw

        return cls(
            bedrag_invoer=f"{bedrag_invoer:.2f}",
            bedrag_exclusief_btw=f"{bedrag_exclusief_btw:.2f}",
            bedrag_btw=f"{bedrag_btw:.2f}",
            bedrag_inclusief_btw=f"{bedrag_invoer:.2f}",
            btw_code=btw_code,
            btw_percentage=str(btw_percentage),
            tegenrekening_code=tegenrekening_code,
        )

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

    def to_string(self):
        """Return a string representation of this object."""
        return (
            "Mutatieregel:\n"
            "-------------\n"
            f"BedragInvoer         : {self.bedrag_invoer}\n"
            f"Bedrag Exclusief BTW : {self.bedrag_exclusief_btw}\n"
            f"Bedrag BTW           : {self.bedrag_btw}\n"
            f"Bedrag met BTW       : {self.bedrag_inclusief_btw}\n"
            f"Btw code             : {self.btw_code}\n"
            f"Btw percentage       : {self.btw_percentage}\n"
            f"Tegenrekening        : {self.tegenrekening_code}\n"
            f"Kostenplaats ID      : {self.kostenplaats_id}\n"
        )

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation of this object."""
        self.to_string()
