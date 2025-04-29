#!/usr/bin/env python3
"""Async comprehension that collects 10 numbers from async_generator"""
from typing import List
from 0-async_generator import async_generator  # Or: from . import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from an async generator"""
    return [i async for i in async_generator()]
