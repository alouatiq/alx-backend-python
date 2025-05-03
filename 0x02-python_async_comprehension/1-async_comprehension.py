#!/usr/bin/env python3
"""Async comprehension that collects 10 numbers from async_generator"""
from typing import List
from importlib import import_module

# Dynamically import the module (since its
# name starts with a digit and has a hyphen)
async_generator = import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from an async generator"""
    return [i async for i in async_generator()]
