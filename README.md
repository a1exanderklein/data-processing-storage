# Python InMemoryDB: A Simple In-Memory Database with Transactions

## Overview
This project implements a simple in-memory key-value database with transaction support. It supports:
- **begin_transaction()**: Starts a new transaction.
- **put(key, value)**: Adds or updates a key-value pair in the database (requires an active transaction).
- **get(key)**: Retrieves the value of a key, if it exists.
- **commit()**: Commits changes made during the transaction to the main database.
- **rollback()**: Reverts all changes made during the transaction.

## Setup Instructions
1. Ensure Python 3.9+ is installed.
2. Clone the repository:
   ```bash
   git clone [https://github.com/a1exanderklein/data-processing-storage.git]
   cd [data-processing-storage]
3. Run the test file:
    python -m unittest test.py

# Assignment Suggestions

To enhance this assignment for future use as an official assignment, consider the following modifications:

## Clarify Error Handling

Specify the exact types of exceptions that should be raised for different error conditions (e.g., `ValueError`, `TypeError`, or custom exception classes). This will ensure consistency across different implementations and make error handling clearer.

## Emphasize Automated Testing

Require students to write unit tests using a testing framework for their language of choice like `unittest` or `pytest`. This not only aids in grading but also ensures correctness of the code. 

## No Automated Testing Route

Alternatively, provide the students with a template and instructions on what you are testing for, so they can provide their file and the TAs will have their own unit tests to assess it.
