from zeep.xsd import SkipValue as ZeepXsdSkipValue

from eboekhouden_python.models import Mutatie, MutatieRegel


def test_mutatie_partially_filled():
    """Test Mutatie."""
    mutatie = Mutatie(
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer=1,
        omschrijving="1",
        betalingstermijn="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=[
            MutatieRegel(
                bedrag_invoer=1.0,
                bedrag_exclusief_btw=1.0,
                bedrag_btw=1.0,
                bedrag_inclusief_btw=1.0,
                btw_code="1",
                btw_percentage=1.0,
                tegenrekening_code="1",
                kostenplaats_id=1,
            )
        ],
    )
    assert mutatie.export() == {
        "MutatieNr": ZeepXsdSkipValue,
        "Soort": "1",
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": "1",
        "Factuurnummer": 1,
        "Boekstuk": ZeepXsdSkipValue,
        "Omschrijving": "1",
        "Betalingstermijn": "1",
        "Betalingskenmerk": ZeepXsdSkipValue,
        "InExBTW": "1",
        "MutatieRegels": {
            "cMutatieRegel": [
                {
                    "BedragInvoer": 1.0,
                    "BedragExclBTW": 1.0,
                    "BedragBTW": 1.0,
                    "BedragInclBTW": 1.0,
                    "BTWCode": "1",
                    "BTWPercentage": 1.0,
                    "TegenrekeningCode": "1",
                    "KostenplaatsID": 1,
                }
            ]
        },
    }


def test_mutatie_fully_filled():
    """Test Mutatie."""
    mutatie = Mutatie(
        mutatie_nummer=1,
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer=1,
        boekstuk="1",
        omschrijving="1",
        betalingstermijn="1",
        betalingskenmerk="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=[
            MutatieRegel(
                bedrag_invoer=1.0,
                bedrag_exclusief_btw=1.0,
                bedrag_btw=1.0,
                bedrag_inclusief_btw=1.0,
                btw_code="1",
                btw_percentage=1.0,
                tegenrekening_code="1",
                kostenplaats_id=1,
            )
        ],
    )
    assert mutatie.export() == {
        "MutatieNr": 1,
        "Soort": "1",
        "Datum": "2020-01-01",
        "Rekening": "1",
        "RelatieCode": "1",
        "Factuurnummer": 1,
        "Boekstuk": "1",
        "Omschrijving": "1",
        "Betalingstermijn": "1",
        "Betalingskenmerk": "1",
        "InExBTW": "1",
        "MutatieRegels": {
            "cMutatieRegel": [
                {
                    "BedragInvoer": 1.0,
                    "BedragExclBTW": 1.0,
                    "BedragBTW": 1.0,
                    "BedragInclBTW": 1.0,
                    "BTWCode": "1",
                    "BTWPercentage": 1.0,
                    "TegenrekeningCode": "1",
                    "KostenplaatsID": 1,
                }
            ]
        },
    }


def test_mutatie_to_string():
    """Test MutatieRegel."""
    mutatie = Mutatie(
        mutatie_nummer=1,
        soort="1",
        datum="2020-01-01",
        rekening="1",
        relatie_code="1",
        factuur_nummer=1,
        boekstuk="1",
        omschrijving="1",
        betalingstermijn="1",
        betalingskenmerk="1",
        inclusief_exclusief_btw="1",
        mutatie_regels=[
            MutatieRegel(
                bedrag_invoer=1.0,
                bedrag_exclusief_btw=1.0,
                bedrag_btw=1.0,
                bedrag_inclusief_btw=1.0,
                btw_code="1",
                btw_percentage=1.0,
                tegenrekening_code="1",
                kostenplaats_id=1,
            )
        ],
    )

    print(f"\n\n{mutatie.to_string()}\n\n")
    assert (
        mutatie.to_string()
        == """Mutatie:
--------
Mutatienummer        : 1
Soort                : 1
Rekening             : 1
RelatieCode          : 1
Factuurnummer        : 1
Omschrijving         : 1
Betalingstermijn     : 1
Inclusief/exclusief  : 1
Boekstuk             : 1
Betalingskenmerk     : 1
Mutatieregels        : 1
----------------------
Mutatieregel:
-------------
BedragInvoer         : 1.0
Bedrag Exclusief BTW : 1.0
Bedrag BTW           : 1.0
Bedrag met BTW       : 1.0
Btw code             : 1
Btw percentage       : 1.0
Tegenrekening        : 1
Kostenplaats ID      : 1
"""
    )
