"""Relation model of E-boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd import SkipValue as ZeepXsdSkipValue


@dataclass
class Relatie:
    """Relation model of E-boekhouden.nl."""

    relatie_code: str  # String
    bedrijf_particulier: str  # String
    bedrijf: str  # String

    add_datum: Optional[str] = None  # String
    id: Optional[int] = None  # int
    contact_person: Optional[str] = None  # String
    geslacht: Optional[str] = None  # String
    adres: Optional[str] = None  # String
    postcode: Optional[str] = None  # String
    plaats: Optional[str] = None  # String
    land: Optional[str] = None  # String
    adres2: Optional[str] = None  # String
    postcode2: Optional[str] = None  # String
    plaats2: Optional[str] = None  # String
    land2: Optional[str] = None  # String
    telefoon: Optional[str] = None  # String
    gsm: Optional[str] = None  # String
    fax: Optional[str] = None  # String
    email: Optional[str] = None  # String
    website: Optional[str] = None  # String
    notitie: Optional[str] = None  # String
    btw_nummer: Optional[str] = None  # String
    kvk_nummer: Optional[str] = None  # String
    aanhef: Optional[str] = None  # String
    iban: Optional[str] = None  # String
    bic: Optional[str] = None  # String
    def1: Optional[str] = None  # String
    def2: Optional[str] = None  # String
    def3: Optional[str] = None  # String
    def4: Optional[str] = None  # String
    def5: Optional[str] = None  # String
    def6: Optional[str] = None  # String
    def7: Optional[str] = None  # String
    def8: Optional[str] = None  # String
    def9: Optional[str] = None  # String
    def10: Optional[str] = None  # String
    leden_administratie: Optional[str] = None  # String
    geen_email: Optional[str] = None  # String
    gb_id: Optional[str] = None  # String
    nieuwsbrief_groepen_count: Optional[str] = None  # int

    def export(self, additional_fields: bool = False):
        """Export to structure used in SOAP of E-Boekhouden.nl."""
        export_dict = dict(
            ID=self.id or ZeepXsdSkipValue,
            AddDatum=self.add_datum or ZeepXsdSkipValue,
            BP=self.bedrijf_particulier,
            Code=self.relatie_code,
            Bedrijf=self.bedrijf,
            Contactpersoon=self.contact_person or ZeepXsdSkipValue,
            Geslacht=self.geslacht or ZeepXsdSkipValue,
            Adres=self.adres or ZeepXsdSkipValue,
            Postcode=self.postcode or ZeepXsdSkipValue,
            Plaats=self.plaats or ZeepXsdSkipValue,
            Land=self.land or ZeepXsdSkipValue,
            Adres2=self.adres2 or ZeepXsdSkipValue,
            Postcode2=self.postcode2 or ZeepXsdSkipValue,
            Plaats2=self.plaats2 or ZeepXsdSkipValue,
            Land2=self.land2 or ZeepXsdSkipValue,
            Telefoon=self.telefoon or ZeepXsdSkipValue,
            GSM=self.gsm or ZeepXsdSkipValue,
            FAX=self.fax or ZeepXsdSkipValue,
            Email=self.email or ZeepXsdSkipValue,
            Site=self.website or ZeepXsdSkipValue,
            Notitie=self.notitie or ZeepXsdSkipValue,
            BTWNummer=self.btw_nummer or ZeepXsdSkipValue,
            KvkNummer=self.kvk_nummer or ZeepXsdSkipValue,
            Aanhef=self.aanhef or ZeepXsdSkipValue,
            IBAN=self.iban or ZeepXsdSkipValue,
            BIC=self.bic or ZeepXsdSkipValue,
            GeenEmail=self.geen_email or ZeepXsdSkipValue,
            Gb_ID=self.gb_id or ZeepXsdSkipValue,
            NieuwsbriefgroepenCount=self.nieuwsbrief_groepen_count or ZeepXsdSkipValue,
        )
        if additional_fields:
            return dict(
                **export_dict,
                Def1=self.def1 or ZeepXsdSkipValue,
                Def2=self.def2 or ZeepXsdSkipValue,
                Def3=self.def3 or ZeepXsdSkipValue,
                Def4=self.def4 or ZeepXsdSkipValue,
                Def5=self.def5 or ZeepXsdSkipValue,
                Def6=self.def6 or ZeepXsdSkipValue,
                Def7=self.def7 or ZeepXsdSkipValue,
                Def8=self.def8 or ZeepXsdSkipValue,
                Def9=self.def9 or ZeepXsdSkipValue,
                Def10=self.def10 or ZeepXsdSkipValue,
                LedenAdministratie=self.leden_administratie or ZeepXsdSkipValue,
            )
        return export_dict
