"""
Test module
"""
import pytest
from typing import List
from src.metrics import count_average

@pytest.mark.parametrize(
                        "numbers, expected_mean", 
                        [([1,2,3], 2),
                         ([10,20,30], 20),
                         ([1,3,5], 3)
                        ]
                        )

def test_count_average(numbers: List[int], expected_mean: float) -> None:
    """
    test
    """
    assert count_average(numbers) == expected_mean