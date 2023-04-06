"""Model for GetMutaties filter in e-Boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd.const import SkipValue as ZeepXsdSkipValue


@dataclass
class RelatieFilter:
    """
    Filter for GetRelaties in e-Boekhouden.nl.

    Trefwoord: Zoekt in de velden code, bedrijfsnaam, plaats, contactpersoon, e-mailadres en soort.
    """

    trefwoord: Optional[str] = None
    code: Optional[str] = None
    id: Optional[int] = None

    def export(self):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        return dict(
            Trefwoord=self.trefwoord or ZeepXsdSkipValue,
            Code=self.code or ZeepXsdSkipValue,
            ID=self.id or ZeepXsdSkipValue,
        )
