"""Mutatie model."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd import SkipValue as ZeepXsdSkipValue

from .mutatie_regel import MutatieRegel
from ..constants import MutatieSoort, InExBTW


@dataclass
class Mutatie:
    """Mutatie model."""

    soort: str  # String
    datum: str  # String format example: "2023-01-01"
    rekening: str  # String grootboekrekening, e.g. 8000
    omschrijving: str  # String
    inclusief_exclusief_btw: str  # String
    mutatie_regels: list[MutatieRegel]  # List of MutatieRegel
    betalingstermijn: Optional[str] = None  # String in days, e.g. 14
    relatie_code: Optional[str] = None  # String
    factuur_nummer: Optional[str] = None  # String
    mutatie_nummer: Optional[str] = None  # str=99999
    boekstuk: Optional[str] = None  # String
    betalingskenmerk: Optional[str] = None  # String

    @classmethod
    def factuur_verstuurd(
        cls,
        datum: str,
        rekening: str,
        relatie_code: str,
        factuur_nummer: str,
        omschrijving: str,
        mutatie_regels: list[MutatieRegel],
        betalingskenmerk: Optional[str] = None,
        betalingstermijn: str = "14",
        inclusief_exclusief_btw: str = InExBTW.inclusief,
    ) -> "Mutatie":
        """Return a Mutatie instance with the correct soort."""
        return cls(
            soort=MutatieSoort.factuur_verstuurd,
            datum=datum,
            rekening=rekening,
            relatie_code=relatie_code,
            factuur_nummer=factuur_nummer,
            omschrijving=omschrijving,
            betalingstermijn=betalingstermijn,
            betalingskenmerk=betalingskenmerk,
            inclusief_exclusief_btw=inclusief_exclusief_btw,
            mutatie_regels=mutatie_regels,
        )

    @classmethod
    def geld_ontvangen(
        cls,
        datum: str,
        rekening: str,
        omschrijving: str,
        mutatie_regels: list[MutatieRegel],
        betalingskenmerk: Optional[str] = None,
        betalingstermijn: str = "14",
        inclusief_exclusief_btw: str = InExBTW.inclusief,
    ) -> "Mutatie":
        """Return a Mutatie instance with the correct soort."""
        return cls(
            soort=MutatieSoort.geld_ontvangen,
            datum=datum,
            rekening=rekening,
            omschrijving=omschrijving,
            betalingstermijn=betalingstermijn,
            betalingskenmerk=betalingskenmerk,
            inclusief_exclusief_btw=inclusief_exclusief_btw,
            mutatie_regels=mutatie_regels,
        )

    @classmethod
    def geld_uitgegeven(
        cls,
        datum: str,
        rekening: str,
        omschrijving: str,
        mutatie_regels: list[MutatieRegel],
        betalingskenmerk: Optional[str] = None,
        betalingstermijn: str = "14",
        inclusief_exclusief_btw: str = InExBTW.inclusief,
    ) -> "Mutatie":
        """Return a Mutatie instance with the correct soort."""
        return cls(
            soort=MutatieSoort.geld_uitgegeven,
            datum=datum,
            rekening=rekening,
            omschrijving=omschrijving,
            betalingstermijn=betalingstermijn,
            betalingskenmerk=betalingskenmerk,
            inclusief_exclusief_btw=inclusief_exclusief_btw,
            mutatie_regels=mutatie_regels,
        )

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            MutatieNr=self.mutatie_nummer or "99999",
            Soort=self.soort,
            Datum=self.datum,
            Rekening=self.rekening,
            RelatieCode=self.relatie_code or ZeepXsdSkipValue,
            Factuurnummer=self.factuur_nummer or ZeepXsdSkipValue,
            Boekstuk=self.boekstuk or ZeepXsdSkipValue,
            Omschrijving=self.omschrijving,
            Betalingstermijn=self.betalingstermijn,
            Betalingskenmerk=self.betalingskenmerk or ZeepXsdSkipValue,
            InExBTW=self.inclusief_exclusief_btw,
            MutatieRegels=dict(cMutatieRegel=[x.export() for x in self.mutatie_regels]),
        )

    def to_string(self):
        """Return a string representation of the object."""
        regels = "\n    ".join([x.to_string() for x in self.mutatie_regels])
        return (
            f"Mutatie(\n  {self.factuur_nummer},\n  {self.datum},\n  {self.relatie_code},\n"
            f"  {self.omschrijving},\n  [\n    {regels}\n  ],\n)"
        )
