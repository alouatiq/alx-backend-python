#!/usr/bin/env python3
'''Function zoom_array'''
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    '''Return a new list where each item is repeated by the factor.'''
    return [item for item in lst for _ in range(factor)]


if __name__ == "__main__":
    array = (12, 72, 91)
    zoom_2x = zoom_array(array)
    print(zoom_2x)  # [12, 12, 72, 72, 91, 91]

    zoom_3x = zoom_array(array, 3)
    print(zoom_3x)  # [12, 12, 12, 72, 72, 72, 91, 91, 91]
