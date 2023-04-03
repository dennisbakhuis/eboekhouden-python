"""Mutatie model."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd import SkipValue as ZeepXsdSkipValue

from .mutatie_regel import MutatieRegel


@dataclass
class Mutatie:
    """Mutatie model."""

    soort: str  # String
    datum: str  # String format example: "2023-01-01"
    rekening: str  # String grootboekrekening, e.g. 8000
    relatie_code: str  # String
    factuur_nummer: str  # String
    omschrijving: str  # String
    betalingstermijn: str  # String in days, e.g. 14
    inclusief_exclusief_btw: str  # String
    mutatie_regels: list[MutatieRegel]  # List of MutatieRegel
    mutatie_nummer: Optional[str] = None  # str=99999
    boekstuk: Optional[str] = None  # String
    betalingskenmerk: Optional[str] = None  # String

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            MutatieNr=self.mutatie_nummer or ZeepXsdSkipValue,
            Soort=self.soort,
            Datum=self.datum,
            Rekening=self.rekening,
            RelatieCode=self.relatie_code,
            Factuurnummer=self.factuur_nummer,
            Boekstuk=self.boekstuk or ZeepXsdSkipValue,
            Omschrijving=self.omschrijving,
            Betalingstermijn=self.betalingstermijn,
            Betalingskenmerk=self.betalingskenmerk or ZeepXsdSkipValue,
            InExBTW=self.inclusief_exclusief_btw,
            MutatieRegels=dict(cMutatieRegel=[x.export() for x in self.mutatie_regels]),
        )

    def to_string(self):
        """Return a string representation of this object."""
        regels = "----------------------\n".join([x.to_string() for x in self.mutatie_regels])
        return (
            "Mutatie:\n"
            "--------\n"
            f"Mutatienummer        : {self.mutatie_nummer}\n"
            f"Soort                : {self.soort}\n"
            f"Datum                : {self.datum}\n"
            f"Rekening             : {self.rekening}\n"
            f"RelatieCode          : {self.relatie_code}\n"
            f"Factuurnummer        : {self.factuur_nummer}\n"
            f"Omschrijving         : {self.omschrijving}\n"
            f"Betalingstermijn     : {self.betalingstermijn}\n"
            f"Inclusief/exclusief  : {self.inclusief_exclusief_btw}\n"
            f"Boekstuk             : {self.boekstuk}\n"
            f"Betalingskenmerk     : {self.betalingskenmerk}\n"
            f"Mutatieregels        : {len(self.mutatie_regels)}\n"
            "----------------------\n"
            f"{regels}"
        )
