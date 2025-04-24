#!/usr/bin/env python3
'''Function safely_get_value'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    '''Safely retrieves a value from a dictionary or returns a default.'''
    if key in dct:
        return dct[key]
    return default
