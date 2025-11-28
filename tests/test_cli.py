"""
Tests for the CLI module.
"""

import tempfile
from io import StringIO
from unittest.mock import patch

import pytest

from pim.cli import (
    fazer_perguntas,
    registrar_aluno,
    ver_notas,
)
from pim.data import disciplinas
from pim.io import Aluno


class TestFazerPerguntas:
    """Tests for fazer_perguntas function."""

    def test_fazer_perguntas_all_correct(self) -> None:
        """Test quiz with all correct answers."""
        # All answers in perguntas are 'A' for most questions
        # Simulate answering 'A' for all questions
        disciplina = "Matemática e Estatística"

        with patch("builtins.input", return_value="A"):
            nota = fazer_perguntas(disciplina)

        # All 10 questions correct = 10.0
        assert nota == 10.0

    def test_fazer_perguntas_all_wrong(self) -> None:
        """Test quiz with all wrong answers."""
        disciplina = "Matemática e Estatística"

        # Answer 'Z' which is never correct
        with patch("builtins.input", return_value="Z"):
            nota = fazer_perguntas(disciplina)

        assert nota == 0.0

    def test_fazer_perguntas_partial_correct(self) -> None:
        """Test quiz with partial correct answers."""
        disciplina = "Matemática e Estatística"

        # Create a sequence of answers: 5 correct (A), 5 wrong (Z)
        answers = iter(["A", "A", "A", "A", "A", "Z", "Z", "Z", "Z", "Z"])

        with patch("builtins.input", side_effect=lambda _: next(answers)):
            nota = fazer_perguntas(disciplina)

        # 5 out of 10 correct = 5.0
        assert nota == 5.0

    def test_fazer_perguntas_nonexistent_discipline(self) -> None:
        """Test quiz with non-existent discipline."""
        with patch("builtins.input", return_value="A"):
            nota = fazer_perguntas("Disciplina Inexistente")

        assert nota == 0.0


class TestRegistrarAluno:
    """Tests for registrar_aluno function."""

    def test_registrar_aluno_success(self) -> None:
        """Test successful student registration."""
        alunos: list[Aluno] = []

        with tempfile.TemporaryDirectory() as tmpdir:
            import os

            os.environ["PIM_DATA_PATH"] = f"{tmpdir}/alunos.json"

            inputs = iter(["Test User", "test@example.com", "password123"])
            with patch("builtins.input", side_effect=lambda _: next(inputs)):
                registrar_aluno(alunos)

            del os.environ["PIM_DATA_PATH"]

        assert len(alunos) == 1
        assert alunos[0].nome == "Test User"
        assert alunos[0].email == "test@example.com"
        assert alunos[0].senha == "password123"

    def test_registrar_aluno_empty_name(self) -> None:
        """Test registration with empty name fails."""
        alunos: list[Aluno] = []

        inputs = iter(["", "test@example.com", "password123"])
        with patch("builtins.input", side_effect=lambda _: next(inputs)):
            registrar_aluno(alunos)

        assert len(alunos) == 0

    def test_registrar_aluno_duplicate_email(self) -> None:
        """Test registration with duplicate email fails."""
        alunos = [Aluno(nome="Existing", email="test@example.com", senha="pass")]

        inputs = iter(["New User", "test@example.com", "newpass"])
        with patch("builtins.input", side_effect=lambda _: next(inputs)):
            registrar_aluno(alunos)

        # Should still have only the original user
        assert len(alunos) == 1
        assert alunos[0].nome == "Existing"


class TestVerNotas:
    """Tests for ver_notas function."""

    def test_ver_notas_with_grades(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test displaying grades for a student with grades."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="pass")
        aluno.notas["Matemática e Estatística"] = [7.0, 8.0, 9.0]

        ver_notas(aluno)

        captured = capsys.readouterr()
        assert "Notas de Test" in captured.out
        assert "[7.0, 8.0, 9.0]" in captured.out
        assert "Média: 8.00" in captured.out
        assert "Mediana: 8.00" in captured.out

    def test_ver_notas_no_grades(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test displaying grades for a student without grades."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="pass")

        ver_notas(aluno)

        captured = capsys.readouterr()
        assert "Notas de Test" in captured.out
        assert "Sem notas" in captured.out

    def test_ver_notas_moda_display(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test displaying mode in grades."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="pass")
        aluno.notas["Matemática e Estatística"] = [7.0, 7.0, 8.0]

        ver_notas(aluno)

        captured = capsys.readouterr()
        assert "Moda: 7.0" in captured.out

    def test_ver_notas_moda_undefined(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test displaying undefined mode."""
        aluno = Aluno(nome="Test", email="test@example.com", senha="pass")
        aluno.notas["Matemática e Estatística"] = [7.0, 8.0, 9.0]  # All unique

        ver_notas(aluno)

        captured = capsys.readouterr()
        assert "Moda: Não definida" in captured.out
