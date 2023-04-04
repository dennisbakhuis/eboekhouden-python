from eboekhouden_python.models import RelatieFilter


def test_relatie_filter_partially_filled():
    """Test RelatieFilter."""
    relatie_filter = RelatieFilter(
        trefwoord="1",
        code="1",
        id=1,
    )
    assert relatie_filter.export() == {
        "Trefwoord": "1",
        "Code": "1",
        "ID": 1,
    }


def test_relatie_filter_fully_filled():
    """Test RelatieFilter."""
    relatie_filter = RelatieFilter(
        trefwoord="1",
        code="1",
        id=1,
    )
    assert relatie_filter.export() == {
        "Trefwoord": "1",
        "Code": "1",
        "ID": 1,
    }
