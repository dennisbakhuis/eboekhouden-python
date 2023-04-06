"""Row in a Mutatie of E-boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional
from collections import OrderedDict

from zeep.xsd.const import SkipValue as ZeepXsdSkipValue

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
    def from_zeep(
        cls,
        zeep_mutatie_regel_object: OrderedDict,
    ) -> "MutatieRegel":
        """Create a MutatieRegel from a zeep object."""
        short = zeep_mutatie_regel_object
        return cls(
            bedrag_invoer=f"{short.get('BedragInvoer'):.2f}",
            bedrag_exclusief_btw=f"{short.get('BedragExclBTW'):.2f}",
            bedrag_btw=f"{short.get('BedragBTW'):.2f}",
            bedrag_inclusief_btw=f"{short.get('BedragInclBTW'):.2f}",
            btw_code=f"{short.get('BTWCode')}",
            btw_percentage=f"{int(short.get('BTWPercentage'))}",  # type: ignore
            tegenrekening_code=short.get("TegenrekeningCode"),  # type: ignore
            kostenplaats_id=short.get("KostenplaatsID"),
        )

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
            btw_code=str(btw_code),
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
            f"Mutatieregel({self.bedrag_invoer}, {self.btw_percentage}%, {self.tegenrekening_code})"
        )
