"""
Tests for the core module (statistical calculations).
"""

import pytest

from pim.core import calcular_media, calcular_mediana, calcular_moda


class TestCalcularMedia:
    """Tests for calcular_media function."""

    def test_media_with_integers(self) -> None:
        """Test mean calculation with integers."""
        assert calcular_media([1, 2, 3, 4, 5]) == 3.0

    def test_media_with_floats(self) -> None:
        """Test mean calculation with floats."""
        assert calcular_media([1.5, 2.5, 3.5]) == 2.5

    def test_media_single_value(self) -> None:
        """Test mean calculation with a single value."""
        assert calcular_media([5]) == 5.0

    def test_media_empty_list(self) -> None:
        """Test mean calculation with empty list returns None."""
        assert calcular_media([]) is None

    def test_media_with_zeros(self) -> None:
        """Test mean calculation with zeros."""
        assert calcular_media([0, 0, 0]) == 0.0

    def test_media_typical_grades(self) -> None:
        """Test mean calculation with typical grade values."""
        assert calcular_media([7.0, 8.0, 9.0, 10.0]) == 8.5


class TestCalcularMediana:
    """Tests for calcular_mediana function."""

    def test_mediana_odd_length(self) -> None:
        """Test median calculation with odd number of elements."""
        assert calcular_mediana([1, 3, 5]) == 3

    def test_mediana_even_length(self) -> None:
        """Test median calculation with even number of elements."""
        assert calcular_mediana([1, 2, 3, 4]) == 2.5

    def test_mediana_unsorted_list(self) -> None:
        """Test median calculation with unsorted list."""
        assert calcular_mediana([5, 2, 1, 4, 3]) == 3

    def test_mediana_single_value(self) -> None:
        """Test median calculation with a single value."""
        assert calcular_mediana([7]) == 7

    def test_mediana_empty_list(self) -> None:
        """Test median calculation with empty list returns None."""
        assert calcular_mediana([]) is None

    def test_mediana_two_values(self) -> None:
        """Test median calculation with two values."""
        assert calcular_mediana([4, 8]) == 6.0


class TestCalcularModa:
    """Tests for calcular_moda function."""

    def test_moda_single_mode(self) -> None:
        """Test mode calculation with single mode."""
        assert calcular_moda([1, 2, 2, 3]) == 2

    def test_moda_multiple_modes(self) -> None:
        """Test mode calculation with multiple modes."""
        result = calcular_moda([1, 1, 2, 2, 3])
        assert isinstance(result, list)
        assert 1 in result
        assert 2 in result

    def test_moda_all_unique(self) -> None:
        """Test mode calculation when all values are unique."""
        assert calcular_moda([1, 2, 3, 4, 5]) is None

    def test_moda_empty_list(self) -> None:
        """Test mode calculation with empty list returns None."""
        assert calcular_moda([]) is None

    def test_moda_single_value(self) -> None:
        """Test mode calculation with single value returns None (no repetition)."""
        # A single value appearing once is not a mode
        assert calcular_moda([5]) is None

    def test_moda_all_same_value(self) -> None:
        """Test mode calculation when all values are the same."""
        assert calcular_moda([3, 3, 3, 3]) == 3

    def test_moda_with_floats(self) -> None:
        """Test mode calculation with float values."""
        assert calcular_moda([1.5, 1.5, 2.5, 3.5]) == 1.5
