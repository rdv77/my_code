"""
metrics
"""

from typing import List, Union


def count_average(nums: List[Union[int, float]]
                  ) -> float:
    """
    return mean
    
    Parameters
    -----------
    numbers: list of numbers to calculate mean
    
    Returns
    -----------
    float (the mean of the numbers)

    Notes
    -----------
    calc mean of the number of list

    Examples
    -----------
    >>> count_average([1,2,3,4,5])
    3.0
    """
    return sum(nums) / len(nums)
