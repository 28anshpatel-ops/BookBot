# Design Decisions and Justifications

## 1. Separation of Concerns (Modular Architecture)
* **Decision:** Split the codebase into two distinct files: `main.py` for user interaction and file orchestration, and `stats.py` for text computation.
* **Justification:** Coupling input/output operations with core analytical logic creates rigid, untestable code. Isolating statistical functions inside `stats.py` ensures they remain pure and side-effect free. `main.py` acts strictly as an entry point. If the interface changes from a CLI to a web page or mobile app, `stats.py` requires zero modification.

## 2. Two-Phase Data Processing (Dictionary to Sorted List)
* **Decision:** Aggregate character counts inside a hash map (dictionary), then transform key-value pairs into a list of dictionary objects for sorting.
* **Justification:** Dictionaries allow O(1) average time complexity for character lookups and updates during full-text scanning. However, sorting raw dictionary structures directly is clunky. Converting data into a list of structured records (`[{"char": c, "num": n}]`) enables clean sorting using Python's native `sort()` method with a custom extractor key (`sort_on`).

## 3. Deferred Filtering over Early Elimination
* **Decision:** Track every single character (including spaces, punctuation, and digits) inside `get_chars_dict()`, but filter for alphabetic characters (`char.isalpha()`) inside `print_report()`.
* **Justification:** Filtering during data intake bakes presentation rules directly into the analysis module. Preserving raw counts in `stats.py` maintains underlying data integrity, allowing the underlying statistics to be repurposed later without altering the core counting logic.

## 4. Immediate Lowercase Normalization
* **Decision:** Execute `.lower()` on every character symbol prior to dictionary lookup and insertion.
* **Justification:** Text metrics demand case-insensitivity so that uppercase and lowercase variants ('T' and 't') map to the same letter bucket. Normalizing data immediately on intake avoids duplicate dictionary keys and removes the need for expensive secondary merging routines.

## 5. Defensive Input Handling via Guard Clauses
* **Decision:** Validate command-line arguments explicitly (`len(sys.argv) < 2`) at the program start and terminate execution via `sys.exit(1)`.
* **Justification:** Omitting argument checks causes Python to crash with raw `IndexError` tracebacks when users pass invalid arguments. Explicitly catching missing inputs guarantees clean terminal feedback, enforces correct CLI contract usage, and prevents execution on undefined paths.
