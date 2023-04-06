from zeep.xsd.const import SkipValue as ZeepXsdSkipValue

from eboekhouden_python.models import Mutatie, MutatieRegel
from eboekhouden_python.constants import MutatieSoort, InExBTW


mutatie_regels = [
    MutatieRegel(
        bedrag_invoer="1.0",
        bedrag_exclusief_btw="1.0",
        bedrag_btw="1.0",
        bedrag_inclusief_btw="1.0",
        btw_code="1",
        btw_percentage="1.0",
        tegenrekening_code="1",
        kostenplaats_id="1",
    )
]


def test_mutatie_partially_filled():
    """Test Mutatie."""
    mutatie = Mutatie(
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer="1",
        omschrijving="1",
        betalingstermijn="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=mutatie_regels,
    )
    assert mutatie.export() == {
        "MutatieNr": "99999",
        "Soort": "1",
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": "1",
        "Factuurnummer": "1",
        "Boekstuk": ZeepXsdSkipValue,
        "Omschrijving": "1",
        "Betalingstermijn": "1",
        "Betalingskenmerk": ZeepXsdSkipValue,
        "InExBTW": "1",
        "MutatieRegels": {
            "cMutatieRegel": [
                {
                    "BedragInvoer": "1.0",
                    "BedragExclBTW": "1.0",
                    "BedragBTW": "1.0",
                    "BedragInclBTW": "1.0",
                    "BTWCode": "1",
                    "BTWPercentage": "1.0",
                    "TegenrekeningCode": "1",
                    "KostenplaatsID": "1",
                }
            ]
        },
    }


def test_mutatie_fully_filled():
    """Test Mutatie."""
    mutatie = Mutatie(
        mutatie_nummer="1",
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer="1",
        boekstuk="1",
        omschrijving="1",
        betalingstermijn="1",
        betalingskenmerk="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=mutatie_regels,
    )
    assert mutatie.export() == {
        "MutatieNr": "1",
        "Soort": "1",
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": "1",
        "Factuurnummer": "1",
        "Boekstuk": "1",
        "Omschrijving": "1",
        "Betalingstermijn": "1",
        "Betalingskenmerk": "1",
        "InExBTW": "1",
        "MutatieRegels": {
            "cMutatieRegel": [
                {
                    "BedragInvoer": "1.0",
                    "BedragExclBTW": "1.0",
                    "BedragBTW": "1.0",
                    "BedragInclBTW": "1.0",
                    "BTWCode": "1",
                    "BTWPercentage": "1.0",
                    "TegenrekeningCode": "1",
                    "KostenplaatsID": "1",
                }
            ]
        },
    }


def test_mutatie_factuur_versturen():
    """Test mutatie.facuur_versturen."""
    mutatie = Mutatie.factuur_verstuurd(
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer="1",
        omschrijving="1",
        betalingstermijn="1",
        betalingskenmerk="1",
        mutatie_regels=mutatie_regels,
    )
    assert mutatie.export() == {
        "MutatieNr": "99999",
        "Soort": MutatieSoort.factuur_verstuurd,
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": "1",
        "Factuurnummer": "1",
        "Boekstuk": ZeepXsdSkipValue,
        "Omschrijving": "1",
        "Betalingstermijn": "1",
        "Betalingskenmerk": "1",
        "InExBTW": InExBTW.inclusief,
        "MutatieRegels": {
            "cMutatieRegel": [
                {
                    "BedragInvoer": "1.0",
                    "BedragExclBTW": "1.0",
                    "BedragBTW": "1.0",
                    "BedragInclBTW": "1.0",
                    "BTWCode": "1",
                    "BTWPercentage": "1.0",
                    "TegenrekeningCode": "1",
                    "KostenplaatsID": "1",
                }
            ]
        },
    }


def test_mutatie_geld_ontvangen():
    """Test mutatie.geld_ontvangen."""
    mutatie = Mutatie.geld_ontvangen(
        datum="2020-01-01",
        rekening="1",
        omschrijving="1",
        mutatie_regels=[],
    )
    assert mutatie.export() == {
        "MutatieNr": "99999",
        "Soort": MutatieSoort.geld_ontvangen,
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": ZeepXsdSkipValue,
        "Factuurnummer": ZeepXsdSkipValue,
        "Boekstuk": ZeepXsdSkipValue,
        "Omschrijving": "1",
        "Betalingstermijn": "14",
        "Betalingskenmerk": ZeepXsdSkipValue,
        "InExBTW": InExBTW.inclusief,
        "MutatieRegels": {"cMutatieRegel": []},
    }


def test_mutatie_geld_uitgegeven():
    """Test mutatie.geld_ontvangen."""
    mutatie = Mutatie.geld_uitgegeven(
        datum="2020-01-01",
        rekening="1",
        omschrijving="1",
        mutatie_regels=[],
    )
    assert mutatie.export() == {
        "MutatieNr": "99999",
        "Soort": MutatieSoort.geld_uitgegeven,
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": ZeepXsdSkipValue,
        "Factuurnummer": ZeepXsdSkipValue,
        "Boekstuk": ZeepXsdSkipValue,
        "Omschrijving": "1",
        "Betalingstermijn": "14",
        "Betalingskenmerk": ZeepXsdSkipValue,
        "InExBTW": InExBTW.inclusief,
        "MutatieRegels": {"cMutatieRegel": []},
    }


def test_mutatie_to_string():
    """Test MutatieRegel."""
    mutatie = Mutatie(
        mutatie_nummer="1",
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer="1",
        boekstuk="1",
        omschrijving="1",
        betalingstermijn="1",
        betalingskenmerk="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=mutatie_regels,
    )

    assert (
        mutatie.to_string()
        == """Mutatie(
  1,
  2020-01-01,
  1,
  1,
  [
    Mutatieregel(1.0, 1.0%, 1)
  ],
)"""
    )
