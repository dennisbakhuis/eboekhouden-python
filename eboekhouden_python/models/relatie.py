"""Relation model of E-boekhouden.nl."""
from dataclasses import dataclass
from typing import Optional

from zeep.xsd.const import SkipValue as ZeepXsdSkipValue
from zeep.helpers import serialize_object


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

    @classmethod
    def from_zeep(
        cls,
        zeep_object,
    ):  # pragma: no cover
        """Create a new instance from a zeep object."""
        serialized_relation = dict(serialize_object(zeep_object))
        if "AddDatum" in serialized_relation:
            serialized_relation["AddDatum"] = serialized_relation["AddDatum"].strftime("%Y-%m-%d")
        return cls(
            id=serialized_relation.get("ID"),
            add_datum=serialized_relation.get("AddDatum"),
            bedrijf_particulier=serialized_relation.get("BP"),  # type: ignore
            relatie_code=serialized_relation.get("Code"),  # type: ignore
            bedrijf=serialized_relation.get("Bedrijf"),  # type: ignore
            contact_person=serialized_relation.get("Contactpersoon"),
            geslacht=serialized_relation.get("Geslacht"),
            adres=serialized_relation.get("Adres"),
            postcode=serialized_relation.get("Postcode"),
            plaats=serialized_relation.get("Plaats"),
            land=serialized_relation.get("Land"),
            adres2=serialized_relation.get("Adres2"),
            postcode2=serialized_relation.get("Postcode2"),
            plaats2=serialized_relation.get("Plaats2"),
            land2=serialized_relation.get("Land2"),
            telefoon=serialized_relation.get("Telefoon"),
            gsm=serialized_relation.get("GSM"),
            fax=serialized_relation.get("Fax"),
            email=serialized_relation.get("Email"),
            website=serialized_relation.get("Website"),
            notitie=serialized_relation.get("Notitie"),
            btw_nummer=serialized_relation.get("BTWNummer"),
            kvk_nummer=serialized_relation.get("KVKNummer"),
            aanhef=serialized_relation.get("Aanhef"),
            iban=serialized_relation.get("IBAN"),
            bic=serialized_relation.get("BIC"),
            def1=serialized_relation.get("Def1"),
            def2=serialized_relation.get("Def2"),
            def3=serialized_relation.get("Def3"),
            def4=serialized_relation.get("Def4"),
            def5=serialized_relation.get("Def5"),
            def6=serialized_relation.get("Def6"),
            def7=serialized_relation.get("Def7"),
            def8=serialized_relation.get("Def8"),
            def9=serialized_relation.get("Def9"),
            def10=serialized_relation.get("Def10"),
            leden_administratie=serialized_relation.get("LA"),
            geen_email=serialized_relation.get("GeenEmail"),
            gb_id=serialized_relation.get("GBID"),
            nieuwsbrief_groepen_count=serialized_relation.get("NieuwsbriefGroepenCount"),
        )

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
                LA=self.leden_administratie or ZeepXsdSkipValue,
            )
        return export_dict

    def to_string(self):
        """Return string representation of this object."""
        return f"Relatie(relatie_code={self.relatie_code}, bedrijf_particulier={self.bedrijf_particulier}, bedrijf={self.bedrijf})"
