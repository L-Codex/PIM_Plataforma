"""
Tests for the IO module (data loading and saving).
"""

import json
import os
import tempfile
from pathlib import Path

import pytest

from pim.data import disciplinas
from pim.io import (
    Aluno,
    DataLoadError,
    DataSaveError,
    carregar_dados,
    get_data_path,
    salvar_dados,
)


class TestAluno:
    """Tests for the Aluno dataclass."""

    def test_aluno_creation(self) -> None:
        """Test creating an Aluno instance."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="password")
        assert aluno.nome == "Test"
        assert aluno.email == "test@example.com"
        assert aluno.senha == "password"

    def test_aluno_default_notas(self) -> None:
        """Test that Aluno has default empty notes for all disciplines."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="password")
        for disc in disciplinas:
            assert disc in aluno.notas
            assert aluno.notas[disc] == []

    def test_aluno_with_notas(self) -> None:
        """Test creating an Aluno with existing notes."""
        notas = {"Matemática e Estatística": [8.0, 9.0]}
        aluno = Aluno(
            nome="Test", email="test@example.com", senha="password", notas=notas
        )
        assert aluno.notas["Matemática e Estatística"] == [8.0, 9.0]
        # Other disciplines should be initialized as empty
        assert aluno.notas["TIC"] == []

    def test_aluno_to_dict(self) -> None:
        """Test converting Aluno to dictionary."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="password")
        d = aluno.to_dict()
        assert d["nome"] == "Test"
        assert d["email"] == "test@example.com"
        assert d["senha"] == "password"
        assert "notas" in d

    def test_aluno_from_dict(self) -> None:
        """Test creating Aluno from dictionary."""
        data = {
            "nome": "Test",
            "email": "test@example.com",
            "senha": "password",
            "notas": {"Matemática e Estatística": [7.0]},
        }
        aluno = Aluno.from_dict(data)
        assert aluno.nome == "Test"
        assert aluno.email == "test@example.com"
        assert aluno.notas["Matemática e Estatística"] == [7.0]


class TestGetDataPath:
    """Tests for get_data_path function."""

    def test_default_path(self) -> None:
        """Test that default path is used when no arguments."""
        # Clear environment variable if set
        old_env = os.environ.pop("PIM_DATA_PATH", None)
        try:
            path = get_data_path()
            assert path == Path("data/alunos.json")
        finally:
            if old_env:
                os.environ["PIM_DATA_PATH"] = old_env

    def test_custom_path(self) -> None:
        """Test that custom path is used when provided."""
        path = get_data_path("/custom/path.json")
        assert path == Path("/custom/path.json")

    def test_env_variable_path(self) -> None:
        """Test that environment variable path is used."""
        old_env = os.environ.get("PIM_DATA_PATH")
        try:
            os.environ["PIM_DATA_PATH"] = "/env/path.json"
            path = get_data_path()
            assert path == Path("/env/path.json")
        finally:
            if old_env:
                os.environ["PIM_DATA_PATH"] = old_env
            else:
                os.environ.pop("PIM_DATA_PATH", None)


class TestCarregarSalvarDados:
    """Tests for carregar_dados and salvar_dados functions."""

    def test_carregar_nonexistent_file(self) -> None:
        """Test loading from non-existent file returns empty list."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "nonexistent.json")
            alunos = carregar_dados(path)
            assert alunos == []

    def test_salvar_and_carregar(self) -> None:
        """Test saving and loading data."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "test_alunos.json")
            aluno = Aluno(nome="Test", email="test@example.com", senha="password")
            aluno.notas["Matemática e Estatística"].append(8.5)

            salvar_dados([aluno], path)
            loaded = carregar_dados(path)

            assert len(loaded) == 1
            assert loaded[0].nome == "Test"
            assert loaded[0].email == "test@example.com"
            assert loaded[0].notas["Matemática e Estatística"] == [8.5]

    def test_salvar_multiple_alunos(self) -> None:
        """Test saving multiple students."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "test_alunos.json")
            alunos = [
                Aluno(nome="Alice", email="alice@example.com", senha="pass1"),
                Aluno(nome="Bob", email="bob@example.com", senha="pass2"),
            ]

            salvar_dados(alunos, path)
            loaded = carregar_dados(path)

            assert len(loaded) == 2
            assert loaded[0].nome == "Alice"
            assert loaded[1].nome == "Bob"

    def test_carregar_malformed_json(self) -> None:
        """Test loading malformed JSON raises DataLoadError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "malformed.json")
            with open(path, "w") as f:
                f.write("{ invalid json }")

            with pytest.raises(DataLoadError):
                carregar_dados(path)

    def test_carregar_invalid_format(self) -> None:
        """Test loading non-list JSON raises DataLoadError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "invalid.json")
            with open(path, "w") as f:
                json.dump({"not": "a list"}, f)

            with pytest.raises(DataLoadError):
                carregar_dados(path)

    def test_salvar_creates_directory(self) -> None:
        """Test that salvar_dados creates parent directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "subdir", "nested", "alunos.json")
            aluno = Aluno(nome="Test", email="test@example.com", senha="password")

            salvar_dados([aluno], path)

            assert os.path.exists(path)
            loaded = carregar_dados(path)
            assert len(loaded) == 1
