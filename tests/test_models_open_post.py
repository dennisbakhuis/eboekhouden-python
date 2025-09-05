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
