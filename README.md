# Simple Order Processing System

This lab demonstrates how to create a simple order processing system using a **queue** to manage and process incoming orders in a **First-In, First-Out (FIFO)** manner. This approach is similar to how real-world e-commerce platforms handle order intake and execution, showing how fundamental data structures can be used for core functionality.

---

## Prerequisites

- **Python** must be installed on your computer.
- A Python package manager like `uv` or `pip` is needed.

---

## How to Use

1.  **Initialize a virtual environment**: You can use `uv`, `pip`, or `venv` for this. The example uses `uv`:

    ```bash
    uv venv .venv
    ```

2.  **Activate the virtual environment**:

    ```bash
    source .venv/bin/activate
    ```

3.  **Run the application**:

    ```bash
    uv run main.py
    ```

    Once the application is running, it will add incoming orders to a queue and process them in the order they were received.

---

## Tools & Libraries Used

- `collections.deque`: This is used to implement the queue because it provides efficient `append` and `pop` operations from both ends, which is ideal for a FIFO structure.
- `json`: Loads a product catalogue from a JSON file into memory for product lookups.

---

## What I Learned

- How to use Python's `deque` from the `collections` module to create an efficient FIFO queue.
- The importance of queues as a foundational data structure in building real-time order processing systems.
- How simple data structures can act as the backbone for larger, more complex systems.
- How to model a product catalogue as a simple in-memory database for indexing and searching.
- How Python dictionaries function as hash maps, enabling fast O(1) product lookups.
- How to use typings like `Dict` to create a clear interface for a product catalogue.
- How to implement a simple database abstraction layer using the repository pattern to handle basic data access operations for a table.
- How to Use Private Attributes and Methods in Python’s Object-Oriented Programming
- How to Implement the Bubble Sort Algorithm in Python to Sort a List of Items
