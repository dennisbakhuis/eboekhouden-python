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
                            "Omschrijving": "test",
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
        # return {
        #     "ErrorMsg": None,
        #     "Mutaties": {
        #         "cMutatieList": [
        #             {
        #                 "MutatieNr": 175,
        #                 "Soort": "FactuurVerstuurd",
        #                 "Datum": datetime.datetime(2023, 4, 1, 0, 0),
        #                 "Rekening": "1300",
        #                 "RelatieCode": "36",
        #                 "Factuurnummer": "test-123",
        #                 "Boekstuk": None,
        #                 "Omschrijving": "Import via api",
        #                 "Betalingstermijn": "14",
        #                 "InExBTW": "IN",
        #                 "MutatieRegels": {
        #                     "cMutatieListRegel": [
        #                         {
        #                             "BedragInvoer": Decimal("121"),
        #                             "BedragExclBTW": Decimal("100"),
        #                             "BedragBTW": Decimal("21"),
        #                             "BedragInclBTW": Decimal("121"),
        #                             "BTWCode": "HOOG_VERK_21",
        #                             "BTWPercentage": Decimal("21"),
        #                             "Factuurnummer": "test-123",
        #                             "TegenrekeningCode": "8140",
        #                             "KostenplaatsID": 0,
        #                         },
        #                         {
        #                             "BedragInvoer": Decimal("242"),
        #                             "BedragExclBTW": Decimal("200"),
        #                             "BedragBTW": Decimal("42"),
        #                             "BedragInclBTW": Decimal("242"),
        #                             "BTWCode": "HOOG_VERK_21",
        #                             "BTWPercentage": Decimal("21"),
        #                             "Factuurnummer": "test-123",
        #                             "TegenrekeningCode": "8140",
        #                             "KostenplaatsID": 0,
        #                         },
        #                     ]
        #                 },
        #             },
        #         ]
        #     },
        # }

    def GetRelaties(self, SessionID, SecurityCode2, cFilter):
        """Get fake relaties."""
        if cFilter["Code"] == "test":
            return {
                "ErrorMsg": None,
                "Relaties": None,
            }
        return {
            "ErrorMsg": None,
            "Relaties": {
                "cRelatie": [
                    {
                        "Code": "36",
                        "Bedrijf": "Test",
                        "BP": "P",
                        "Adres": "1234AB",
                        "Postcode": "Test",
                        "Land": "NL",
                    }
                ]
            },
        }

    def AddMutatie(self, SessionID, SecurityCode2, oMut):
        """Add a fake mutatie."""
        if oMut["MutatieNr"] != "test":
            return {
                "ErrorMsg": None,
                "Mutatienummer": None,
            }
        return {
            "ErrorMsg": None,
            "Mutatienummer": oMut["MutatieNr"],
        }

    def AddRelatie(self, SessionID, SecurityCode2, oRel):
        """Add a fake mutatie."""
        if oRel["Code"] != "test":
            return {
                "ErrorMsg": None,
                "Rel_ID": None,
            }
        return {
            "ErrorMsg": None,
            "Rel_ID": oRel["Code"],
        }

    def GetOpenPosten(self, SessionID, SecurityCode2, OpSoort):
        """Get fake open posten."""
        return {
            "ErrorMsg": None,
            "Openposten": {
                "cOpenPost": [
                    {
                        "MutDatum": datetime.datetime(2023, 4, 1, 0, 0),
                        "MutFactuur": "INV-001",
                        "RelCode": "REL-001",
                        "RelBedrijf": "Test Company",
                        "Bedrag": "1000.00",
                        "Voldaan": "500.00",
                        "Openstaand": "500.00",
                    }
                ]
            },
        }


class MockServer:
    """Mock server."""

    def __init__(self, server_url: str) -> None:
        """Mock api initiation."""
        self._server_url = server_url
        self.service = MockServices()
