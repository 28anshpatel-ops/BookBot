# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# BookBot

BookBot is a Python-based Command-Line Interface (CLI) application designed to analyze text files (such as digital books) and generate detailed statistical reports. It processes full-length books to extract total word counts and frequency analysis for every alphabetic character, presented in a clean, sorted report.

---

## Features

- **Word Count Analysis:** Reads full text files and computes total word counts.
- **Character Frequency Analysis:** Counts the occurrence of all characters, handling case-insensitivity (e.g., treating `'A'` and `'a'` as the same character).
- **Sorted Statistical Output:** Filters for alphabetic characters and presents frequency data ordered from most frequent to least frequent.
- **Command-Line Interface:** Takes target text paths as command-line arguments, complete with usage validation and error messaging.

---

## Directory Structure

.
├── main.py
├── stats.py
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
└── README.md
