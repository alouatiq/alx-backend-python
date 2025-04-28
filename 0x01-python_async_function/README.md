# 0x01. Python - Async

## Project Description
This project focuses on asynchronous programming in Python. You will learn how to use `async` and `await` syntax, create concurrent coroutines, manage tasks using `asyncio`, and work with random delays. Understanding asynchronous programming is crucial for building efficient and scalable applications, especially for back-end development.

## Learning Objectives
By the end of this project, you should be able to:

- Explain the `async` and `await` syntax in Python.
- Execute asynchronous programs using `asyncio`.
- Run concurrent coroutines.
- Create and manage `asyncio` tasks.
- Use the `random` module effectively.

## Requirements
- All code must be written in Python 3.7.
- Code must comply with pycodestyle (version 2.5.x).
- Each file must start with `#!/usr/bin/env python3`.
- Each function, coroutine, and module must have a proper docstring.
- Code must be executable and end with a new line.

## Project Structure

```
0x01-python_async_function/
|│
|├── 0-basic_async_syntax.py  # Basic async coroutine with random delay
|├── 1-concurrent_coroutines.py # Execute multiple coroutines concurrently
|├── 2-measure_runtime.py       # Measure total execution time
|├── 3-tasks.py                  # Create and return asyncio Task
|├── 4-tasks.py                  # Execute multiple tasks concurrently
|└── README.md                   # Project documentation
```

## Files Description

- **0-basic_async_syntax.py**
  - Implements `wait_random(max_delay=10)`: waits for a random delay.

- **1-concurrent_coroutines.py**
  - Implements `wait_n(n, max_delay)`: spawns `n` coroutines and returns their delays in ascending order.

- **2-measure_runtime.py**
  - Implements `measure_time(n, max_delay)`: measures average execution time per coroutine.

- **3-tasks.py**
  - Implements `task_wait_random(max_delay)`: returns an asyncio.Task.

- **4-tasks.py**
  - Implements `task_wait_n(n, max_delay)`: spawns multiple tasks and returns delays in ascending order.

## How to Run

1. Make sure you are using Python 3.7.
2. Ensure all files are executable (`chmod +x filename.py`).
3. Use `asyncio.run()` to execute coroutines.

Example:
```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

## References
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio – Asynchronous I/O documentation](https://docs.python.org/3/library/asyncio.html)
- [random.uniform() documentation](https://docs.python.org/3/library/random.html#random.uniform)

---

> This project is part of the **ALX Backend Specialization** program.

