"""
PIM Platform - Student Review and Assessment Platform.

This package provides a CLI application for student registration,
content review, and assessments across multiple disciplines.
"""

from .cli import main
from .core import calcular_media, calcular_mediana, calcular_moda
from .data import conteudos, disciplinas, perguntas
from .io import Aluno, carregar_dados, salvar_dados

__version__ = "1.0.0"
__all__ = [
    "main",
    "calcular_media",
    "calcular_mediana",
    "calcular_moda",
    "disciplinas",
    "conteudos",
    "perguntas",
    "Aluno",
    "carregar_dados",
    "salvar_dados",
]
