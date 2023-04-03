"""Btw codes used by E-boekhouden.nl."""
from .string_enum import StringEnum


class BtwCode(StringEnum):
    """Btw codes used by E-boekhouden.nl."""

    hoog_verkoop_19 = "HOOG_VERK"  # BTW hoog, verkopen 19%
    hoog_verkoop_21 = "HOOG_VERK_21"  # BTW hoog, verkopen 21%
    laag_verkoop = "LAAG_VERK"  # BTW laag, verkopen voor 2019 6% daarna 9%
    laag_verkoop_9 = "LAAG_VERK_9"  # BTW laag, verkopen 9%
    verlegd_verkoop_9 = "VERL_VERK_L9"  # BTW Verlegd 9% (1e op de btw-aangifte)
    verlegd_verkoop_21 = "VERL_VERK"  # BTW Verlegd 21% (1e op de btw-aangifte)
    afwijkend = "AFW"  # Afwijkend btw-tarief
    buiten_eu_verkoop_0 = "BU_EU_VERK"  # Leveringen naar buiten de EU 0%
    binnen_eu_verkoop_0 = "BI_EU_VERK"  # Goederen naar binnen de EU 0%
    binnen_eu_diensten_0 = "BI_EU_VERK_D"  # Diensten naar binnen de EU 0%
    afstand_verkopen_0 = "AFST_VERK"  # Afstandsverkopen naar binnen de EU 0%
    laag_inkopen = "LAAG_INK"  # BTW laag, inkopen voor 2019 6% daarna 9%
    laag_inkopen_9 = "LAAG_INK_9"  # BTW laag, inkopen 9%
    verlegd_inkopen_9 = "VERL_INK_L9"  # BTW verlegd, laag, inkopen
    hoog_inkopen = "HOOG_INK"  # BTW hoog, inkopen
    hoog_inkopen_21 = "HOOG_INK_21"  # BTW hoog, inkopen 21%
    verlegd_inkopen_21 = "VERL_INK"  # BTW verlegd, hoog, inkopen
    afwijkend_verkoop = "AFW_VERK"  # Afwijkend btw-tarief verkoop
    buiten_eu_inkopen_0 = "BU_EU_INK"  # Leveringen/diensten van buiten de EU 0%
    binnen_eu_inkopen_0 = "BI_EU_INK"  # Leveringen/diensten van binnen de EU 0%
    geen = "GEEN"  # Geen BTW


btw_codes_hoog = [
    BtwCode.hoog_verkoop_19,
    BtwCode.hoog_verkoop_21,
    BtwCode.hoog_inkopen,
    BtwCode.hoog_inkopen_21,
    BtwCode.verlegd_inkopen_21,
]
btw_codes_laag = [
    BtwCode.laag_verkoop,
    BtwCode.laag_verkoop_9,
    BtwCode.verlegd_verkoop_9,
    BtwCode.laag_inkopen,
    BtwCode.laag_inkopen_9,
]
btw_codes_geen = [x for x in BtwCode if x not in btw_codes_hoog + btw_codes_laag]
