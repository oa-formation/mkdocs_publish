import pytest

def north_korea():
    return "Best Korea"

def test_empty_function():
    assert north_korea() == "Best Korea"
