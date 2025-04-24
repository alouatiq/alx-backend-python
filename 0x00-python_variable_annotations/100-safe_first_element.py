#!/usr/bin/env python3
'''Function safe_first_element'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence if it exists, else None.'''
    if lst:
        return lst[0]
    return None
