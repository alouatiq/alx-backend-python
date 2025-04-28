#!/usr/bin/env python3
"""Basic asynchronous coroutine that waits for a random delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay up to
    max_delay seconds and returns the delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
