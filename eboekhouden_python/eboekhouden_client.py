"""Eboekhouden client."""
from typing import Optional, Any
import os

from zeep import Client as ZeepClient

from .models import (
    MutatieFilter,
    Mutatie,
    RelatieFilter,
    Relatie,
)


class EboekhoudenClient:
    """Eboekhouden client."""

    def __init__(
        self,
        username: Optional[str] = None,
        code1: Optional[str] = None,
        code2: Optional[str] = None,
        server_url: Optional[str] = "https://soap.e-boekhouden.nl/soap.asmx?wsdl",
    ):
        """Initialize Eboekhouden client."""
        self._username = username or os.environ.get("EBOEKHOUDEN_USERNAME")
        self._code1 = code1 or os.environ.get("EBOEKHOUDEN_CODE1")
        self._code2 = code2 or os.environ.get("EBOEKHOUDEN_CODE2")
        self._server_url = server_url or os.environ.get("EBOEKHOUDEN_SERVER_URL")

        if self._username is None or self._code1 is None or self._code2 is None:
            raise ValueError("Incomplete Eboekhouden credentials")

        if self._server_url is None or self._server_url == "":
            raise ValueError("Server URL Eboekhouden missing")

        self._client = ZeepClient(self._server_url)

        self.get_session_id()

    def _check_response(self, response) -> None:
        """Check for general response for errors."""
        if "ErrorMsg" not in response:
            raise ValueError("Unexpected response, do you have the correct server URL?")

        if response["ErrorMsg"] is not None:
            if "LastErrorCode" in response["ErrorMsg"]:
                if response["ErrorMsg"]["LastErrorCode"] is not None:
                    error_code = response["ErrorMsg"]["LastErrorCode"]
                    description = response["ErrorMsg"]["LastErrorDescription"]
                    raise ValueError(
                        f"{error_code}: {description}",
                    )
            else:
                if response["ErrorMsg"] is not None:
                    print(response["ErrorMsg"])
                    raise ValueError(
                        f"Error: {response['ErrorMsg']}",
                    )

    def get_session_id(self):
        """Get session ID."""
        response = self._client.service.OpenSession(
            Username=self._username,
            SecurityCode1=self._code1,
            SecurityCode2=self._code2,
        )
        self._check_response(response)

        self._session_id = response["SessionID"]

    def get_mutaties(
        self,
        mutatie_nummer: Optional[str] = None,
        mutatie_nummer_van: Optional[str] = None,
        mutatie_nummer_totmet: Optional[str] = None,
        factuur_nummer: Optional[str] = None,
        datum_van: Optional[str] = None,
        datum_totmet: Optional[str] = None,
        return_zeep_object: bool = False,
    ) -> list[Any]:
        """
        Get mutaties.

        Returns a zeep.objects.cMutatieList, might want to convert to Relatie
        """
        mutatie_filter = MutatieFilter(
            mutatie_nummer=mutatie_nummer,
            mutatie_nummer_van=mutatie_nummer_van,
            mutatie_nummer_totmet=mutatie_nummer_totmet,
            factuur_nummer=factuur_nummer,
            datum_van=datum_van,
            datum_totmet=datum_totmet,
        )

        self.get_session_id()

        mutaties = self._client.service.GetMutaties(
            SessionID=self._session_id,
            SecurityCode2=self._code2,
            cFilter=mutatie_filter.export(),
        )

        self._check_response(mutaties)

        if mutaties["Mutaties"] is None:
            return []

        if return_zeep_object:
            return mutaties["Mutaties"]["cMutatieList"]

        mutatie_objects = [Mutatie.from_zeep(x) for x in mutaties["Mutaties"]["cMutatieList"]]
        return mutatie_objects

    def add_mutatie(self, mutatie: Mutatie) -> str:
        """Add mutatie."""
        self.get_session_id()

        exported_mutatie = mutatie.export()

        response = self._client.service.AddMutatie(
            SessionID=self._session_id,
            SecurityCode2=self._code2,
            oMut=exported_mutatie,
        )

        self._check_response(response)

        if response["Mutatienummer"] is None or response["Mutatienummer"] == 0:
            raise ValueError("Error adding mutatie")

        return response["Mutatienummer"]

    def get_relaties(
        self,
        trefwoord: Optional[str] = None,
        relatie_code: Optional[str] = None,
        id: Optional[int] = None,
        return_zeep_object: bool = False,
    ) -> list[Any]:
        """Get relaties."""
        relatie_filter = RelatieFilter(trefwoord=trefwoord, code=relatie_code, id=id)

        self.get_session_id()

        relaties = self._client.service.GetRelaties(
            SessionID=self._session_id,
            SecurityCode2=self._code2,
            cFilter=relatie_filter.export(),
        )

        self._check_response(relaties)

        if relaties["Relaties"] is None:
            return []

        if return_zeep_object:
            return relaties["Relaties"]["cRelatie"]

        relatie_objects = [Relatie.from_zeep(x) for x in relaties["Relaties"]["cRelatie"]]
        return relatie_objects

    def add_relatie(self, relatie: Relatie, additional_fields: bool = False) -> str:
        """Add mutatie."""
        self.get_session_id()

        response = self._client.service.AddRelatie(
            SessionID=self._session_id,
            SecurityCode2=self._code2,
            oRel=relatie.export(additional_fields),
        )

        self._check_response(response)

        if response["Rel_ID"] is None:
            raise ValueError("Error adding mutatie")

        return response["Rel_ID"]

    def mutatie_exists(self, mutatie: Mutatie) -> bool:
        """Check if mutatie already exists in E-boekhouden by matching the date and omschrijving."""
        found_mutaties = self.get_mutaties(
            datum_van=mutatie.datum,
            datum_totmet=mutatie.datum,
        )
        omschrijvingen = [x.omschrijving for x in found_mutaties]
        return mutatie.omschrijving in omschrijvingen
