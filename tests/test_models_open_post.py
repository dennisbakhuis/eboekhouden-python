from zeep.xsd import SkipValue as ZeepXsdSkipValue
from eboekhouden_python.models import OpenPost


def test_open_post_partially_filled():
    """Test Open Post."""
    relatie = OpenPost(mutatie_datum="2000-01-01")
    assert relatie.export() == dict(
        MutDatum="2000-01-01",
        MutFactuur=ZeepXsdSkipValue,
        RelCode=ZeepXsdSkipValue,
        RelBedrijf=ZeepXsdSkipValue,
        Bedrag=ZeepXsdSkipValue,
        Voldaan=ZeepXsdSkipValue,
        Openstaand=ZeepXsdSkipValue,
    )


def test_open_post_to_string():
    """Test OpenPost to_string method."""
    open_post = OpenPost(
        mutatie_datum="2023-04-01",
        factuur_nummer="INV-123",
        bedrag_voldaan="500.00",
        bedrag_openstaand="250.00",
    )
    expected = "OpenPost(factuur_nummer=INV-123, bedrag_voldaan=500.00, bedrag_openstaand=250.00)"
    assert open_post.to_string() == expected


def test_open_post_to_string_with_none_values():
    """Test OpenPost to_string method with None values."""
    open_post = OpenPost(mutatie_datum="2023-04-01")
    expected = "OpenPost(factuur_nummer=None, bedrag_voldaan=None, bedrag_openstaand=None)"
    assert open_post.to_string() == expected
