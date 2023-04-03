"""Fake Eboekhouden api server."""
from decimal import Decimal
import datetime


class MockServices:
    """Mock services."""

    def OpenSession(self, Username, SecurityCode1, SecurityCode2):
        """Open a fake session."""
        return {
            "SessionID": "test",
            "ErrorMsg": None,
        }

    def GetMutaties(self, SessionID, SecurityCode2, cFilter):
        """Get fake mutaties."""
        if cFilter["MutatieNr"] == "test":
            return {
                "ErrorMsg": None,
                "Mutaties": None,
            }
        else:
            return {
                "ErrorMsg": None,
                "Mutaties": {
                    "cMutatieList": [
                        {
                            "MutatieNr": 175,
                            "Soort": "FactuurVerstuurd",
                            "Datum": datetime.datetime(2023, 4, 1, 0, 0),
                            "Rekening": "1300",
                            "RelatieCode": "36",
                            "Factuurnummer": "test-123",
                            "Boekstuk": None,
                            "Omschrijving": "Import via api",
                            "Betalingstermijn": "14",
                            "InExBTW": "IN",
                            "MutatieRegels": {
                                "cMutatieListRegel": [
                                    {
                                        "BedragInvoer": Decimal("121"),
                                        "BedragExclBTW": Decimal("100"),
                                        "BedragBTW": Decimal("21"),
                                        "BedragInclBTW": Decimal("121"),
                                        "BTWCode": "HOOG_VERK_21",
                                        "BTWPercentage": Decimal("21"),
                                        "Factuurnummer": "test-123",
                                        "TegenrekeningCode": "8140",
                                        "KostenplaatsID": 0,
                                    },
                                    {
                                        "BedragInvoer": Decimal("242"),
                                        "BedragExclBTW": Decimal("200"),
                                        "BedragBTW": Decimal("42"),
                                        "BedragInclBTW": Decimal("242"),
                                        "BTWCode": "HOOG_VERK_21",
                                        "BTWPercentage": Decimal("21"),
                                        "Factuurnummer": "test-123",
                                        "TegenrekeningCode": "8140",
                                        "KostenplaatsID": 0,
                                    },
                                ]
                            },
                        }
                    ]
                },
            }
        return {
            "ErrorMsg": None,
            "Mutaties": {
                "cMutatieList": [
                    {
                        "MutatieNr": 175,
                        "Soort": "FactuurVerstuurd",
                        "Datum": datetime.datetime(2023, 4, 1, 0, 0),
                        "Rekening": "1300",
                        "RelatieCode": "36",
                        "Factuurnummer": "test-123",
                        "Boekstuk": None,
                        "Omschrijving": "Import via api",
                        "Betalingstermijn": "14",
                        "InExBTW": "IN",
                        "MutatieRegels": {
                            "cMutatieListRegel": [
                                {
                                    "BedragInvoer": Decimal("121"),
                                    "BedragExclBTW": Decimal("100"),
                                    "BedragBTW": Decimal("21"),
                                    "BedragInclBTW": Decimal("121"),
                                    "BTWCode": "HOOG_VERK_21",
                                    "BTWPercentage": Decimal("21"),
                                    "Factuurnummer": "test-123",
                                    "TegenrekeningCode": "8140",
                                    "KostenplaatsID": 0,
                                },
                                {
                                    "BedragInvoer": Decimal("242"),
                                    "BedragExclBTW": Decimal("200"),
                                    "BedragBTW": Decimal("42"),
                                    "BedragInclBTW": Decimal("242"),
                                    "BTWCode": "HOOG_VERK_21",
                                    "BTWPercentage": Decimal("21"),
                                    "Factuurnummer": "test-123",
                                    "TegenrekeningCode": "8140",
                                    "KostenplaatsID": 0,
                                },
                            ]
                        },
                    },
                ]
            },
        }

    def AddMutatie(self, SessionID, SecurityCode2, oMut):
        """Add a fake mutatie."""
        if oMut["MutatieNr"] != "test":
            return {
                "ErrorMsg": None,
                "MutatieNr": None,
            }
        return {
            "ErrorMsg": None,
            "MutatieNr": oMut["MutatieNr"],
        }


class MockServer:
    """Mock server."""

    def __init__(self, server_url: str) -> None:
        """Mock api initiation."""
        self._server_url = server_url
        self.service = MockServices()
