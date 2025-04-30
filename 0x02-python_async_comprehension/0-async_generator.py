#!/usr/bin/env python3
"""Module that provides an async generator
for yielding random floats."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random float between 0
    and 10 every second for 10 iterations."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
