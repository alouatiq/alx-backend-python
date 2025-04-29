#!/usr/bin/env python3
"""Measure execution time for four parallel async comprehensions"""
import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and return the total time"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
