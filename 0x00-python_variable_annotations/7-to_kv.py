#!/usr/bin/env python3
'''Function to_kv'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple with a string and the square of the value.'''
    return (k, float(v ** 2))
