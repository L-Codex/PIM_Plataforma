"""
IO module for loading and saving student data.
"""

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .data import disciplinas

logger = logging.getLogger(__name__)

# Default data file path
DEFAULT_DATA_PATH = Path("data/alunos.json")


class DataLoadError(Exception):
    """Exception raised when loading data fails."""

    pass


class DataSaveError(Exception):
    """Exception raised when saving data fails."""

    pass


@dataclass
class Aluno:
    """Dataclass representing a student."""

    nome: str
    email: str
    senha: str
    notas: Dict[str, List[float]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Initialize notes for all disciplines if not provided."""
        if not self.notas:
            self.notas = {disc: [] for disc in disciplinas}
        else:
            # Ensure all disciplines exist in notas
            for disc in disciplinas:
                if disc not in self.notas:
                    self.notas[disc] = []

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Aluno":
        """Create an Aluno instance from a dictionary."""
        return cls(
            nome=data.get("nome", ""),
            email=data.get("email", ""),
            senha=data.get("senha", ""),
            notas=data.get("notas", {}),
        )


def get_data_path(custom_path: Optional[str] = None) -> Path:
    """
    Get the path for the data file.

    Args:
        custom_path: Optional custom path. If not provided, uses DEFAULT_DATA_PATH.

    Returns:
        Path object for the data file.
    """
    if custom_path:
        return Path(custom_path)

    # Check environment variable for custom path
    env_path = os.environ.get("PIM_DATA_PATH")
    if env_path:
        return Path(env_path)

    return DEFAULT_DATA_PATH


def carregar_dados(caminho: Optional[str] = None) -> List[Aluno]:
    """
    Load student data from a JSON file.

    Args:
        caminho: Optional path to the JSON file. If not provided, uses default path.

    Returns:
        List of Aluno objects.

    Raises:
        DataLoadError: If there's an error loading the data.
    """
    path = get_data_path(caminho)
    logger.info(f"Loading student data from {path}")

    if not path.exists():
        logger.info(f"Data file {path} does not exist, returning empty list")
        return []

    try:
        with open(path, "r", encoding="utf-8") as arquivo:
            data = json.load(arquivo)

        if not isinstance(data, list):
            logger.error(f"Invalid data format in {path}: expected list, got {type(data)}")
            raise DataLoadError(f"Invalid data format: expected list, got {type(data)}")

        alunos = [Aluno.from_dict(item) for item in data]
        logger.info(f"Successfully loaded {len(alunos)} students")
        return alunos

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {path}: {e}")
        raise DataLoadError(f"Invalid JSON format in {path}: {e}") from e
    except OSError as e:
        logger.error(f"Failed to read file {path}: {e}")
        raise DataLoadError(f"Failed to read file {path}: {e}") from e


def salvar_dados(alunos: List[Aluno], caminho: Optional[str] = None) -> None:
    """
    Save student data to a JSON file.

    Args:
        alunos: List of Aluno objects to save.
        caminho: Optional path to the JSON file. If not provided, uses default path.

    Raises:
        DataSaveError: If there's an error saving the data.
    """
    path = get_data_path(caminho)
    logger.info(f"Saving {len(alunos)} students to {path}")

    try:
        # Ensure parent directory exists
        path.parent.mkdir(parents=True, exist_ok=True)

        data = [aluno.to_dict() for aluno in alunos]

        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(data, arquivo, indent=4, ensure_ascii=False)

        logger.info(f"Successfully saved data to {path}")

    except OSError as e:
        logger.error(f"Failed to write file {path}: {e}")
        raise DataSaveError(f"Failed to write file {path}: {e}") from e
    except (TypeError, ValueError) as e:
        logger.error(f"Failed to serialize data: {e}")
        raise DataSaveError(f"Failed to serialize data: {e}") from e
