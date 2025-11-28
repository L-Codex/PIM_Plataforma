"""
Core module containing statistical calculation functions.
"""

import logging
from typing import List, Optional, Union

logger = logging.getLogger(__name__)


def calcular_media(lista: List[float]) -> Optional[float]:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        lista: List of numbers to calculate the mean.

    Returns:
        The arithmetic mean, or None if the list is empty.
    """
    if not lista:
        logger.warning("Attempted to calculate mean of empty list")
        return None
    return sum(lista) / len(lista)


def calcular_mediana(lista: List[float]) -> Optional[float]:
    """
    Calculate the median of a list of numbers.

    Args:
        lista: List of numbers to calculate the median.

    Returns:
        The median value, or None if the list is empty.
    """
    if not lista:
        logger.warning("Attempted to calculate median of empty list")
        return None

    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]


def calcular_moda(lista: List[float]) -> Optional[Union[float, List[float]]]:
    """
    Calculate the mode of a list of numbers.

    Args:
        lista: List of numbers to calculate the mode.

    Returns:
        A single mode value if there's only one, a list of modes if there are multiple,
        or None if the list is empty or all values are unique.
    """
    if not lista:
        logger.warning("Attempted to calculate mode of empty list")
        return None

    frequencias: dict[float, int] = {}
    for valor in lista:
        frequencias[valor] = frequencias.get(valor, 0) + 1

    maior_freq = max(frequencias.values())

    # If all values appear only once, there's no mode
    if maior_freq == 1:
        return None

    modas = [k for k, v in frequencias.items() if v == maior_freq]

    # If all values have the same frequency and appear more than once, no mode
    if len(modas) == len(lista):
        return None

    return modas[0] if len(modas) == 1 else modas
