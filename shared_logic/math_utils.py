"""Shared math utilities for financial tools."""

import numpy as np


def real_return(nominal: float, inflation: float) -> float:
    """Compute the real return given nominal return and inflation rate."""
    return (1 + nominal) / (1 + inflation) - 1
