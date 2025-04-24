#!/usr/bin/env python3
'''Function sum_mixed_list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a list with ints and floats.'''
    return sum(mxd_lst)
