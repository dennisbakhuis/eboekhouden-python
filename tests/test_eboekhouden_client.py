import pytest

from eboekhouden_python import EboekhoudenClient
from eboekhouden_python.models import Mutatie, Relatie, OpenPost
from eboekhouden_python.constants import BedrijfParticulier, OpenPostSoort

from .mock_server import MockServer


mutatie = Mutatie(
    soort="test",
    datum="2023-04-01",
    rekening="test",
    relatie_code="test",
    factuur_nummer="test",
    omschrijving="test",
    betalingstermijn="test",
    inclusief_exclusief_btw="test",
    mutatie_regels=[],
    mutatie_nummer="test",
)


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
    assert isinstance(mutaties[0], Mutatie)

    # Test to retrieve "zeep" object (here it is a dict)
    mutaties = client.get_mutaties(return_zeep_object=True)
    assert len(mutaties) == 1
    assert isinstance(mutaties[0], dict)

    # Test if we get empty list when no mutaties are found
    mutaties = client.get_mutaties(mutatie_nummer="test")
    assert len(mutaties) == 0


def test_eboekhouden_client_add_mutatie(client):
    # Test to add a mutatie
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
    assert isinstance(relatie[0], Relatie)

    # Test to retrieve "zeep" object (here it is a dict)
    relatie = client.get_relaties(return_zeep_object=True)
    assert len(relatie) == 1
    assert isinstance(relatie[0], dict)

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


def test_eboekhouden_client_mutatie_exists(client):
    # Test if we can check if a mutatie exists
    assert client.mutatie_exists(mutatie)


def test_eboekhouden_client_get_open_posten(client):
    # Test if we can get open posten
    open_posten = client.get_open_posten(OpenPostSoort.debiteuren)
    assert len(open_posten) == 1
    assert isinstance(open_posten[0], OpenPost)
    assert open_posten[0].factuur_nummer == "INV-001"
    assert open_posten[0].relatie_code == "REL-001"
    assert open_posten[0].relatie_bedrijf == "Test Company"
    assert open_posten[0].factuur_bedrag == "1000.00"
    assert open_posten[0].bedrag_voldaan == "500.00"
    assert open_posten[0].bedrag_openstaand == "500.00"
    assert open_posten[0].soort == OpenPostSoort.debiteuren
