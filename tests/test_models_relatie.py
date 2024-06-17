from zeep.xsd import SkipValue as ZeepXsdSkipValue

from eboekhouden_python.models import Relatie
from eboekhouden_python.constants import BedrijfParticulier


def test_relatie_partially_filled():
    """Test Relatie."""
    relatie = Relatie(
        relatie_code="1",
        bedrijf_particulier=BedrijfParticulier.particulier,
        bedrijf="1",
        adres="1",
        postcode="1",
        plaats="1",
        land="1",
    )
    assert relatie.export() == dict(
        ID=ZeepXsdSkipValue,
        AddDatum=ZeepXsdSkipValue,
        BP=BedrijfParticulier.particulier,
        Code="1",
        Bedrijf="1",
        Contactpersoon=ZeepXsdSkipValue,
        Geslacht=ZeepXsdSkipValue,
        Adres="1",
        Postcode="1",
        Plaats="1",
        Land="1",
        Adres2=ZeepXsdSkipValue,
        Postcode2=ZeepXsdSkipValue,
        Plaats2=ZeepXsdSkipValue,
        Land2=ZeepXsdSkipValue,
        Telefoon=ZeepXsdSkipValue,
        GSM=ZeepXsdSkipValue,
        FAX=ZeepXsdSkipValue,
        Email=ZeepXsdSkipValue,
        Site=ZeepXsdSkipValue,
        Notitie=ZeepXsdSkipValue,
        BTWNummer=ZeepXsdSkipValue,
        KvkNummer=ZeepXsdSkipValue,
        Aanhef=ZeepXsdSkipValue,
        IBAN=ZeepXsdSkipValue,
        BIC=ZeepXsdSkipValue,
        GeenEmail=ZeepXsdSkipValue,
        Gb_ID=ZeepXsdSkipValue,
        NieuwsbriefgroepenCount=ZeepXsdSkipValue,
    )


def test_relatie_partially_filled_additional_fields():
    """Test Relatie."""
    relatie = Relatie(
        relatie_code="1",
        bedrijf_particulier=BedrijfParticulier.particulier,
        bedrijf="1",
        adres="1",
        postcode="1",
        plaats="1",
        land="1",
        def1="1",
        def2="1",
        def3="1",
        def4="1",
        def5="1",
        def6="1",
        def7="1",
        def8="1",
        def9="1",
        def10="1",
        leden_administratie="1",
    )
    assert relatie.export(additional_fields=True) == dict(
        ID=ZeepXsdSkipValue,
        AddDatum=ZeepXsdSkipValue,
        BP=BedrijfParticulier.particulier,
        Code="1",
        Bedrijf="1",
        Contactpersoon=ZeepXsdSkipValue,
        Geslacht=ZeepXsdSkipValue,
        Adres="1",
        Postcode="1",
        Plaats="1",
        Land="1",
        Adres2=ZeepXsdSkipValue,
        Postcode2=ZeepXsdSkipValue,
        Plaats2=ZeepXsdSkipValue,
        Land2=ZeepXsdSkipValue,
        Telefoon=ZeepXsdSkipValue,
        GSM=ZeepXsdSkipValue,
        FAX=ZeepXsdSkipValue,
        Email=ZeepXsdSkipValue,
        Site=ZeepXsdSkipValue,
        Notitie=ZeepXsdSkipValue,
        BTWNummer=ZeepXsdSkipValue,
        KvkNummer=ZeepXsdSkipValue,
        Aanhef=ZeepXsdSkipValue,
        IBAN=ZeepXsdSkipValue,
        BIC=ZeepXsdSkipValue,
        GeenEmail=ZeepXsdSkipValue,
        Gb_ID=ZeepXsdSkipValue,
        NieuwsbriefgroepenCount=ZeepXsdSkipValue,
        Def1="1",
        Def2="1",
        Def3="1",
        Def4="1",
        Def5="1",
        Def6="1",
        Def7="1",
        Def8="1",
        Def9="1",
        Def10="1",
        LA="1",
    )


def test_relatie_to_string():
    """Test to_string."""
    relatie = Relatie(
        relatie_code="1",
        bedrijf_particulier=BedrijfParticulier.particulier,
        bedrijf="1",
        adres="1",
        postcode="1",
        plaats="1",
        land="1",
    )

    print(f"\n\n{relatie.to_string()}\n\n")
    assert relatie.to_string() == "Relatie(relatie_code=1, bedrijf_particulier=P, bedrijf=1)"
