"""Mutatie types used by E-boekhouden.nl."""
from .string_enum import StringEnum


class MutatieSoort(StringEnum):
    """Mutatie types used by E-boekhouden.nl."""

    factuur_ontvangen = "FactuurOntvangen"  # Factuur ontvangen
    factuur_verstuurd = "FactuurVerstuurd"  # Factuur verstuurd
    factuurbetaling_ontvangen = "FactuurbetalingOntvangen"  # Factuurbetaling ontvangen
    factuurbetaling_verstuurd = "FactuurbetalingVerstuurd"  # Factuurbetaling verstuurd
    geld_ontvangen = "GeldOntvangen"  # Geld ontvangen
    geld_uitgegeven = "GeldUitgegeven"  # Geld uitgegeven
    memoriaal = "Memoriaal"  # Memoriaal
