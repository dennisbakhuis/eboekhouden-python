from zeep.xsd import SkipValue as ZeepXsdSkipValue

from eboekhouden_python.models import MutatieRegel


def test_mutatie_regel_fully_filled():
    """Test MutatieRegel."""
    mutatie_regel = MutatieRegel(
        bedrag_invoer=1.0,
        bedrag_exclusief_btw=1.0,
        bedrag_btw=1.0,
        bedrag_inclusief_btw=1.0,
        btw_code="1",
        btw_percentage=1.0,
        tegenrekening_code="1",
        kostenplaats_id=1,
    )
    assert mutatie_regel.export() == {
        "BedragInvoer": 1.0,
        "BedragExclBTW": 1.0,
        "BedragBTW": 1.0,
        "BedragInclBTW": 1.0,
        "BTWCode": "1",
        "BTWPercentage": 1.0,
        "TegenrekeningCode": "1",
        "KostenplaatsID": 1,
    }


def test_mutatie_regel_partially_filled():
    """Test MutatieRegel."""
    mutatie_regel = MutatieRegel(
        bedrag_invoer=1.0,
        bedrag_exclusief_btw=1.0,
        bedrag_btw=1.0,
        bedrag_inclusief_btw=1.0,
        btw_code="1",
        btw_percentage=1.0,
        tegenrekening_code="1",
    )
    assert mutatie_regel.export() == {
        "BedragInvoer": 1.0,
        "BedragExclBTW": 1.0,
        "BedragBTW": 1.0,
        "BedragInclBTW": 1.0,
        "BTWCode": "1",
        "BTWPercentage": 1.0,
        "TegenrekeningCode": "1",
        "KostenplaatsID": ZeepXsdSkipValue,
    }
