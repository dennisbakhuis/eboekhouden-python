from zeep.xsd import SkipValue as ZeepXsdSkipValue
import pytest

from eboekhouden_python.models import MutatieRegel
from eboekhouden_python.constants import BtwCode


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


def test_mutatie_regel_from_bedrag():
    """Test MutatieRegel."""
    mutatie_regel = MutatieRegel.from_bedrag(
        bedrag_invoer=121,
        btw_code=BtwCode.hoog_verkoop_21,
        tegenrekening_code="1",
    )
    assert mutatie_regel.export() == {
        "BedragInvoer": "121.00",
        "BedragExclBTW": "100.00",
        "BedragBTW": "21.00",
        "BedragInclBTW": "121.00",
        "BTWCode": "HOOG_VERK_21",
        "BTWPercentage": "21",
        "TegenrekeningCode": "1",
        "KostenplaatsID": ZeepXsdSkipValue,
    }

    mutatie_regel = MutatieRegel.from_bedrag(
        bedrag_invoer=109,
        btw_code=BtwCode.laag_verkoop_9,
        tegenrekening_code="1",
    )
    assert mutatie_regel.export() == {
        "BedragInvoer": "109.00",
        "BedragExclBTW": "100.00",
        "BedragBTW": "9.00",
        "BedragInclBTW": "109.00",
        "BTWCode": "LAAG_VERK_9",
        "BTWPercentage": "9",
        "TegenrekeningCode": "1",
        "KostenplaatsID": ZeepXsdSkipValue,
    }

    mutatie_regel = MutatieRegel.from_bedrag(
        bedrag_invoer=100,
        btw_code=BtwCode.geen,
        tegenrekening_code="1",
    )
    assert mutatie_regel.export() == {
        "BedragInvoer": "100.00",
        "BedragExclBTW": "100.00",
        "BedragBTW": "0.00",
        "BedragInclBTW": "100.00",
        "BTWCode": "GEEN",
        "BTWPercentage": "0",
        "TegenrekeningCode": "1",
        "KostenplaatsID": ZeepXsdSkipValue,
    }

    with pytest.raises(ValueError):
        MutatieRegel.from_bedrag(
            bedrag_invoer=100,
            btw_code="",
            tegenrekening_code="1",
        )


def test_mutatie_to_string():
    """Test MutatieRegel."""
    mutatie_regel = MutatieRegel(
        bedrag_invoer="1.21",
        bedrag_exclusief_btw="1.0",
        bedrag_btw="0.21",
        bedrag_inclusief_btw="1.21",
        btw_code="1",
        btw_percentage="21",
        tegenrekening_code="1",
    )
    assert (
        mutatie_regel.to_string()
        == """Mutatieregel:
-------------
BedragInvoer         : 1.21
Bedrag Exclusief BTW : 1.0
Bedrag BTW           : 0.21
Bedrag met BTW       : 1.21
Btw code             : 1
Btw percentage       : 21
Tegenrekening        : 1
Kostenplaats ID      : None
"""
    )
