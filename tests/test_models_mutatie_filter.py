from zeep.xsd import SkipValue as ZeepXsdSkipValue

from eboekhouden_python.models import MutatieFilter


def test_mutatie_filter_fully_filled():
    """Test MutatieFilter."""
    mutatie_filter = MutatieFilter(
        mutatie_nummer=1,
        mutatie_nummer_van=1,
        mutatie_nummer_totmet=1,
        factuur_nummer=1,
        datum_van="2020-01-01",
        datum_totmet="2020-01-01",
    )
    assert mutatie_filter.export() == {
        "MutatieNr": 1,
        "MutatieNrVan": 1,
        "MutatieNrTm": 1,
        "Factuurnummer": 1,
        "DatumVan": "2020-01-01",
        "DatumTm": "2020-01-01",
    }


def test_mutatie_filter_partially_filled():
    """Test MutatieFilter."""
    mutatie_filter = MutatieFilter(
        factuur_nummer=1,
    )
    assert mutatie_filter.export() == {
        "MutatieNr": ZeepXsdSkipValue,
        "MutatieNrVan": ZeepXsdSkipValue,
        "MutatieNrTm": ZeepXsdSkipValue,
        "Factuurnummer": 1,
        "DatumVan": ZeepXsdSkipValue,
        "DatumTm": ZeepXsdSkipValue,
    }
