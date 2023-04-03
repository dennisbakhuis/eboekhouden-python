import pytest

from eboekhouden_python import EboekhoudenClient
from eboekhouden_python.models import Mutatie, Relatie
from eboekhouden_python.constants import BedrijfParticulier

from .mock_server import MockServer


def test_eboekhouden_client_init_fail(monkeypatch):
    # Test if the client fails when no credentials are provided
    monkeypatch.delenv("EBOEKHOUDEN_USERNAME", raising=False)
    with pytest.raises(ValueError):
        client = EboekhoudenClient()

    # Fix credentials
    monkeypatch.setenv("EBOEKHOUDEN_USERNAME", "test")
    monkeypatch.setenv("EBOEKHOUDEN_CODE1", "test")
    monkeypatch.setenv("EBOEKHOUDEN_CODE2", "test")

    # Test if the client fails when no server URL is provided
    monkeypatch.delenv("EBOEKHOUDEN_SERVER_URL", raising=False)
    with pytest.raises(ValueError):
        client = EboekhoudenClient(server_url=None)

    # Test initiation of client
    monkeypatch.setenv("EBOEKHOUDEN_SERVER_URL", "test_server")
    monkeypatch.setattr("eboekhouden_python.eboekhouden_client.ZeepClient", MockServer)
    client = EboekhoudenClient(server_url=None)
    assert client._username == "test"
    assert client._code1 == "test"
    assert client._code2 == "test"
    assert client._server_url == "test_server"


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("EBOEKHOUDEN_USERNAME", "test")
    monkeypatch.setenv("EBOEKHOUDEN_CODE1", "test")
    monkeypatch.setenv("EBOEKHOUDEN_CODE2", "test")
    monkeypatch.setenv("EBOEKHOUDEN_SERVER_URL", "test_server")
    monkeypatch.setattr("eboekhouden_python.eboekhouden_client.ZeepClient", MockServer)
    return EboekhoudenClient(server_url=None)


def test_eboekhouden_client_check_response(client):
    # Test if the client fails when the has error information missing
    with pytest.raises(ValueError):
        client._check_response({})

    # Test wrong credentials
    with pytest.raises(ValueError):
        client._check_response({"ErrorMsg": "Error code 1: Invalid username or password"})  # fake

    # Test other service typical error responses
    with pytest.raises(ValueError):
        client._check_response(
            {
                "ErrorMsg": {
                    "LastErrorCode": "some error",
                    "LastErrorDescription": "some description",
                }
            }
        )  # fake


def test_eboekhouden_client_get_session_id(client):
    client.get_session_id()
    assert client._session_id == "test"


def test_eboekhouden_client_get_mutaties(client):
    # Test if we can get mutaties
    mutaties = client.get_mutaties()
    assert len(mutaties) == 1

    # Test if we get empty list when no mutaties are found
    mutaties = client.get_mutaties(mutatie_nummer="test")
    assert len(mutaties) == 0


def test_eboekhouden_client_add_mutatie(client):
    # Test to add a mutatie
    mutatie = Mutatie(
        soort="test",
        datum="test",
        rekening="test",
        relatie_code="test",
        factuur_nummer="test",
        omschrijving="test",
        betalingstermijn="test",
        inclusief_exclusief_btw="test",
        mutatie_regels=[],
        mutatie_nummer="test",
    )
    response = client.add_mutatie(mutatie)
    assert response == "test"

    # Test if client fails adding a new mutatie
    with pytest.raises(ValueError):
        mutatie.mutatie_nummer = "Nope"
        client.add_mutatie(mutatie)


def test_eboekhouden_client_get_relaties(client):
    # Test if we can get relatie
    relatie = client.get_relaties()
    assert len(relatie) == 1

    # Test if we get empty list when no relatie is found
    relatie = client.get_relaties(relatie_code="test")
    assert len(relatie) == 0


def test_eboekhouden_client_add_relatie(client):
    # Test to add a relatie
    relatie = Relatie(
        relatie_code="test",
        bedrijf="test",
        bedrijf_particulier=BedrijfParticulier.particulier,
    )
    response = client.add_relatie(relatie)
    assert response == "test"

    # Test if client fails adding a new relatie
    with pytest.raises(ValueError):
        relatie.relatie_code = "Nope"
        client.add_relatie(relatie)
