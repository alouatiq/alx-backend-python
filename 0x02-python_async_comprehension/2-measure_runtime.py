#!/usr/bin/env python3
"""Measure execution time for running async_comprehension in parallel"""
import asyncio
import time
from importlib import import_module
from typing import Callable


async_comprehension = import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of running async_comprehension 4 times in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
